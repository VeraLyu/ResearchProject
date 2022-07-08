import matplotlib.pyplot as plt
import numpy as np

"""
day1    price_size=5
    high    low
A   3130    3100
B   3120    3090
C   3105    3085
D   3115    3075
E   3105    3075
"""
# 创建一个字典price_dic存储价格和对应tpo单位
A_dic = {
    "3100": 2.6,
    "3105": 2.7,
    "3110": 2.8,
    "3115": 2.9,
    "3120": 3.0,
    "3125": 3.1,
    "3130": 3.2
}
B_dic = {
    "3090": 2.4,
    "3095": 2.5,
    "3100": 2.6,
    "3105": 2.7,
    "3110": 2.8,
    "3115": 2.9,
    "3120": 3.0
}
C_dic = {
    "3085": 2.3,
    "3090": 2.4,
    "3095": 2.5,
    "3100": 2.6,
    "3105": 2.7,
    "3110": 2.8,
    "3115": 2.9
}
D_dic = {
    "3075": 2.1,
    "3080": 2.2,
    "3085": 2.3,
    "3090": 2.4,
    "3095": 2.5,
    "3100": 2.6,
    "3105": 2.7,
    "3110": 2.8,
    "3115": 2.9
}
E_dic = {
    "3075": 2.1,
    "3080": 2.2,
    "3085": 2.3,
    "3090": 2.4,
    "3095": 2.5,
    "3100": 2.6,
    "3105": 2.7
}
price_dic = {
    "A": A_dic,
    "B": B_dic,
    "C": C_dic,
    "D": D_dic,
    "E": E_dic
}
"""
    "2975": 0.1,
    "2980": 0.2,
    "2985": 0.3,
    "2990": 0.4,
    "2995": 0.5,
    "3000": 0.6,
    "3005": 0.7,
    "3010": 0.8,
    "3015": 0.9,
    "3020": 1.0,
    "3025": 1.1,
    "3030": 1.2,
    "3035": 1.3,
    "3040": 1.4,
    "3045": 1.5,
    "3050": 1.6,
    "3055": 1.7,
    "3060": 1.8,
    "3065": 1.9,
    "3070": 2.0,
    "3075": 2.1,
    "3080": 2.2,
    "3085": 2.3,
    "3090": 2.4,
    "3095": 2.5,
    "3100": 2.6,
    "3105": 2.7,
    "3110": 2.8,
    "3115": 2.9,
    "3120": 3.0,
    "3125": 3.1,
    "3130": 3.2
"""
# print(price_dic[A_dic["3100"]])
print(price_dic)
# 创建一个color_dic字典存储颜色和对应tpo单位
color_dic = {
    "A": "#E8E8E8",
    "B": "#CFCFCF",
    "C": "#B5B5B5",
    "D": "#9C9C9C",
    "E": "#828282"
}
print(color_dic["A"])

plt.rcParams['font.sans-serif'] = ['FangSong']

plt.figure(figsize=(8, 8))  # 绘制一个8*8的画布
ax = plt.axes()
bar_width = 0.05  # 条形宽度

# 第一组
# A
# 第一个钟形图第1条y轴起始位置，钟形图每条间距，间隔0.1紧挨
fname = [2.6]
# 第一个钟形图第1条长度
fspend = [0.15]
fname1 = [2.7]
fspend1 = [0.15]
fname2 = [2.8]
fspend2 = [0.15]
fname3 = [2.9]
fspend3 = [0.15]
fname4 = [3.0]
fspend4 = [0.15]
fname5 = [3.1]
fspend5 = [0.15]
fname6 = [3.2]
fspend6 = [0.15]
# 参数:  height:高  color:条行颜色  align:条形上下位置    left:left为相对于y轴的距离   alpha:颜色变化
# fill：条形填充  joinstyle:两条线段端点连接方式   label:条形标签
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#E8E8E8', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#E8E8E8', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#E8E8E8', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#E8E8E8', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#E8E8E8', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#E8E8E8', align='center', left=0,
        fill=True, joinstyle='bevel')
# B
fname = [2.4]
fspend = [0.15]
fname1 = [2.5]
fspend1 = [0.15]
fname2 = [2.6]
fspend2 = [0.15]
fname3 = [2.7]
fspend3 = [0.15]
fname4 = [2.8]
fspend4 = [0.15]
fname5 = [2.9]
fspend5 = [0.15]
fname6 = [3.0]
fspend6 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#CFCFCF', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#CFCFCF', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#CFCFCF', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#CFCFCF', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#CFCFCF', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#CFCFCF', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#CFCFCF', align='center', left=0.15,
        fill=True, joinstyle='bevel')

