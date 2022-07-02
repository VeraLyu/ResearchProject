![](https://img.shields.io/github/repo-size/carlolepelaars/ghostnet_tf2)

# ghostnet_tf2
An implementation of GhostNet for Tensorflow 2.0+ (From the paper "GhostNet: More Features from Cheap Operations")

Link to paper: https://arxiv.org/pdf/1911.11907.pdf

这个代码出现了一点问题，训练正确率能达到100%，但是测试时预测结果每一个都一样，大家帮忙看一下，非常感谢！
数据集在另一个文件夹里面，/dataset,直接复制到这个主文件夹里面就可以用。
运行 ： python main.py  --nets=ghostnet  --batch_size=32   --lr=0.001   --epochs=10
