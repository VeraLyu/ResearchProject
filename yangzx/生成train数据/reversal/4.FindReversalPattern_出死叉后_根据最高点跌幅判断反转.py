import tushare as ts
import datetime as dt
import time
import typing
import sys
import os

import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np

sys.path.append('..\..')
from Helper import DrawHelper
from Helper import ZipHelper

""""
# 寻找反转模式
# 目标：出死叉后，找到最高点，判断最高点后chgDayCount日最大跌幅是否达到预期，达到预期则选出来
# 1. ma10 连续在 ma20 上 n 天后，首次出现交叉，获取这样的区间数据（不包含交叉当天）
# 2. 在交叉日区间中，找到最高点对应的日期
# 3. 从最高点向未来取p个交易日，判断从最高位起，跌幅是否达到x%，若达到则为所求
# 4. 从最高点向前取 m 个交易日
# 5. 记录股票代码、日期区间、价格区间，输出区间数据的图像

# 后续改进：
目标：出现死叉后，找到死叉出现之后的n日最大跌幅是否达到预期，达到预期则选出来
# 1.在交叉日期后，向后取 m 个交易日
# 2.若连续 m 天 ma10 < ma20，即为所求
"""

# 获取所有股票列表
def GetAllStockList():
    pro = ts.pro_api('6d9ac99d25b0157dcbb1ee3d35ef1250e5295ff80bb59741e1a56b35')
    df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol')
    allstocklistdic = dict()
    allstocklistdic1 = dict()
    for col in df.values:
        allstocklistdic[col[0]] = col[1]
        allstocklistdic1[col[1]] = col[0]
    return allstocklistdic

# 获取股票池，结构{symbol:bool}
def GetStockPool(indexCode='399300.SZ'):
    pro = ts.pro_api('1c5440f527d1e513c75d10518ef9fd05a34a33ec4146b353bc7ce5bf')
    # 月初月末各公布一次成分股
    startdate = (dt.datetime.today() - dt.timedelta(31)).strftime("%Y%m%d")
    df = pro.index_weight(index_code=indexCode, start_date=startdate, end_date=time.strftime("%Y%m%d"))
    stockPoolDic = dict()
    for col in df.values:
        stockPoolDic[col[1]] = True
    return list(stockPoolDic.keys())

# 取股票均线数据
# maPara: 想要获取的均线窗口值
def GetStockMA(stockCode, period=1401, maPara=[10, 20], calDay=100, type="D", benchmark="close"):
    startdate = (dt.datetime.today() - dt.timedelta(period)).strftime("%Y%m%d")
    df = ts.pro_bar(ts_code=stockCode, adj='qfq', start_date=startdate, end_date=time.strftime("%Y%m%d"), ma=maPara)
    
    # 样本点小于40个不计算
    if df is None or df.values is None or len(df.values) < 40:
        print("数据缺失：",stockCode)
        return False
    
    # 遍历重构正向时序上的数据
    OrderDic = typing.OrderedDict()
    for i in range(len(df.values)-1,-1,-1):
        # 剔除前n天均线为Nan值的数据
        if i > len(df.values) - maPara[len(maPara)-1]:
            continue
        value = df.values[i]
        OrderDic[value[1]] = {'tdate':value[1], 'open':value[2], 'high':value[3], 'low':value[4], 'close':value[5], \
            'lclose':value[6], 'change':value[7], 'chg':value[8], 'vol':value[9], 'amount':value[10]*1000, \
            'ma10':value[11], 'ma_v_10':value[12], 'ma20':value[13], 'ma_v_20':value[14]}
    #print(OrderDic[next(reversed(OrderDic))])
    return OrderDic

