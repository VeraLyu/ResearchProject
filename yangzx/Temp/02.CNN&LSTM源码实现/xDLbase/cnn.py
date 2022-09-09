"""
CNN Layer Class
"""

import numpy as np
import time
import numba
import logging.config

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
from xDLUtils import Tools

# create logger
exec_abs = os.getcwd()
log_conf = exec_abs + '/config/logging.conf'
logging.config.fileConfig(log_conf)
logger = logging.getLogger('cnn')

# 卷积处理类
class ConvLayer(object):
    def __init__(self, LName, miniBatchesSize, i_size, channel, f_size, o_depth, o_size,
                 strides, activator, optimizerCls,optmParams, dataType,init_w):

        # 初始化超参数
        self.name = LName
        self.miniBatchesSize = miniBatchesSize
        self.i_size = i_size
        # 输入通道个数
        self.channel = channel
        self.f_size = f_size
        # 输出通道个数
        self.o_depth = o_depth
        self.o_size = o_size
        self.strides = strides
        self.activator = activator
        self.optimizerObj = optimizerCls(optmParams, dataType)
        self.dataType = dataType
        self.init_w = init_w
        # 卷积层权重矩阵 (输出通道，输入通道，卷积核长，卷积核高)
        self.w = init_w * np.random.randn(o_depth, channel, f_size, f_size).astype(self.dataType)
        self.b = np.zeros((o_depth, 1), dtype=dataType)
        self.out = []
        self.deltaPrev = []
        self.deltaOri = []
    # 预测时前向传播
    def inference(self, input):
        self.out = self.fp(input)
        return self.out

    # 前向传播,激活后输出
    def fp(self, input):
        # 进行卷积计算
        self.out = self.activator.activate(self.conv_efficient(input, self.w, self.b, self.o_size, self.name, self.strides))
        return self.out

    # 反向传播(误差和权参),先对输出误差求导再反向传播至上一层
    def bp(self, input, delta, lrt):
        self.deltaOri = self.activator.bp(delta, self.out)

        self.deltaPrev, dw, db = self.bp4conv(self.deltaOri, self.w, input, self.strides, 'd' + self.name)
        weight = (self.w,self.b)
        dweight = (dw,db)
        self.optimizerObj.getUpdWeights(weight,dweight, lrt)

        return self.deltaPrev

    # conv4dw,反向传播计算dw
    # 以卷积层输出误差为卷积核，对卷计层输入做卷积，得到卷积层w的梯度
    # 输入输出尺寸不变的过滤器 当s==1时，p=(f-1)/2
    # 入参:
    #     x规格: 根据x.ndim 判断入参的规格
    #           x.ndim=4:原始规格,未padding
    #                   batch * depth_i * row * col,  其中 depth_i为输入节点矩阵深度，
    #           x.ndim=3:x_col规格,已padding
    #                   前向:batch * (depth_i * filter_size * filter_size) * (out_size*out_size)
    #                   反向:batch * depth_i * ( filter_size * filter_size) * (out_size*out_size)
    #                   注意，反向传播时，x_col保持四个维度而不是前向传播的三个
    #     w规格: batches * depth_o  * filter_size * filter_size ， ，
    #           depth_o为过滤器个数或输出矩阵深度，
    #           w_row: batches * depth_o * ( filter_size * filter_size)
    #           此处的w是反向传播过来卷积层输出误差，没有depth_i这个维度
    #     b规格: 长度为 depth_o*1 的数组,b的长度即为过滤器个数或节点深度,和w的depth_o一致。
    #           conv4dw时,b为0
    #     output_size:conv4dw的输出矩阵尺寸,对应原始卷积层w的尺寸
    #     strides: 缺省为1
    #     x_v : False x未作矢量化,True x已作向量化(对第一层卷积适用，每个mini-batch多个Iteration时可提速)
    # 返回: 卷积层加权输出(co-relation)
    #       conv : batch * depth_o * depth_i * output_size * output_size
    def conv4dw(self, x, w, output_size, b=0, strides=1, x_v=False):
        batches = x.shape[0]
        depth_i = x.shape[1]
        filter_size = w.shape[2]  # 过滤器尺寸,对应卷积层误差矩阵尺寸
        x_per_filter = filter_size * filter_size
        depth_o = w.shape[1]

        if False == x_v:  # 原始规格:
            input_size = x.shape[2]  #
            p = int(((output_size - 1) * strides + filter_size - input_size) / 2)  # padding尺寸
            if p > 0:  # 需要padding处理
                x_pad = Tools.padding(x, p, self.dataType)
            else:
                x_pad = x
            logger.debug("vec4dw begin..")
            x_col = self.vectorize4convdw_batches(x_pad, filter_size, output_size, strides)
            logger.debug("vec4dw end..")
        else:  # x_col规格
            x_col = x

        w_row = w.reshape(batches, depth_o, x_per_filter)
        conv = np.zeros((batches, depth_i, depth_o, (output_size * output_size)), dtype=self.dataType)
        logger.debug("conv4dw matmul begin..")
        for batch in range(batches):
            for col in range(depth_i):
                conv[batch, col] = Tools.matmul(w_row[batch], x_col[batch, col])

        conv_sum = np.sum(conv, axis=0)
        # transpose而不是直接reshape避免错位
        conv = conv_sum.transpose(1, 0, 2).reshape(depth_o, depth_i, output_size, output_size)

        logger.debug("conv4dw matmul end..")
        return conv, x_col

    # conv_efficient,使用向量化和BLAS优化的卷积计算版本
    # 入参:
    #     x:前向传播时表示输入矩阵，反向传播时表示误差矩阵
    #     x规格: 根据x.ndim 判断入参的规格
    #           x.ndim=4:原始规格,未padding
    #                   batch * depth_i * row * col,  其中 depth_i为输入节点矩阵深度，
    #           x.ndim=3:x_col规格,已padding
    #                   batch * (depth_i * filter_size * filter_size) * (out_size*out_size)
    #     w规格: depth_o * depth_i * filter_size * filter_size ， ，
    #           depth_o为过滤器个数或输出矩阵深度，depth_i和 x的 depth一致
    #           w_row: depth_o * (depth_i * filter_size * filter_size)
    #     b规格: 长度为 depth_o*1 的数组,b的长度即为过滤器个数或节点深度,和w的depth_o一致，可以增加校验。
    #     output_size:卷积输出尺寸
    #     strides: 缺省为1
    #     vec_idx_key: vec_idx键
    # 返回: 卷积层加权输出(co-relation)
    #       conv : batch * depth_o * output_size * output_size
    def conv_efficient(self, x, w, b, output_size, vec_idx_key, strides=1):
        # 1.x.shape(32, 1, 28, 28)
        # 2.x.shape(32, 32, 14, 14)
        # -1.x.shape(32, 64, 14, 14)
        # -2.x.shape(32, 32, 28, 28)
        batches = x.shape[0]
        depth_i = x.shape[1]
        # 1.w.shape(32, 1, 5, 5)
        # 2.w.shape(64, 32, 5, 5)
        # -1.w.shape(32, 64, 5, 5)
        # -2.w.shape(1, 32, 5, 5)
        filter_size = w.shape[2]
        # 输出通道个数
        depth_o = w.shape[0]

        if 4 == x.ndim:  # 原始规格:
            input_size = x.shape[2]  #输入尺寸
            # 根据filter_size计算padding尺寸
            p = int(((output_size - 1) * strides + filter_size - input_size) / 2)
            # logger.debug("padding begin..")
            if p > 0:
                # 1.对原始图像进行padding处理，p=2，(32, 1, 28, 28)->(32, 1, 32, 32)
                # 2.对原始图像进行padding处理，p=2，(32, 32, 14, 14)->(32, 32, 18, 18)
                # -1.对原始图像进行padding处理，p=2，(32, 64, 14, 14)->(32, 64, 18, 18)
                # -2.对原始图像进行padding处理，p=2，(32, 32, 28, 28)->(32, 32, 32, 32)
                x_pad = Tools.padding(x, p, self.dataType)
            else:
                x_pad = x
            #st = time.time()
            #logger.debug("vecting begin..")
            # 使用向量化和BLAS优化的卷积计算，可以根据自己的硬件环境，在三种优化方式中选择较快的一种
            # 1.filter=5，output=28,x_pad.shape(32, 1, 32, 32)  => (32, 1*5*5, 28*28)  = x_col.shape(32, 25, 784) 
            # 2.filter=5，output=14,x_pad.shape(32, 32, 18, 18) => (32, 32*5*5, 14*14) = x_col.shape(32, 800, 196)
            # -1.filter=5，output=28,x_pad.shape(32, 64, 18, 18)  => (32, 64*5*5, 1*14)  = x_col.shape(32, 1600, 196)
            # -2.filter=5，output=28,x_pad.shape(32, 32, 32, 32)  => (32, 32*5*5, 28*28)  = x_col.shape(32, 800, 784)
            x_col = self.vectorize4conv_batches(x_pad, filter_size, output_size, strides)
            #x_col = spd.vectorize4conv_batches(x_pad, filter_size, output_size, strides)
            #x_col = vec_by_idx(x_pad, filter_size, filter_size,vec_idx_key,0, strides)
            #logger.debug("vecting end.. %f s" % (time.time() - st))
        else:  # x_col规格
            x_col = x
        # 1.将权重w.shape(32, 1, 5, 5)转化为与卷积结果x_col对应的维度，方便计算，w_row.shape(32, 25) 
        # 2.将权重w.shape(64, 32, 5, 5)转化为与卷积结果x_col对应的维度，方便计算，w_row.shape(64, 800)
        # -1.(32, 64, 5, 5)(32, 1600)
        # -2.(1, 32, 5, 5)(1, 800)
        w_row = w.reshape(depth_o, x_col.shape[1])
        # 1.(32, 32, 28*28) 构建卷积输出shape，通道数为depth_o=32
        # 2.(32, 64, 14*14) 构建卷积输出shape，通道数为depth_o=64
        # -1.(32, 32, 14*14) 构建卷积输出shape，通道数为depth_o=32
        # -2.(32, 1, 28*28) 构建卷积输出shape，通道数为depth_o=1
        conv = np.zeros((batches, depth_o, (output_size * output_size)), dtype=self.dataType)
        st1 = time.time()
        logger.debug("matmul begin..")
        #不广播，提高处理效率
        for batch in range(batches):
            # 1.conv.shape(32, 32, 784) = {32, [(32, 25)*(25, 784)+(32, 1)]}  
            # 2.conv.shape(32, 64, 196) = {32, [(64, 800)*(800, 196)+(64,1)]}
            # -1.conv.shape(32, 32, 196) = {32, [(32, 1600)*(1600, 196)+0]}
            # -2.conv.shape(32, 1, 784) = {32, [(1, 800)*(800, 784)+0]}
            conv[batch] = Tools.matmul(w_row, x_col[batch]) + b

        logger.debug("matmul end.. %f s" % (time.time() - st1))
        # 1.conv.shape(32, 32, 784)->conv_return.shape(32, 32, 28, 28)
        # 2.conv.shape(32, 64, 196)->conv_return.shape(32, 64, 14, 14)
        # -1.conv.shape(32, 32, 196)->conv_return.shape(32, 32, 14, 14)
        # -2.conv.shape(32, 1, 784)->conv_return.shape(32, 1, 28, 28)
        conv_return = conv.reshape(batches, depth_o, output_size, output_size)
        return conv_return

    # vectorize4convdw_batches:用于反向传播计算dw的向量化
    # ------------------------------------
    # 入参
    #    x : padding后的实例 batches * channel * conv_i_size * conv_i_size
    #    fileter_size :
    #    conv_o_size:
    #    strides:
    # 返回
    #    x_col: batches *channel* (filter_size * filter_size) * ( conv_o_size * conv_o_size)
    #@numba.jit
    def vectorize4convdw_batches(self, x, filter_size, conv_o_size, strides):
        batches = x.shape[0]
        channels = x.shape[1]
        x_per_filter = filter_size * filter_size
        x_col = np.zeros((batches, channels, x_per_filter, conv_o_size * conv_o_size), dtype=self.dataType)
        for j in range(x_col.shape[3]):
            b = int(j / conv_o_size) * strides
            c = (j % conv_o_size) * strides
            x_col[:, :, :, j] = x[:, :, b:b + filter_size, c:c + filter_size].reshape(batches, channels, x_per_filter)

        return x_col

    # cross-correlation向量化优化
    # x_col = (depth_i * filter_size * filter_size) * (conv_o_size * conv_o_size)
    # w: depth_o * （ depth_i/channel * conv_i_size * conv_o_size） =  2*3*3*3
    # reshape 为 w_row =  depth_o * (depth_i/channel * (conv_i_size * conv_o_size)) = 2 * 27
    # conv_t= matmul(w_row,x_col)
    # 得到 conv_t = depth_o * (conv_o_size * conv_size) = 2 * (3*3) =2*9
    #  再 conv = conv_t.reshape ( depth_o * conv_o_size * conv_size) = (2*3*3)
    # ------------------------------------
    # 入参
    #    x : padding后的实例 batches * channel * conv_i_size * conv_i_size
    #    fileter_size :
    #    conv_o_size:
    #    strides:
    # 返回
    #    x_col: batches *(channel* filter_size * filter_size) * ( conv_o_size * conv_o_size)
    #@numba.jit
    def vectorize4conv_batches(self, x, filter_size, conv_o_size, strides):
        batches = x.shape[0]
        channels = x.shape[1]
        x_per_filter = filter_size * filter_size
        shape_t = channels * x_per_filter
        x_col = np.zeros((batches, channels * x_per_filter, conv_o_size * conv_o_size), dtype=self.dataType)
        for j in range(x_col.shape[2]):
            b = int(j / conv_o_size) * strides
            c = (j % conv_o_size) * strides
            x_col[:, :, j] = x[:, :, b:b + filter_size, c:c + filter_size].reshape(batches, shape_t)

        return x_col

    # bp4conv: conv反向传播梯度计算
    # 入参:
    #    d_o :卷积输出误差 batches * depth_o * output_size * output_size   ，规格同 conv的输出
    #    w: depth_o * depth_i * filter_size * filter_size
    #    input: 原卷积层输入 batch * depth_i * input_size * input_size
    #    strides:
    # 返参:
    #    d_i :卷积输入误差 batch * depth_i * input_size * input_size,  其中 depth_i为输入节点矩阵深度
    #    dw : w梯度，规格同w
    #    db : b 梯度 规格同b, depth_O * 1 数组
    #    vec_idx_key:
    # 说明: 1.误差反向传递和db
    #      将w翻转180度作为卷积核，
    #      在depth_o上，对每一层误差矩阵14*14，以该层depth_i个翻转后的w 5*5,做cross-re得到 depth_i个误差矩阵14*14
    #      所有depth_o做完，得到depth_o组，每组depth_i个误差矩阵
    #           batch * depth_o * depth_i * input_size * input_size
    #      d_i:每组同样位置的depth_o个误差矩阵相加，得到depth_i个误差矩阵d_i ,规格同a
    #          优化, 多维数组w_rtLR， 在dept_o和dept_i上做转置，作为卷积和与d_o组协相关
    #      db: 每个d_o上的误差矩阵相加
    #     2. dw
    #       以d_o作为卷积核，对原卷积层输入input做cross-correlation得到 dw
    #       do的每一层depth_o，作为卷积核 14*14，
    #                       与原卷积的输入input的每一个depth_i输入层14*14和做cross-re 得到,depth_i个结果矩阵5*5
    #               合计depth_o * depth_i * f_size * f_size
    #                       只要p/s =2 即可使结果矩阵和w同样规格，如 p=2,s=1
    #               每个结果矩阵作为该depth_o上，该输入层w对应的dw。
    def bp4conv(self, d_o, w, input, strides, vec_idx_key):
        st = time.time()
        logger.debug("bp4conv begin..")
        # -1.input.shape(32, 32, 14, 14) 
        # -2.input.shape(32, 1, 28, 28)
        input_size = input.shape[2]
        # -1.w.shape(64, 32, 5, 5) 
        # -2.w.shape(32, 1, 5, 5)
        f_size = w.shape[2]

        # w翻转180度,先上下翻转，再左右翻转，然后前两维互换实现高维转置
        # -1.(64, 32, 5, 5) 
        # -2.(32, 1, 5, 5)
        w_rtUD = w[:, :, ::-1]  
        w_rtLR = w_rtUD[:, :, :, ::-1]  
        # -1.w_rt.shape(32, 64, 5, 5)  w_rtLR(64, 32, 5, 5)
        # -2.w_rt.shape(1, 32, 5, 5)  w_rtLR(32, 1, 5, 5)
        w_rt = w_rtLR.transpose(1, 0, 2, 3)  

        # 误差项传递
        # -1.d_o.shape(32, 64, 14, 14) w_rt.shape(32, 64, 5, 5) d_i.shape(32, 32, 14, 14) input_size=14
        # -2.d_o.shape(32, 32, 28, 28) w_rt.shape(1, 32, 5, 5) d_i.shape(32, 1, 28, 28) input_size=28
        d_i = self.conv_efficient(d_o, w_rt, 0, input_size, vec_idx_key, 1)
        logger.debug("d_i ready..")

        # 每个d_o上的误差矩阵相加
        # -1.d_o.shape(32, 64, 14, 14) -> db.shape(64, 1)
        # -2.d_o.shape(32, 32, 28, 28) -> db.shape(32, 1)
        db = np.sum(np.sum(np.sum(d_o, axis=-1), axis=-1), axis=0).reshape(-1, 1)
        logger.debug("db ready.. %f s" % (time.time() - st))
        # -1.input.shape(32, 32, 14, 14),d_o.shape(32, 64, 14, 14),f_size=5 dw.shape(64, 32, 5, 5),x_col(32, 32, 196, 25)
        # -2.input.shape(32, 1, 28, 28),d_o.shape(32, 32, 28, 28),f_size=5 dw.shape(32, 1, 5, 5),x_col(32, 1, 784, 25)
        dw, x_col = self.conv4dw(input, d_o, f_size, 0, 1, False)
        logger.debug("bp4conv end.. %f s" % (time.time() - st))

        return d_i, dw, db

    # 梯度检查todo
    def init_test():
        pass

