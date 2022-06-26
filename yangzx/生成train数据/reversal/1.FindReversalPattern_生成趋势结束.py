import tushare as ts
import datetime as dt
import time
import typing

import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np
from Helper import DrawHelper


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

# 寻找反转趋势
# 1. ma10 连续在 ma20下 n 天后，首次出现交叉，获取这样的数据
# 2. 在交叉日中，找到最低点对应的日期，向后取 m 个交易日
# 3. 如果最低点后的 m 个交易日，涨幅达到x or 连续y天 ma10 > ma20，即为所求
# 4. 记录这样的股票代码和日期区间，输出图像

# 取股票均线数据
# maPara: 想要获取的均线窗口值
def GetStockMA(stockCode, period=1401, maPara=[10, 20], calDay=100, type="D", benchmark="close"):
    startdate = (dt.datetime.today() - dt.timedelta(period)).strftime("%Y%m%d")
    #df = ts.pro_bar(ts_code=stockCode, adj='qfq', freq=type, start_date=startdate, end_date=time.strftime("%Y%m%d"))
    df = ts.pro_bar(ts_code=stockCode, start_date=startdate, end_date=time.strftime("%Y%m%d"), ma=maPara)
    
    # 样本点小于40个不计算
    if df is None or df.values is None or len(df.values) < 40:
        print("数据缺失：",stockCode)
        return 0
    
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

def DrawDataK(dates, prices):
    #prices = data[['open', 'high', 'low', 'close']]
    #dates = data['date']
    candleData = np.column_stack([list(range(len(dates))), prices])
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
    plt.axis('off')
    mpf.candlestick_ohlc(ax, candleData, width=0.5, colorup='r', colordown='b')
    plt.savefig('D:\\导出的图片.png')
    #plt.show()

# 判断反转模式
def FindReversal(stockMA, reversalDay=8):
    # 连续趋势计数
    compareCount = 0
    # 日期列表
    seriesTdateList = list()
    # 详情列表
    seriesList = list()
    OrderDic = typing.OrderedDict()
    for stockMAKey, stockMAValue in stockMA.items():
        # 从下跌趋势开始时，记录本次趋势内数据
        if float(stockMAValue["ma10"]) <= float(stockMAValue["ma20"]):
            seriesTdateList.append(stockMAValue["tdate"])
            seriesList.append([stockMAValue["open"],stockMAValue["high"],stockMAValue["low"],stockMAValue["close"]])
            compareCount += 1
        # 遇到死叉，如果本次下跌趋势满足，就进行记录,若记录当天信息，在此处添加即可
        if float(stockMAValue["ma10"]) > float(stockMAValue["ma20"]):
            if compareCount > reversalDay:
                OrderDic[stockMAValue["tdate"]] = {"tdateList":seriesTdateList, "seriesList":seriesList}
                seriesTdateList = list()
                seriesList = list()
            compareCount = 0
    listIndex = list(OrderDic.keys())
    # 返回用于作图的数据
    DrawHelper.DrawDataK(OrderDic[listIndex[0]]["tdateList"][-reversalDay:], OrderDic[listIndex[0]]["seriesList"][-reversalDay:])

# 主函数
if __name__ == '__main__':
    
    # 生成策略结果数据
    tagDic = dict()
    # 循环计数器
    dataCount = 0
    # 股票样本数
    sampleCount = 50
    stockMADic = GetStockMA('000001.SZ')
    FindReversal(stockMADic, 16)



    # 获取股票池 上证50:000016.SH 沪深300:399300.SZ 上证180：000010.SH
    stockPoolList = GetStockPool('000016.SH')
    # 读取全市场股票列表
    for code in GetAllStockList().keys():
        if len(stockPoolList) > 0 and code not in stockPoolList:
            continue
        # 取fullSequenceCount条行情数据，取其中calSequenceCount条进行计算，监督窗口大小为windowCount
        #tag = CalTagList.CalNormal(code,fullSequenceCount,calSequenceCount,windowCount)
        tag = 1
        if dataCount > sampleCount:
            break
        elif tag == False:
            continue
        else:
            tagDic[code] = tag
            dataCount += 1
            if dataCount == 500:
                time.sleep(60)


