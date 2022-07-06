import matplotlib.pyplot as plt
import numpy as np
 
plt.rcParams['font.sans-serif']=['FangSong']
 
plt.figure(figsize=(8,8))# 绘制一个8*8的画布
ax=plt.axes()
bar_width=0.2  # 条形宽度
 
fname=[2.1]
fspend=[1]

fname1=[2.2]
fspend1=[2]

fname2=[2.3]
fspend2=[3]

fname3=[2.4]
fspend3=[1]

# 第一组
ax.barh(fname,fspend,height=0.1,color='#00FA9A',ec='#A0522D',linewidth='0',align='center',left=0,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='a')
# 第一组
ax.barh(fname1,fspend1,height=0.1,color='#A0522D',ec='#A0522D',linewidth='0',align='center',left=0,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='b')
# 第一组
ax.barh(fname2,fspend2,height=0.1,color='#EEE8AA',ec='#A0522D',linewidth='0',align='center',left=0,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='c')
# 第一组
ax.barh(fname3,fspend3,height=0.1,color='#EEE8AA',ec='#A0522D',linewidth='0',align='center',left=0,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='c')

sname=[2.8]
sspend=[1]

sname1=[2.9]
sspend1=[3]

sname2=[3]
sspend2=[2]

sname3=[3.1]
sspend3=[1]

sname4=[3.2]
sspend4=[1]

# 第二组
ax.barh(sname,sspend,height=0.1,color='#00FA9A',ec='#A0522D',linewidth='0',align='center',left=3,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='a')
# 第二组
ax.barh(sname1,sspend1,height=0.1,color='#A0522D',ec='#A0522D',linewidth='0',align='center',left=3,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='b')
# 第二组
ax.barh(sname2,sspend2,height=0.1,color='#EEE8AA',ec='#A0522D',linewidth='0',align='center',left=3,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='c')
# 第二组
ax.barh(sname3,sspend3,height=0.1,color='#EEE8AA',ec='#A0522D',linewidth='0',align='center',left=3,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='c')
# 第二组
ax.barh(sname4,sspend4,height=0.1,color='#EEE8AA',ec='#A0522D',linewidth='0',align='center',left=3,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='c')

tname=[2.3]
tspend=[1]

tname1=[2.4]
tspend1=[2]

tname2=[2.5]
tspend2=[3]

tname3=[2.6]
tspend3=[1]

tname4=[2.7]
tspend4=[1]

tname5=[2.8]
tspend5=[2]

tname5=[2.9]
tspend5=[1]

# 第三组
ax.barh(tname,tspend,height=0.1,color='#EFEFEF',ec='#A0522D',linewidth='0',align='center',left=7,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='a')
# 第三组
ax.barh(tname1,tspend1,height=0.1,color='#EFEFEF',ec='#A0522D',linewidth='0',align='center',left=7,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel',label='b')
# 第三组
ax.barh(tname2,tspend2,height=0.1,color='#EFEFEF',ec='#A0522D',linewidth='0',align='center',left=7,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel')
# 第三组
ax.barh(tname3,tspend3,height=0.1,color='#EFEFEF',ec='#A0522D',linewidth='0',align='center',left=7,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel')
# 第三组
ax.barh(tname4,tspend4,height=0.1,color='#EFEFEF',ec='#A0522D',linewidth='0',align='center',left=7,alpha=0.5,
      linestyle='-',fill=True,joinstyle='bevel')

fname=[2.5]
fspend=[2]

fname1=[2.6]
fspend1=[1]

# 叠加
ax.barh(fname,fspend,height=0.1,color='#353535',linewidth='0',align='center',left=10,alpha=0.5,linestyle='-',fill=True,joinstyle='bevel')

# 叠加
ax.barh(fname1,fspend1,height=0.1,color='#A3A3A3',linewidth='0',align='center',left=8,alpha=0.5,linestyle='-',fill=True,joinstyle='bevel')

#ax.set_xticks(spend) # 修改X轴刻度值字体大小
#ax.set_yticks(name) # 修改y轴刻度值字体大小
 
#ax.set_title('title',fontsize=30) # 设置图标标题
ax.set_xlabel('x轴',fontsize=20)  # 设置x轴标题
ax.set_ylabel('y轴',fontsize=20)  # 设置y轴标题
 
ax.grid(axis='x') # 设置仅显示x轴网格线
plt.axis('off') #不显示坐标轴
ax.legend()  # 显示图例
plt.show()