# 池化处理类
class MaxPoolLayer(object):
    def __init__(self, LName, miniBatchesSize, f_size,
                 strides, needReshape, dataType):
        # 初始化超参数
        self.name = LName
        self.miniBatchesSize = miniBatchesSize
        self.f_size = f_size
        self.strides = strides
        self.needReshape = needReshape  # 输出到全连接层是否需要reshape
        self.dataType = dataType
        self.out = []
        self.shapeOfOriOut = ()  # 保留原始输出的shape，用于反向传播
        self.poolIdx = []
        self.deltaPrev = []  
        self.deltaOri = []  


    # 预测时前向传播
    def inference(self, input):
        self.out = self.fp(input)
        return self.out

    # 池化层前向传播
    def fp(self, input):
        # 最大池化计算
        pooling, self.poolIdx = self.pool(input, self.f_size, self.strides, 'MAX')
        self.shapeOfOriOut = pooling.shape
        # 最后一个池化层要链接全连接层，所以输出需要进行reshape
        if True == self.needReshape:
            self.out = pooling.reshape(pooling.shape[0], -1)
        else:
            self.out = pooling
        return self.out

    # 池化层反向传播,有误差无权参，先对输出误差求导再反向传播至上一层
    def bp(self, input, delta, lrt):

        if True == self.needReshape:
            self.deltaOri = delta.reshape(self.shapeOfOriOut)
        else:
            self.deltaOri = delta

        self.deltaPrev = self.bp4pool(self.deltaOri, self.poolIdx, self.f_size, self.strides, 'MAX')

        return self.deltaPrev

    # pooling, 优化后的的降采样计算
    # 入参:
    #     x规格: batch * depth_i * row * col,  其中 depth_i为输入节点矩阵深度，
    #     fileter_size: 过滤器尺寸
    #     strides: 缺省为1
    #     type: 降采样类型，MAX/MEAN  ,缺省为MAX
    # 返回: 卷积层加权输出(co-relation)
    #       pooling : batch * depth_i * output_size * output_size
    #       pooling_idx : batch * depth_i * y_per_o_layer * x_per_filter
    #                其中 y_per_o_layer =  output_size * output_size
    #                    x_per_filter = pool_f_size * pool_f_size
    #                MAX value在当前input_block 对应位置为1,其它为0
    # 优化：先把x 组织成 batch * depth_i * (output_size * output_size) * (filter_size * filter_size)
    #      然后利用矩阵运算，对最后一维做max得到batch * depth_i * (output_size * output_size)
    #      再reshape 为 batch * depth_i * output_size * output_size
    def pool(self, x, filter_size, strides=2, type='MAX'):
        logger.debug("pooling begin..")
        batches = x.shape[0]
        depth_i = x.shape[1]
        input_size = x.shape[2]
        x_per_filter = filter_size * filter_size
        # 1.output_size = (28-2)/2 + 1
        # 2.output_size = (14-2)/2 + 1
        output_size = int((input_size - filter_size) / strides) + 1
        # 1.y_per_o_layer=14*14=196，输出矩阵,每一层元素个数
        # 2.y_per_o_layer=7*7=49，输出矩阵,每一层元素个数
        y_per_o_layer = output_size * output_size  
        # 1.(32, 32, 196, 4)
        # 2.(32, 64, 49, 4)
        x_vec = np.zeros((batches, depth_i, y_per_o_layer, x_per_filter), dtype=self.dataType)

        # pooling处理
        for j in range(y_per_o_layer):
            b = int(j / output_size) * strides
            c = (j % output_size) * strides
            # 1.从x.shape(32, 32, 28, 28)中每次从后两维中提取四个值,即将(32, 32, 2, 2)reshape成x.shape(32, 32, 4)。放入x_vec[::].shape=(32, 32, {j<=196隐藏}, 4)对应位置中
            # 2.从x.shape(32, 64, 14, 14)中每次从后两维中提取四个值,即将(32, 64, 2, 2),reshape成x.shape(32, 64, 4)。放入x_vec[::].shape=(32, 64, {j<=49隐藏}, 4)对应位置中
            x_vec[:, :, j, 0:x_per_filter] = x[:, :, b:b + strides, c:c + strides].reshape(batches, depth_i, x_per_filter)
        # 1.选取最后一维中的最大值，即在x_vec(?,?,196,4)里，196个样本中包含的4个值中的最大值，pooling.shape(32, 32, 14, 14)
        # 2.选取最后一维中的最大值，即在x_vec(?,?,49,4)里，196个样本中包含的4个值中的最大值，pooling.shape(32, 64, 7, 7)
        pooling = np.max(x_vec, axis=3).reshape(batches, depth_i, output_size, output_size)
        # 1.pooling_idx.shape(32, 32, 196, 4)，仅在池化时取max的位置记录1，用于反向传播，可参考maxpooling反向传播原理
        # 2.pooling_idx.shape(32, 64, 49, 4)
        pooling_idx = np.eye(x_vec.shape[3], dtype=int)[x_vec.argmax(3)]
        logger.debug("pooling end..")

        return pooling, pooling_idx

    # bp4pool: 反向传播上采样梯度
    # 入参：
    #      dpool: 池化层输出的误差项, N * 3136 =N*(64*7*7)=  batches * (depth_i * pool_o_size * pool_o_size)
    #                  reshape为batches * depth_i * pool_o_size * pool_o_size
    #      pool_idx : MAX pool时保留的max value index , batches * depth_i * y_o * x_per_filter
    #      pool_f_size: pool  filter尺寸
    #      pool_stides:
    #      type : MAX ,MEAN, 缺省为MAX
    # 返参:
    #      dpool_i: 传递到上一层的误差项  , batches * depth_i * pool_i_size * pool_i_size
    #             当 strides =2 ,filter = 2 时， pool的pool_i_size 是pool_o_size 的2倍
    def bp4pool(self, dpool, pool_idx, pool_f_size, pool_strides, type='MAX'):
        logger.debug("bp4pool begin..")
        batches = dpool.shape[0]
        depth_i = pool_idx.shape[1]
        y_per_o = pool_idx.shape[2]
        # x_per_filter=2*2
        x_per_filter = pool_f_size * pool_f_size
        # -1.pool_o_size=7 
        # -2.pool_o_size=14
        pool_o_size = int(np.sqrt(y_per_o))
        # 反推输入的
        # -1.input_size=14 
        # -2.input_size=28
        input_size = (pool_o_size - 1) * pool_strides + pool_f_size
        # reshape误差矩阵
        # -1.dpool_reshape.shape(32, 64, 49) 
        # -2.dpool_reshape.shape(32, 32, 196)
        dpool_reshape = dpool.reshape(batches, depth_i, y_per_o)
        # -1.(32, 64, 14, 14) 
        # -2.(32, 32, 28, 28)
        dpool_i_tmp = np.zeros((batches, depth_i, input_size, input_size), dtype=self.dataType)
        pool_idx_reshape = np.zeros(dpool_i_tmp.shape, dtype=self.dataType)
        for j in range(y_per_o):
            b = int(j / pool_o_size) * pool_strides
            c = (j % pool_o_size) * pool_strides
            # pool_idx_reshape规格同池化层输入，每个block的max value位置值为1，其余位置值为0(池化层反向传播原理)
            # 使用前向传播时保存的maxpooling索引矩阵pool_idx，将pool_idx池化取值元素位置信息反向传播到pool_idx_reshape对应位置
            # -1.将pool_idx的j位置对应信息提取到pool_idx_reshape.shape(32, 64, 14, 14)。 pool_idx_reshape[::].shape=(32, 64, 2, 2), pool_idx[::].shape(32, 64, {j<=49隐藏}, 4).reshape(32, 64, 2, 2) 
            # -2.将pool_idx的j位置对应信息提取到pool_idx_reshape.shape(32, 32, 28, 28)。 pool_idx_reshape[::].shape=(32, 32, 2, 2), pool_idx[::].shape(32, 32, {j<=196隐藏}, 4).reshape(32, 32, 2, 2)
            pool_idx_reshape[:, :, b:b + pool_f_size, c:c + pool_f_size] = pool_idx[:, :, j, 0:x_per_filter].reshape( batches, depth_i, pool_f_size, pool_f_size)
            # dpool_i_tmp规格规格同池化层输入，每个block的值均以对应dpool元素填充
            for row in range(pool_f_size):  # 只需要循环 x_per-filter 次得到 填充扩展后的delta
                for col in range(pool_f_size):
                    # -1.dpool_i_tmp[].shape=(32, 64, {<=14, <=14隐藏}) , dpool_reshape[].shape=(32, 64, {<=49隐藏})
                    # -2.dpool_i_tmp[].shape=(32, 64, {<=28, <=28隐藏}) , dpool_reshape[].shape=(32, 64, {<=196隐藏})
                    dpool_i_tmp[:, :, b + row, c + col] = dpool_reshape[:, :, j]
        # 相乘后，max value位置delta向上传播，其余位置为delta为0
        # -1.(32, 64, 14, 14) = (32, 64, 14, 14) * (32, 64, 14, 14)
        # -2.(32, 32, 28, 28) = (32, 32, 28, 28) * (32, 32, 28, 28)
        dpool_i = dpool_i_tmp * pool_idx_reshape
        logger.debug("bp4pool end..")
        return dpool_i

