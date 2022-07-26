# 项目结构如下

## 一、生成train数据 
### 1.反转模式（reversal）  
+ ***存放生成反转模式图像的程序***  
```
  1.FindReversalPattern_生成趋势结束.py 
  2.FindReversalPattern_出金叉后_生成最低点及历史数据.py 
  3.FindReversalPattern_出死叉后_生成最高点及历史数据.py 
  4.FindReversalPattern_出死叉后_根据最高点跌幅判断反转.py 
```  

### 2.市场轮廓图（TPO）  
+ ***存放生成TPO图像的程序***  
```
  1.GetTPOImage.py 
  2.data.py 
  3.绘制市场轮廓图demo.py 
```  

## 二、Helper 
### 1.生成图片类库（DrawHelper）  
```
  1.DrawHelper.py 
```  
### 2.压缩文件类库（ZipHelper）  
```
  1.ZipHelper.py 
```  

## 三、Strategy  
### 1.策略文件夹（Strategy）  
```
  1.MA.py 
  2.REF.py 
```  