import tushare as ts
import datetime as dt
import time


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


# 主函数
if __name__ == '__main__':
    # 生成策略结果数据
    tagDic = dict()
    # 循环计数器
    dataCount = 0
    # 股票样本数
    sampleCount = 50
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


