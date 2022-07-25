# DataToImage()函数封装
import matplotlib.pyplot as plt
import collections
def DataToImage(baseDataList, extendData):
    # 归一化后的价格数据
    allDataList = baseDataList
    # 单位钟形图区间天数
    nuitDayCount = 5
    # 循环计数器
    calDayCount = 0
    # 钟形图展示数量
    showCount = 0
    # 钟形图序列集合
    allNuitList = list()
    # 单个钟形图序列
    unitDayList = list()
    for baseDataItem in baseDataList:
        calDayCount += 1
        # 记录区间内的最高价和最低价
        unitDayList.append([baseDataItem[0], baseDataItem[1]])
        # 存储一个完整的钟形图
        if calDayCount % nuitDayCount == 0:
            allNuitList.append(unitDayList)
            showCount += 1
            unitDayList = list()
        if showCount >= 3:
            break

    # 轮廓标记
    tDic = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    unitDic = collections.OrderedDict()
    resultList = list()
    # 遍历钟形图序列集合
    for allNuitItem in allNuitList:
        numCount = 0
        for item in allNuitItem:
            # 最小值
            little = int(item[1] * 100)
            big = int(item[0] * 100)
            drawList = list()
            for num in range(little, big + 1):
                if num in unitDic:
                    unitDic[num].append(tDic[numCount])
                else:
                    drawList = list()
                    drawList.append(tDic[numCount])
                    unitDic[num] = drawList
            numCount += 1
        resultList.append(unitDic)
        unitDic = collections.OrderedDict()

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

    fiveLiftCount = 0
    for everyKDic in resultList:
        for everyKKey, everyValue in everyKDic.items():
            leftCount = 0
            for point in everyValue:
                fname = [int(everyKKey)]
                # 第一个钟形图第1条长度
                fspend = [1]
                ax.barh(fname, fspend, height=1, color=color_dic[point], align='center',
                        left=fiveLiftCount * 6 + leftCount, fill=True, joinstyle='bevel')
                leftCount += 1
        fiveLiftCount += 1

    ax.set_xlabel('x轴', fontsize=20)  # 设置x轴标题
    ax.set_ylabel('y轴', fontsize=20)  # 设置y轴标题

    ax.grid(axis='x')  # 设置仅显示x轴网格线
    plt.axis('off')  # 不显示坐标轴
    # ax.legend()  # 显示图例
    plt.show()
    input()
