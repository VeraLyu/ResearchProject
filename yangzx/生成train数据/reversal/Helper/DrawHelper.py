import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np

def DrawDataK1(dates, prices):
    #data = ts.get_k_data('002153', ktype='D', autype='qfq', start='2021-12-17', end='')
    #prices = data[['open', 'high', 'low', 'close']]
    #dates = data['date']
    candleData = np.column_stack([list(range(len(dates))), prices])
    # 图片的长宽比例
    fig = plt.figure(figsize=(10, 6))
    # 图像的左，底，宽，高 位置（left, bottom, width, height）
    ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
    # 是否带边框
    plt.axis('off')
    mpf.candlestick_ohlc(ax, candleData, width=0.5, colorup='r', colordown='b')
    plt.savefig('D:\\导出的图片.png')
    #plt.show()

def DrawDataK(dates, prices):
    #prices = data[['open', 'high', 'low', 'close']]
    #dates = data['date']
    candleData = np.column_stack([list(range(len(dates))), prices])
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
    plt.axis('off')
    mpf.candlestick_ohlc(ax, candleData, width=0.5, colorup='r', colordown='b')
    plt.savefig('D:\\导出的图片.png')

# 主函数
if __name__ == '__main__':
    data = ts.get_k_data('002153', ktype='D', autype='qfq', start='2021-12-17', end='')
    print(data)
    prices = data[['open', 'high', 'low', 'close']]
    dates = data['date']
    candleData = np.column_stack([list(range(len(dates.values.tolist()))), prices.values.tolist()])
    # 图片的长宽比例
    fig = plt.figure(figsize=(10, 6))
    # 图像的左，底，宽，高 位置（left, bottom, width, height）
    ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
    # 是否带边框
    plt.axis('off')
    mpf.candlestick_ohlc(ax, candleData, width=0.5, colorup='r', colordown='b')
    #plt.savefig('D:\\导出的图片.png')
    plt.show()
    input()
    