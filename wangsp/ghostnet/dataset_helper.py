import os
import pickle
import numpy as np
import scipy.misc
from PIL import Image
from sklearn.model_selection import train_test_split
import cv2
def read_stock_image(image_width, image_height):
    path = "dataset/ReversalNegative"
    reversal_negative = os.listdir(path)
    dataset = []
    labels = []
    for i in range(len(reversal_negative)):
        image = cv2.imread(os.path.join(path,reversal_negative[i]))
        image = cv2.resize(image,dsize=(image_height,image_width))
        dataset.append(np.array(image))
        labels.append([1,0])
    path = "dataset/ReversalPositive"
    reversal_positive = os.listdir(path)
    for i in range(len(reversal_positive)):
        image = cv2.imread(os.path.join(path,reversal_positive[i]))
        image = cv2.resize(image,dsize=(image_height,image_width))
        dataset.append(np.array(image))
        labels.append([0,1])
    dataset = np.array(dataset)
    labels = np.array(labels,dtype=np.float32)
    print(dataset.shape)
    print(labels.shape)
    print(labels)
    x_trian,x_test,y_train,y_test = train_test_split(dataset,labels,test_size=0.2)
    print(x_trian.shape)
    print(y_train.shape)
    print(y_train)
    return x_trian,y_train,x_test,y_test
# read_cifar_10(224,224)
read_stock_image(224, 224)