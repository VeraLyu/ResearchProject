from operator import index
import matplotlib.pyplot as plt
import collections
from typing import OrderedDict
import tushare as ts

# TPO标志符号sign字典
signDic = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
# 每个TPO sign对应的颜色
colorDic = {
    "A": "#E8E8E8",
    "B": "#CFCFCF",
    "C": "#B5B5B5",
    "D": "#9C9C9C",
    "E": "#828282"
}

"""
# 画TPO市场轮廓图
# baseDataList：两列tpo基础数据，全局归一化后的 每个交易日价格最大最小值
# extendData：后续扩展数据列，包含一些扩展特征
"""
def DrawTPOImage(baseDataList, extendData):
    # 归一化后的价格数据
    allDataList = baseDataList
    # 每组钟形图区间天数
    unitDayCount = 5
    # 循环计数器
    calDayCount = 0
    # TPO钟形图展示数量
    showCount = 0
    # TPO钟形图序列集合
    allUnitList = list()
    # 单组TPO钟形图序列
    unitTPOList = list()
    for baseDataItem in baseDataList:
        calDayCount += 1
        # 记录区间内的最高价和最低价
        unitTPOList.append([baseDataItem[0], baseDataItem[1]])
        # 存储一个完整的钟形图
        if calDayCount % unitDayCount == 0:
            allUnitList.append(unitTPOList)
            showCount += 1
            unitTPOList = list()
        if showCount >= 5:
            break

    
    # 每组TPO钟形图对应的填充字典
    unitTPODic = OrderedDict()
    # 多组TPO钟形图集合
    resultTPOList = list()
    # 遍历每组 市场轮廓钟形图序列 的集合，将其转换为TPO字典
    for allUnitItem in allUnitList:
        # 当前交易日对应的TPO标志符号
        sign = 0
        # 计算每个交易日区间内要填充图像的序列
        for item in allUnitItem:
            # 计算每个交易日覆盖的范围区间
            little = int(item[1] * 100)
            big = int(item[0] * 100)
            # 最小值和最大值之间的区域indexKey，都要进行市场轮廓TPO填充
            for indexKey in range(little, big + 1):
                # 填充区间范围索引indexKey，每个indexKey索引后跟一个TPO list结构
                if indexKey in unitTPODic:
                    unitTPODic[indexKey].append(signDic[sign])
                else:
                    indexKeyList = list()
                    indexKeyList.append(signDic[sign])
                    unitTPODic[indexKey] = indexKeyList
            sign += 1
        resultTPOList.append(unitTPODic)
        unitTPODic = OrderedDict()

    

    plt.rcParams['font.sans-serif'] = ['FangSong']
    # 绘制一个8*8的画布
    plt.figure(figsize=(8, 8))
    axes = plt.axes()
    # 一个tpo块的高度
    barHeight = 1
    # 每组TPO钟形图计数器
    topGroupCount = 0
    # 一个TPO块的宽度
    barWidth = [1]
    # 遍历多组TPO钟形图集合
    for everyTPODic in resultTPOList:
        for TPOKey, TPOValue in everyTPODic.items():
            # TPO组内交易日计数器
            tpoItemCount = 0
            for sign in TPOValue:
                # TPO块的x,y坐标
                y_axis = [TPOKey]
                x_axis = topGroupCount * 6 + tpoItemCount
                # 每个TPO图像
                axes.barh(y_axis, barWidth, height=barHeight, color=colorDic[sign], align='center', left=x_axis, fill=True, joinstyle='bevel')
                tpoItemCount += 1
        topGroupCount += 1
        break

    # 设置x,y轴标题
    axes.set_xlabel('DateTime', fontsize=20)
    axes.set_ylabel('Price', fontsize=20)

    axes.grid(axis='x')  # 设置仅显示x轴网格线
    plt.axis('off')  # 不显示坐标轴
    # ax.legend()  # 显示图例
    plt.show()
    input()



# 主函数
if __name__ == '__main__':
    # 获取tushare的token
    token = '1c5440f527d1e513c75d10518ef9fd05a34a33ec4146b353bc7ce5bf'
    ts.set_token(token)
    pro = ts.pro_api()
    # 获取000001.SZ 中国平安 100天历史交易数据
    df = pro.daily(ts_code='000001.SZ', start_date='20220609', end_date='20220713', fields='ts_code,trade_date,high,low')

    # 取最高价high和最低价low列表
    df_price = df.iloc[:, 2:4]
    # 取最高价最大值
    max = df.iloc[:, 2].max()
    # 取最低价最小值
    min = df.iloc[:, 3].min()

    # 将dataframe数据转换成list
    data = df.values.tolist()
    # print(data)
    # 将数据保存为csv文件
    # df.to_csv('./csv/data.csv')


    # 对价格数据进行归一化处理
    def data_norm(df_price, *cols):
        df_x = df_price.copy()
        for col in cols:
            df_x[col + '_n'] = (df_x[col] - min) / (max - min)
        return(df_x)

    df_x = data_norm(df_price,'high','low')
    df_norm = round(df_x, 2)
    # 将数据保存为csv文件
    # df_norm.to_csv('./csv/data_norm.csv')
    DrawTPOImage(df_norm.values[:,2:],[])