# C
fname = [2.3]
fspend = [0.15]
fname1 = [2.4]
fspend1 = [0.15]
fname2 = [2.5]
fspend2 = [0.15]
fname3 = [2.6]
fspend3 = [0.15]
fname4 = [2.7]
fspend4 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#B5B5B5', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#B5B5B5', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#B5B5B5', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#B5B5B5', align='center', left=0.3,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#B5B5B5', align='center', left=0.3,
        fill=True, joinstyle='bevel')

# D
fname = [2.1]
fspend = [0.15]
fname1 = [2.2]
fspend1 = [0.15]
fname2 = [2.3]
fspend2 = [0.15]
fname3 = [2.4]
fspend3 = [0.15]
fname4 = [2.5]
fspend4 = [0.15]
fname5 = [2.6]
fspend5 = [0.15]
fname6 = [2.7]
fspend6 = [0.15]
fname7 = [2.8]
fspend7 = [0.15]
fname8 = [2.9]
fspend8 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#9C9C9C', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#9C9C9C', align='center', left=0,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#9C9C9C', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#9C9C9C', align='center', left=0.3,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#9C9C9C', align='center', left=0.3,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#9C9C9C', align='center', left=0.45,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#9C9C9C', align='center', left=0.45,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#9C9C9C', align='center', left=0.3,
        fill=True, joinstyle='bevel')
ax.barh(fname8, fspend8, height=0.1, color='#9C9C9C', align='center', left=0.3,
        fill=True, joinstyle='bevel')

# E
fname = [2.1]
fspend = [0.15]
fname1 = [2.2]
fspend1 = [0.15]
fname2 = [2.3]
fspend2 = [0.15]
fname3 = [2.4]
fspend3 = [0.15]
fname4 = [2.5]
fspend4 = [0.15]
fname5 = [2.6]
fspend5 = [0.15]
fname6 = [2.7]
fspend6 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#828282', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#828282', align='center', left=0.15,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#828282', align='center', left=0.3,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#828282', align='center', left=0.45,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#828282', align='center', left=0.45,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#828282', align='center', left=0.6,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#828282', align='center', left=0.6,
        fill=True, joinstyle='bevel')

# 第二组
# A
# 第一个钟形图第1条y轴起始位置，钟形图每条间距，间隔0.1紧挨
fname = [2.2]
# 第一个钟形图第1条长度
fspend = [0.15]
fname1 = [2.3]
fspend1 = [0.15]
fname2 = [2.4]
fspend2 = [0.15]
fname3 = [2.5]
fspend3 = [0.15]
fname4 = [2.6]
fspend4 = [0.15]
fname5 = [2.7]
fspend5 = [0.15]
# 参数:  height:高  color:条行颜色  align:条形上下位置    left:left为相对于y轴的距离   alpha:颜色变化
# fill：条形填充  joinstyle:两条线段端点连接方式   label:条形标签
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#E8E8E8', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#E8E8E8', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#E8E8E8', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#E8E8E8', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#E8E8E8', align='center', left=0.75,
        fill=True, joinstyle='bevel')
# B
fname = [2.0]
fspend = [0.15]
fname1 = [2.1]
fspend1 = [0.15]
fname2 = [2.2]
fspend2 = [0.15]
fname3 = [2.3]
fspend3 = [0.15]
fname4 = [2.4]
fspend4 = [0.15]
fname5 = [2.5]
fspend5 = [0.15]
fname6 = [2.6]
fspend6 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#CFCFCF', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#CFCFCF', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#CFCFCF', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#CFCFCF', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#CFCFCF', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#CFCFCF', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#CFCFCF', align='center', left=0.9,
        fill=True, joinstyle='bevel')

# C
fname = [2.3]
fspend = [0.15]
fname1 = [2.4]
fspend1 = [0.15]
fname2 = [2.5]
fspend2 = [0.15]
fname3 = [2.6]
fspend3 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#B5B5B5', align='center', left=1.05,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#B5B5B5', align='center', left=1.05,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#B5B5B5', align='center', left=1.05,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#B5B5B5', align='center', left=1.05,
        fill=True, joinstyle='bevel')

