from random import random
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# we can check how many number 0, 1
# print(np.count_nonzero(y_train==0)) # 5923
# print(np.count_nonzero(y_train==1)) # 6742

# extract  0 and 1
mask_01_train = []
mask_01_test = []
for i, label in enumerate(y_train):
    if label == 0 or label == 1:
        mask_01_train.append(i)

for i, label in enumerate(y_test):
    if label == 0 or label == 1:
        mask_01_test.append(i)

x_train = x_train[mask_01_train]
y_train = y_train[mask_01_train]
x_test = x_test[mask_01_test]
y_test = y_test[mask_01_test]

# make reverse train and test image ( reverse mean [255 - image])
x_train_re = (255 - x_train)
x_test_re = (255 - x_test)

# concatenate org image and reversed image
x_train = np.concatenate((x_train, x_train_re), axis=0)
x_test = np.concatenate((x_test, x_test_re),axis=0)

y_train = np.concatenate((y_train, y_train), axis=0)
y_test = np.concatenate((y_test, y_test), axis=0)

# make label for multi label image classification
train_zeros = np.zeros((len(y_train)//2))
train_ones = np.ones((len(y_train)//2))
train_zeros_and_ones = np.concatenate((train_zeros, train_ones), axis=0)

train_zeros_and_ones = train_zeros_and_ones.reshape(len(train_zeros_and_ones), 1)
y_train = y_train.reshape(len(y_train), 1)

y_train = np.concatenate((y_train, train_zeros_and_ones), axis=1)


test_zeros = np.zeros((len(y_test)//2))
test_ones = np.ones((len(y_test)//2))
test_zeros_and_ones = np.concatenate((test_zeros, test_ones), axis=0)

test_zeros_and_ones = test_zeros_and_ones.reshape(len(test_zeros_and_ones), 1)
y_test = y_test.reshape(len(y_test), 1)

y_test = np.concatenate((y_test, test_zeros_and_ones), axis=1)

# 0 to 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# data shuffle
random_train = np.array(range(len(y_train)))
random_test = np.array(range(len(y_test)))
np.random.shuffle(random_train)
np.random.shuffle(random_test)

x_train = x_train[random_train]
y_train = y_train[random_train]
x_test = x_test[random_test]
y_test = y_test[random_test]


x_train = x_train.reshape(len(x_train), 28, 28, 1)
x_test = x_test.reshape(len(x_test), 28, 28, 1)

# check shape
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)


model = keras.Sequential(
    [
        keras.Input(shape=(28, 28, 1)),
        layers.Conv2D(16, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(128),
        layers.Dense(64),
        layers.Dense(2, activation="sigmoid"),
    ]
)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1)

model.evaluate(x_test, y_test)

model.save('mnist_test_model.h5')