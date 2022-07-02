# 一、Stock_image_classification文件夹
## 该文件夹里面主要是实现趋势反转的分类算法
**几乎所有的算法，训练集都达到了100%，在测试集上,batch_size设置比较大的时候预测效果不太好，batch_size设置为1、2、4时测试正确率接近100%。**

# 二、GhostNet文件夹
这个代码出现了一点问题，训练正确率能达到100%，但是测试时预测结果每一个都一样，大家帮忙看一下，非常感谢！ 数据集在另一个文件夹里面，/dataset,直接复制到这个主文件夹里面就可以用。
运行 ：
```
python main.py --nets=ghostnet --batch_size=32 --lr=0.001 --epochs=10
```