# 判断反转模式
def FindReversal(stockMA, reversalDay=8, chgDayCount=5, pchg=0.15):
    # 连续趋势计数
    compareCount = 0
    # 全局循环计数器
    globleCount = 0
    # 日期列表
    seriesTdateList = list()
    # 交易数据列表
    seriesList = list()
    orderDic = typing.OrderedDict()
    # 字典转列表
    dicToList = list()
    # 将整个有序字典转换成数组，方便后续根据下标取值
    dicToList = list(stockMA.values())
    for stockMAKey, stockMAValue in stockMA.items():
        # 从首次上涨趋势开始时，记录本次趋势内序列
        if float(stockMAValue["ma10"]) >= float(stockMAValue["ma20"]):
            seriesTdateList.append(stockMAValue["tdate"])
            seriesList.append([stockMAValue["open"],stockMAValue["high"],stockMAValue["low"],stockMAValue["close"]])
            compareCount += 1
        # 遇到死叉本轮趋势终止，若本轮上涨趋势满足趋势时长，在orderDic添加本轮趋势序列（默认不记录交叉当天信息，若记录交叉当天信息，在此处添加即可）
        if float(stockMAValue["ma10"]) < float(stockMAValue["ma20"]):
            if compareCount > reversalDay:
                # 寻找区间最高点K线对应收盘价的日期，在序列中的位置
                featureList = np.array(seriesList)[:,3].tolist()
                # 反转序列，以便找到featureList区间内最大值的位置下标
                featureList.reverse()
                maxIndex = featureList.index(max(featureList))
                theIndex = len(featureList)-maxIndex-1
                
                # 判断最高点向未来chgDayCount天是否越界
                if (globleCount - (len(featureList) - theIndex) + chgDayCount) <= len(dicToList) - 1:
                    # 从最高点向未来取chgDayCount个交易日收盘价，计入chgList，计算跌幅
                    chgList = list()
                    for count in range(chgDayCount):
                        # 从最高点向未来chgDayCount天的价格序列=(金叉日位置-(区间总长-最高点位置)+i)
                        chgList.append(dicToList[globleCount - (len(featureList) - theIndex) + count]['close'])
                    # 如果跌幅达标 只存储最高点及历史部分的序列
                    if ((chgList[0] - min(chgList)) / chgList[0]) >= pchg:
                        orderDic[stockMAValue["tdate"]] = {"tdateList":seriesTdateList[:theIndex+1], "seriesList":seriesList[:theIndex+1]}
            seriesTdateList = list()
            seriesList = list()
            compareCount = 0
        globleCount += 1
    return orderDic

# 画出每个符合要求的图
def SavePicture(code, dataDic, reversalDay, reversalDayOffset, dirPath=''):
    if dirPath == '' or not os.path.exists(dirPath):
        dirPath = sys.path[0]
        print("缺少保存路径，默认保存至当前文件夹下")
    for item in dataDic.values():
        if len(item["tdateList"]) > reversalDay - reversalDayOffset:
            tdateList = item["tdateList"][-reversalDay+reversalDayOffset:]
            priceList = item["seriesList"][-reversalDay+reversalDayOffset:]
            path = dirPath + "\\" + code + "_" + item["tdateList"][0] + ".png"
            DrawHelper.DrawDataK(tdateList, priceList, path)
        else:
            print(code,":数据量不足","，不生成图片")

# 主函数
if __name__ == '__main__':
    # 生成策略结果数据
    tagDic = dict()
    # 循环计数器
    dataCount = 0
    # 股票样本大小限制
    sampleCount = 50
    # 提取趋势区间序列长度
    reversalDay = 21
    # 后续涨跌幅计算区间
    chgCount = 8
    # 目标波动幅度
    pchg = 0.15
    # 提取趋势区间长度偏移量，剔除最低点右侧数据后，序列提取长度应相对缩短
    reversalDayOffset = 5
    # 压缩文件源路径
    dirPath = "..\\..\\..\\Communal\\ReversalNegative"
    # 压缩文件生成路径
    imgOutFullName = "..\\..\\..\\Communal\\ReversalNegative{0}.zip".format(time.strftime("%Y%m%d"))

    # 获取股票池 上证50:000016.SH 沪深300:399300.SZ 上证180：000010.SH
    stockPoolList = GetStockPool('000016.SH')
    # 读取全市场股票列表
    for code in GetAllStockList().keys():
        if len(stockPoolList) > 0 and code not in stockPoolList:
            continue
        # 获取均线数据
        stockMADic = GetStockMA(code)
        
        if dataCount > sampleCount:
            break
        elif stockMADic == False:
            continue
        else:
            # 找到反转模式区间
            reversalDic = FindReversal(stockMADic, reversalDay, chgCount, pchg)
            # 生成反转模式区间的图片
            SavePicture(code, reversalDic, reversalDay, reversalDayOffset, dirPath)
            dataCount += 1
            if dataCount == 500:
                time.sleep(60)
    
    # 压缩生成图片的文件夹
    ZipHelper.ZipDir(dirPath, imgOutFullName)






    print("finish")
    input()

