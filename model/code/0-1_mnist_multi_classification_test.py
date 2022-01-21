import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(_, _), (x_test, y_test) = mnist.load_data()

# we can check how many number 0, 1

# print(np.count_nonzero(y_train==0)) # 5923
# print(np.count_nonzero(y_train==1)) # 6742

# extract  0 and 1

mask_01_test = []

for i, label in enumerate(y_test):
    if label == 0 or label == 1:
        mask_01_test.append(i)

x_test = x_test[mask_01_test]
y_test = y_test[mask_01_test]

# make reverse train and test image ( reverse mean [255 - image])
x_test_re = (255 - x_test)

# concatenate org image and reversed image
x_test = np.concatenate((x_test, x_test_re),axis=0)

y_test = np.concatenate((y_test, y_test), axis=0)

# make label for multi label image classification

test_zeros = np.zeros((len(y_test)//2))
test_ones = np.ones((len(y_test)//2))
test_zeros_and_ones = np.concatenate((test_zeros, test_ones), axis=0)

test_zeros_and_ones = test_zeros_and_ones.reshape(len(test_zeros_and_ones), 1)
y_test = y_test.reshape(len(y_test), 1)

y_test = np.concatenate((y_test, test_zeros_and_ones), axis=1)

# 0 to 1
x_test =  x_test / 255.0

# data shuffle
random_test = np.array(range(len(y_test)))
np.random.shuffle(random_test)

x_test = x_test[random_test]
y_test = y_test[random_test]

x_test = x_test.reshape(len(x_test), 28, 28, 1)

# image check

# for i in range(10):
#     print(y_test[i])
#     plt.imshow(x_test[i, :, :, 0])
#     plt.colorbar()
#     plt.show()

model = keras.models.load_model("mnist_test_model.h5")
model.evaluate(x_test, y_test)
