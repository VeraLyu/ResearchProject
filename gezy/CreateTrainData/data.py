from typing import OrderedDict
import tushare as ts
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

# 获取tushare的token
token = '1c5440f527d1e513c75d10518ef9fd05a34a33ec4146b353bc7ce5bf'
ts.set_token(token)

pro = ts.pro_api()
# 获取000001.SZ 中国平安 100天历史交易数据
df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20181126', fields='ts_code,trade_date,high,low')

# 取最高价high和最低价low列表
df_price = df.iloc[:, 2:4]
# print(df_price)

# 取最高价最大值
max = df.iloc[:, 2].max()
# 取最低价最小值
min = df.iloc[:, 3].min()
print(max, min)

# 将dataframe数据转换成list
data = df.values.tolist()
# print(data)
# 将数据保存为csv文件
#df.to_csv('./csv/data.csv')


# 对价格数据进行归一化处理
# 计算方法：x = (x - min) / (max - min)
def data_norm(df_price,*cols):
    df_x = df_price.copy()
    for col in cols:
        df_x[col + '_n'] = (df_x[col] - min) / (max - min)
    return(df_x)
# 创建函数，标准化数据

df_x = data_norm(df_price,'high','low')
df_norm = round(df_x, 2)
print(df_norm)
# 将数据保存为csv文件
#df_norm.to_csv('./csv/data_norm.csv')

print(df_norm.values)
#input()
allDataList = df_norm.values
fiveDayCount = 0
allCount = 0
allList = list()
fiveDayList = list()
for dataListItem in allDataList:
    fiveDayCount += 1
    fiveDayList.append([dataListItem[2],dataListItem[3]])
    if fiveDayCount % 5 == 0:
        allList.append(fiveDayList)
        fiveDayList = list()
    if allCount > 5:
        break
print(allList[0])
print(allList[1])
print(allList[2])
print(allList[3])
print(allList[4])

#dicc = OrderedDict()

tDic = {0:'A',1:'B',2:'C',3:'D',4:'E',}
fiveDic = OrderedDict()
resultList = list()
for listItem in allList:
    numCount = 0
    for item in listItem:
        little = int(item[1] * 100)
        big = int(item[0] * 100)
        drawList = list()
        for num in range(little,big+1):
            if num in fiveDic:
                fiveDic[num].append(tDic[numCount])
            else:
                drawList = list()
                drawList.append(tDic[numCount])
                fiveDic[num] = drawList
        numCount += 1
    resultList.append(fiveDic)
    fiveDic = dict()


color_dic = {
    "A": "#E8E8E8",
    "B": "#CFCFCF",
    "C": "#B5B5B5",
    "D": "#9C9C9C",
    "E": "#828282"
}
plt.rcParams['font.sans-serif'] = ['FangSong']

plt.figure(figsize=(8, 8))  # 绘制一个8*8的画布
ax = plt.axes()
bar_width = 0.05  # 条形宽度


for everyKDic in resultList[0:5]:
    for everyKKey, everyValue in  everyKDic.items():
        leftCount = 0
        for point in everyValue:
            fname = [int(everyKKey)]
            # 第一个钟形图第1条长度
            fspend = [1]
            ax.barh(fname, fspend, height=1, color='#E8E8E8',  align='center', left=leftCount, fill=True, joinstyle='bevel')
            leftCount += 1





ax.set_xlabel('x轴', fontsize=20)  # 设置x轴标题
ax.set_ylabel('y轴', fontsize=20)  # 设置y轴标题

ax.grid(axis='x')  # 设置仅显示x轴网格线
plt.axis('off')  # 不显示坐标轴
# ax.legend()  # 显示图例
plt.show()
input()