# D
fname = [1.7]
fspend = [0.15]
fname1 = [1.8]
fspend1 = [0.15]
fname2 = [1.9]
fspend2 = [0.15]
fname3 = [2.0]
fspend3 = [0.15]
fname4 = [2.1]
fspend4 = [0.15]
fname5 = [2.2]
fspend5 = [0.15]
fname6 = [2.3]
fspend6 = [0.15]
fname7 = [2.4]
fspend7 = [0.15]
fname8 = [2.5]
fspend8 = [0.15]
fname9 = [2.6]
fspend9 = [0.15]
fname10 = [2.7]
fspend10 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#9C9C9C', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#9C9C9C', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#9C9C9C', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#9C9C9C', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#9C9C9C', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#9C9C9C', align='center', left=1.05,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#9C9C9C', align='center', left=1.2,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#9C9C9C', align='center', left=1.2,
        fill=True, joinstyle='bevel')
ax.barh(fname8, fspend8, height=0.1, color='#9C9C9C', align='center', left=1.2,
        fill=True, joinstyle='bevel')
ax.barh(fname9, fspend9, height=0.1, color='#9C9C9C', align='center', left=1.2,
        fill=True, joinstyle='bevel')
ax.barh(fname10, fspend10, height=0.1, color='#9C9C9C', align='center', left=0.9,
        fill=True, joinstyle='bevel')

# E
fname = [1.6]
fspend = [0.15]
fname1 = [1.7]
fspend1 = [0.15]
fname2 = [1.8]
fspend2 = [0.15]
fname3 = [1.9]
fspend3 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#828282', align='center', left=0.75,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#828282', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#828282', align='center', left=0.9,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#828282', align='center', left=0.9,
        fill=True, joinstyle='bevel')

# 第三组
# A
# 第一个钟形图第1条y轴起始位置，钟形图每条间距，间隔0.1紧挨
fname = [0.1]
# 第一个钟形图第1条长度
fspend = [0.15]
fname1 = [0.2]
fspend1 = [0.15]
fname2 = [0.3]
fspend2 = [0.15]
fname3 = [0.4]
fspend3 = [0.15]
fname4 = [0.5]
fspend4 = [0.15]
fname5 = [0.6]
fspend5 = [0.15]
fname6 = [0.7]
fspend6 = [0.15]
fname7 = [0.8]
fspend7 = [0.15]
fname8 = [0.9]
fspend8 = [0.15]
fname9 = [1.0]
fspend9 = [0.15]
# 参数:  height:高  color:条行颜色  align:条形上下位置    left:left为相对于y轴的距离   alpha:颜色变化
# fill：条形填充  joinstyle:两条线段端点连接方式   label:条形标签
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname8, fspend8, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname9, fspend9, height=0.1, color='#E8E8E8', align='center', left=1.5,
        fill=True, joinstyle='bevel')
# B
fname = [0.8]
fspend = [0.15]
fname1 = [0.9]
fspend1 = [0.15]
fname2 = [1.0]
fspend2 = [0.15]
fname3 = [1.1]
fspend3 = [0.15]
fname4 = [1.2]
fspend4 = [0.15]
fname5 = [1.3]
fspend5 = [0.15]
fname6 = [1.4]
fspend6 = [0.15]
fname7 = [1.5]
fspend7 = [0.15]
fname8 = [1.6]
fspend8 = [0.15]
fname9 = [1.7]
fspend9 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#CFCFCF', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#CFCFCF', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#CFCFCF', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#CFCFCF', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#CFCFCF', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#CFCFCF', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#CFCFCF', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#CFCFCF', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname8, fspend8, height=0.1, color='#CFCFCF', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname9, fspend9, height=0.1, color='#CFCFCF', align='center', left=1.5,
        fill=True, joinstyle='bevel')

# C
fname = [1.3]
fspend = [0.15]
fname1 = [1.4]
fspend1 = [0.15]
fname2 = [1.5]
fspend2 = [0.15]
fname3 = [1.6]
fspend3 = [0.15]
fname4 = [1.7]
fspend4 = [0.15]
fname5 = [1.8]
fspend5 = [0.15]
fname6 = [1.9]
fspend6 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#B5B5B5', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#B5B5B5', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#B5B5B5', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#B5B5B5', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#B5B5B5', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#B5B5B5', align='center', left=1.5,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#B5B5B5', align='center', left=1.5,
        fill=True, joinstyle='bevel')

# D
fname = [0.8]
fspend = [0.15]
fname1 = [0.9]
fspend1 = [0.15]
fname2 = [1.0]
fspend2 = [0.15]
fname3 = [1.1]
fspend3 = [0.15]
fname4 = [1.2]
fspend4 = [0.15]
fname5 = [1.3]
fspend5 = [0.15]
fname6 = [1.4]
fspend6 = [0.15]
fname7 = [1.5]
fspend7 = [0.15]
fname8 = [1.6]
fspend8 = [0.15]
fname9 = [1.7]
fspend9 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#9C9C9C', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#9C9C9C', align='center', left=1.65,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname8, fspend8, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname9, fspend9, height=0.1, color='#9C9C9C', align='center', left=1.8,
        fill=True, joinstyle='bevel')

