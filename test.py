import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm
import os
from os import listdir


def realFake():
    train = pd.read_csv('/home/pranab/Desktop/fake/final.csv', sep=' ')

    print(train.head())

    # We have grayscale images, so while loading the images we will keep grayscale=True, if you have RGB images, you should set grayscale as False
    train_image = []
    for a, b in train.itertuples(index=False):
        print(a)
        try:
            img = image.load_img('/home/pranab/Desktop/fake/FINALIMAGES/' + a, target_size=(32,32,1), grayscale=True)
            img = image.img_to_array(img)
            img = img/255
            train_image.append(img)
        except:
            pass
    X = np.array(train_image)

    y = train['name'].values
    y = to_categorical(y)

    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(32,32,1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))

    model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))
    # model.fit(X, y, epochs=10)

    # TESTING PHASE
    test_image = []

    for i in listdir('/home/pranab/Desktop/fake/testImages/'):
        print(i)
        img = image.load_img('/home/pranab/Desktop/fake/testImages/' + str(i), target_size=(32,32,1), grayscale=True)
        img = image.img_to_array(img)
        img = img/255
        test_image.append(img)
    test = np.array(test_image)

    # making predictions
    prediction = model.predict_classes(test)

    print(prediction)

    for i in [1, 2, 3, 4, 5, 6]:
        if i not in prediction:
            print('Fake')
            return False
        else:
            pass
        print('Real')
        return True

realFake()