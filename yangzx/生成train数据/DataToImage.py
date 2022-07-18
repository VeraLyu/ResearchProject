# DataToImage()函数封装
import matplotlib.pyplot as plt

def DataToImage(df_norm):
    allDataList = df_norm.values     # 归一化后的数据df_norm
    fiveDayCount = 0  # 天数计数
    allCount = 0  # 每5天，allCount+1
    allList = list()
    fiveDayList = list()
    for dataListItem in allDataList:
        fiveDayCount += 1
        fiveDayList.append([dataListItem[2], dataListItem[3]])  # 取归一化后的最高价和最低价
        if fiveDayCount % 5 == 0:  # 每5天，为一个list列表
            allList.append(fiveDayList)
            fiveDayList = list()  # 每5天，清空fiveDayList列表
        if allCount > 5:
            break

    # dicc = OrderedDict()

    tDic = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    fiveDic = dict()
    resultList = list()
    for listItem in allList:
        numCount = 0
        for item in listItem:
            little = int(item[1] * 100)
            big = int(item[0] * 100)
            drawList = list()
            for num in range(little, big + 1):
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