# E
fname = [0.8]
fspend = [0.15]
fname1 = [0.9]
fspend1 = [0.15]
fname2 = [1.0]
fspend2 = [0.15]
fname3 = [1.1]
fspend3 = [0.15]
fname4 = [1.2]
fspend4 = [0.15]
fname5 = [1.3]
fspend5 = [0.15]
fname6 = [1.4]
fspend6 = [0.15]
fname7 = [1.5]
fspend7 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#828282', align='center', left=1.95,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#828282', align='center', left=1.95,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#828282', align='center', left=1.95,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#828282', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#828282', align='center', left=1.8,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#828282', align='center', left=1.95,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#828282', align='center', left=1.95,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#828282', align='center', left=1.95,
        fill=True, joinstyle='bevel')

# 第四组
# A
# 第一个钟形图第1条y轴起始位置，钟形图每条间距，间隔0.1紧挨
fname = [0.6]
# 第一个钟形图第1条长度
fspend = [0.15]
fname1 = [0.7]
fspend1 = [0.15]
fname2 = [0.8]
fspend2 = [0.15]
fname3 = [0.9]
fspend3 = [0.15]
fname4 = [1.0]
fspend4 = [0.15]
fname5 = [1.1]
fspend5 = [0.15]
fname6 = [1.2]
fspend6 = [0.15]
fname7 = [1.3]
fspend7 = [0.15]
fname8 = [1.4]
fspend8 = [0.15]
fname9 = [1.5]
fspend9 = [0.15]
fname10 = [1.6]
fspend10 = [0.15]
fname11 = [1.7]
fspend11 = [0.15]
fname12 = [1.8]
fspend12 = [0.15]
# 参数:  height:高  color:条行颜色  align:条形上下位置    left:left为相对于y轴的距离   alpha:颜色变化
# fill：条形填充  joinstyle:两条线段端点连接方式   label:条形标签
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname8, fspend8, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname9, fspend9, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname10, fspend10, height=0.1, color='#E8E8E8',  align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname11, fspend11, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname12, fspend12, height=0.1, color='#E8E8E8', align='center', left=2.25,
        fill=True, joinstyle='bevel')
# B
fname = [1.6]
fspend = [0.15]
fname1 = [1.7]
fspend1 = [0.15]
fname2 = [1.8]
fspend2 = [0.15]
fname3 = [1.9]
fspend3 = [0.15]
fname4 = [2.0]
fspend4 = [0.15]
fname5 = [2.1]
fspend5 = [0.15]
fname6 = [2.2]
fspend6 = [0.15]
fname7 = [2.3]
fspend7 = [0.15]
fname8 = [2.4]
fspend8 = [0.15]
fname9 = [2.5]
fspend9 = [0.15]
fname10 = [2.6]
fspend10 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#CFCFCF', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#CFCFCF', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#CFCFCF', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname7, fspend7, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname8, fspend8, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname9, fspend9, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname10, fspend10, height=0.1, color='#CFCFCF', align='center', left=2.25,
        fill=True, joinstyle='bevel')

# C
fname = [1.9]
fspend = [0.15]
fname1 = [2.0]
fspend1 = [0.15]
fname2 = [2.1]
fspend2 = [0.15]
fname3 = [2.2]
fspend3 = [0.15]
fname4 = [2.3]
fspend4 = [0.15]
fname5 = [2.4]
fspend5 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#B5B5B5', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#B5B5B5', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#B5B5B5', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#B5B5B5', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#B5B5B5', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#B5B5B5', align='center', left=2.4,
        fill=True, joinstyle='bevel')

# D
fname = [2.2]
fspend = [0.15]
fname1 = [2.3]
fspend1 = [0.15]
fname2 = [2.4]
fspend2 = [0.15]
fname3 = [2.5]
fspend3 = [0.15]
fname4 = [2.6]
fspend4 = [0.15]
fname5 = [2.7]
fspend5 = [0.15]
fname6 = [2.8]
ax.barh(fname, fspend, height=0.1, color='#9C9C9C', align='center', left=2.55,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#9C9C9C', align='center', left=2.55,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#9C9C9C', align='center', left=2.55,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#9C9C9C', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#9C9C9C', align='center', left=2.4,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#9C9C9C', align='center', left=2.25,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#9C9C9C', align='center', left=2.25,
        fill=True, joinstyle='bevel')

