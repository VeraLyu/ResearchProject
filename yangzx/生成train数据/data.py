from typing import OrderedDict
import tushare as ts
from DataToImage import DataToImage


# 获取tushare的token
token = '1c5440f527d1e513c75d10518ef9fd05a34a33ec4146b353bc7ce5bf'
ts.set_token(token)

pro = ts.pro_api()
# 获取000001.SZ 中国平安 100天历史交易数据
df = pro.daily(ts_code='000001.SZ', start_date='20220609', end_date='20220713', fields='ts_code,trade_date,high,low')
# print(df)
# 取最高价high和最低价low列表
df_price = df.iloc[:, 2:4]
# print(df_price)

# 取最高价最大值
max = df.iloc[:, 2].max()
# 取最低价最小值
min = df.iloc[:, 3].min()
# print(max, min)

# 将dataframe数据转换成list
data = df.values.tolist()
# print(data)
# 将数据保存为csv文件
# df.to_csv('./csv/data.csv')


# 对价格数据进行归一化处理
# 计算方法：x = (x - min) / (max - min)
def data_norm(df_price, *cols):
    df_x = df_price.copy()
    for col in cols:
        df_x[col + '_n'] = (df_x[col] - min) / (max - min)
    return(df_x)
# 创建函数，标准化数据

df_x = data_norm(df_price,'high','low')
df_norm = round(df_x, 2)
# print(df_norm)
# 将数据保存为csv文件
# df_norm.to_csv('./csv/data_norm.csv')

# print(df_norm.values)
#input()

DataToImage(df_norm)





