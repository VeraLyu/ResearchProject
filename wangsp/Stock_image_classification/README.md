

<h2 align=center>股票反转趋势二分类</h2>


## Usage
```bash
$ python main.py 
    --nets={NETS} 
    --batch_size={BATCH_SIZE} 
    --lr={LEARNING_RATE} 
    --epochs={EPOCHS}
```

## Models

- [VGG](#vgg)
- [GoogLeNet](#googlenet)
- [ResNet](#resnet)
- [DenseNet](#densenet)
- [InceptionV3](#inceptionv3)
- [InceptionV4](#inceptionv4)
- [MobileNet](#mobilenet)
- [MobileNetV2](#mobilenetv2)
- [Squeezenet](#squeezenet)
- [SENet](#senet)
- [ShuffleNet](#shufflenet)
- [CondenseNet](#condenseNet)
- [Xcention](#xception)
- [PreActResNet](#preactresnet)
- [ResAttNet](#resattnet)
- [ResNeXt](#resnext)
- [PolyNet](#polynet)
- [PyramidNet](#pyramidnet)


<hr>

<a name='vgg'></a>

### VGG

**Paper** [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)<br>
**Author** Karen Simonyan, Andrew Zissermanr<br>
<br><br>
**Model Options**

```bash
--nets {VGG11 or VGG13 or VGG16 or VGG19}
```

<hr>

<a name='googlenet'></a>

### GoogLeNet

**Paper** [Going Deeper with Convolutions](https://arxiv.org/abs/1409.4842)<br>
**Author** Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, Andrew Rabinovich<br>
<br><br>
**Model Options**

```bash
--nets {GoogLeNet}
```

<hr>

<a name='resnet'></a>

### ResNet

**Paper** [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)<br>
**Author** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun<br>
<br><br>
**Model Options**

```bash
--nets {ResNet18 or ResNet34 ResNet50 ResNet101 ResNet 152}
```

<hr>
<a name='densenet'></a>

### DenseNet

**Paper** [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)<br>
**Author** Gao Huang, Zhuang Liu, Laurens van der Maaten, Kilian Q. Weinberger
<br>
<br><br>
**Model Options**

```bash
--nets {DenseNet121 or DenseNet169 or DenseNet201 or DenseNet161}
```

<hr>


<a name='inceptionv3'></a>

### InceptionV3

**Paper** [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567)<br>
**Author** Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, Zbigniew Wojna
<br>
<br><br>
**Model Options**

```bash
--nets {InceptionV3}
```

<hr>

<a name='inceptionv4'></a>

### InceptionV4

**Paper** [Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning](https://arxiv.org/abs/1602.07261)<br>
**Author** Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi
<br>
<br><br>
**Model Options**

```bash
--nets {InceptionV4}
```

<hr>

<a name='mobilenet'></a>

### MobileNet

**Paper** [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)<br>
**Author** Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto, Hartwig Adam
<br>
<br><br>
**Model Options**

```bash
--nets {MobileNet}
```

<hr>

<a name='mobilenetv2'></a>

### MobileNetV2

**Paper** [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)<br>
**Author** Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, Liang-Chieh Chen
<br>
<br><br>
**Model Options**

```bash
--nets {MobileNetV2}
```

<hr>

<a name='squeezenet'></a>

### SqueezeNet

**Paper** [SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size](https://arxiv.org/abs/1602.07360)<br>
**Author** Forrest N. Iandola, Song Han, Matthew W. Moskewicz, Khalid Ashraf, William J. Dally, Kurt Keutzer
<br>
<br><br>
**Model Options**

```bash
--nets {SqueezeNet}
```

<hr>

<a name='SENet'></a>

### SENet

**Paper** [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507)<br>
**Author** Jie Hu, Li Shen, Samuel Albanie, Gang Sun, Enhua Wu
<br>
<br><br>
**Model Options**

```bash
--nets {SEResNet18 or SEResNet34 or SEResNet50 or SEResNet101 or SEResNet152}
```

<hr>

<a name='shufflenet'></a>

### ShuffleNet

**Paper** [ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices](https://arxiv.org/abs/1707.01083)<br>
**Author** Xiangyu Zhang, Xinyu Zhou, Mengxiao Lin, Jian Sun
<br>
<br><br>
**Model Options**


<hr>

<a name='condensenet'></a>

### CondenseNet

**Paper** [CondenseNet: An Efficient DenseNet using Learned Group Convolutions](https://arxiv.org/abs/1711.09224)<br>
**Author** Gao Huang, Shichen Liu, Laurens van der Maaten, Kilian Q. Weinberger
<br>
<br><br>
**Model Options**


<hr>

<a name='xception'></a>

### Xception

**Paper** [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357)<br>
**Author** François Chollet
<br>
<br><br>
**Model Options**



<hr>

<a name='preactresnet'></a>

### PreActResNet

**Paper** [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027)<br>
**Author** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
<br>
<br><br>
**Model Options**



<hr>

<a name='resattnet'></a>

### ResAttNet

**Paper** [Residual Attention Network for Image Classification](https://arxiv.org/abs/1704.06904)<br>
**Author** Fei Wang, Mengqing Jiang, Chen Qian, Shuo Yang, Cheng Li, Honggang Zhang, Xiaogang Wang, Xiaoou Tang
<br>
<br><br>
**Model Options**



<hr>

<a name='polynet'></a>

### PolyNet

**Paper** [PolyNet: A Pursuit of Structural Diversity in Very Deep Networks](https://arxiv.org/abs/1611.05725)<br>
**Author** Xingcheng Zhang, Zhizhong Li, Chen Change Loy, Dahua Lin
<br>
<br><br>
**Model Options**



<hr>

<a name='pyramidnet'></a>

### PyramidNet

**Paper** [Deep Pyramidal Residual Networks](https://arxiv.org/abs/1610.02915)<br>
**Author** Dongyoon Han, Jiwhan Kim, Junmo Kim
<br>
<br><br>
**Model Options**



<hr>

## Reference

- https://github.com/weiaicunzai/pytorch-cifar100