# E
fname = [2.4]
fspend = [0.15]
fname1 = [2.5]
fspend1 = [0.15]
fname2 = [2.6]
fspend2 = [0.15]
fname3 = [2.7]
fspend3 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#828282', align='center', left=2.7,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#828282', align='center', left=2.55,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#828282', align='center', left=2.55,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#828282', align='center', left=2.4,
        fill=True, joinstyle='bevel')

# 第五组
# A
# 第一个钟形图第1条y轴起始位置，钟形图每条间距，间隔0.1紧挨
fname = [2.4]
# 第一个钟形图第1条长度
fspend = [0.15]
fname1 = [2.5]
fspend1 = [0.15]
fname2 = [2.6]
fspend2 = [0.15]
fname3 = [2.7]
fspend3 = [0.15]
fname4 = [2.8]
fspend4 = [0.15]
# 参数:  height:高  color:条行颜色  align:条形上下位置    left:left为相对于y轴的距离   alpha:颜色变化
# fill：条形填充  joinstyle:两条线段端点连接方式   label:条形标签
ax.barh(fname, fspend, height=0.1, color='#E8E8E8',  align='center', left=3,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#E8E8E8', align='center', left=3,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#E8E8E8', align='center', left=3,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#E8E8E8', align='center', left=3,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#E8E8E8', align='center', left=3,
        fill=True, joinstyle='bevel')
# B
fname = [2.1]
fspend = [0.15]
fname1 = [2.2]
fspend1 = [0.15]
fname2 = [2.3]
fspend2 = [0.15]
fname3 = [2.4]
fspend3 = [0.15]
fname4 = [2.5]
fspend4 = [0.15]
fname5 = [2.6]
fspend5 = [0.15]
fname6 = [2.7]
fspend6 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#CFCFCF', align='center', left=3,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#CFCFCF', align='center', left=3,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#CFCFCF', align='center', left=3,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#CFCFCF', align='center', left=3.15,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#CFCFCF', align='center', left=3.15,
        fill=True, joinstyle='bevel')
ax.barh(fname5, fspend5, height=0.1, color='#CFCFCF', align='center', left=3.15,
        fill=True, joinstyle='bevel')
ax.barh(fname6, fspend6, height=0.1, color='#CFCFCF', align='center', left=3.15,
        fill=True, joinstyle='bevel')

# C
fname = [2.1]
fspend = [0.15]
fname1 = [2.2]
fspend1 = [0.15]
fname2 = [2.3]
fspend2 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#B5B5B5', align='center', left=3.15,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#B5B5B5', align='center', left=3.15,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#B5B5B5', align='center', left=3.15,
        fill=True, joinstyle='bevel')

# D
fname = [2.1]
fspend = [0.15]
fname1 = [2.2]
fspend1 = [0.15]
fname2 = [2.3]
fspend2 = [0.15]
fname3 = [2.4]
fspend3 = [0.15]
fname4 = [2.5]
fspend4 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#9C9C9C', align='center', left=3.3,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#9C9C9C', align='center', left=3.3,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#9C9C9C', align='center', left=3.3,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#9C9C9C', align='center', left=3.3,
        fill=True, joinstyle='bevel')
ax.barh(fname4, fspend4, height=0.1, color='#9C9C9C', align='center', left=3.3,
        fill=True, joinstyle='bevel')

# E
fname = [2.1]
fspend = [0.15]
fname1 = [2.2]
fspend1 = [0.15]
fname2 = [2.3]
fspend2 = [0.15]
fname3 = [2.4]
fspend3 = [0.15]
ax.barh(fname, fspend, height=0.1, color='#828282', align='center', left=3.45,
        fill=True, joinstyle='bevel')
ax.barh(fname1, fspend1, height=0.1, color='#828282', align='center', left=3.45,
        fill=True, joinstyle='bevel')
ax.barh(fname2, fspend2, height=0.1, color='#828282', align='center', left=3.45,
        fill=True, joinstyle='bevel')
ax.barh(fname3, fspend3, height=0.1, color='#828282', align='center', left=3.45,
        fill=True, joinstyle='bevel')

# ax.set_xticks(spend) # 修改X轴刻度值字体大小
# ax.set_yticks(name) # 修改y轴刻度值字体大小

# ax.set_title('title',fontsize=30) # 设置图标标题
ax.set_xlabel('x轴', fontsize=20)  # 设置x轴标题
ax.set_ylabel('y轴', fontsize=20)  # 设置y轴标题

ax.grid(axis='x')  # 设置仅显示x轴网格线
plt.axis('off')  # 不显示坐标轴
# ax.legend()  # 显示图例
plt.show()


