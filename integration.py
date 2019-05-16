import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm

from os import listdir
import cv2



def cropResizeImage(url):
	img = cv2.imread(url,0)

	width = 946
	height = 373

	correctSize = cv2.resize(img,(width,height))
	govSignature = correctSize[160:252, 585:680]
	rupeeSymbol = correctSize[250:312, 700:860]
	ashoka = correctSize[210:317, 860:930]
	horizontalRec = correctSize[179: 235, 863:925]
	leftLines = correctSize[85:187, 1:33]
	rightLines = correctSize[90:191, 914:943]

	path = '/home/pranab/Desktop/fake/testImages/'

	cv2.imwrite(path+'govSignature.png',govSignature)
	cv2.imwrite(path+'rupeeSymbol.png',rupeeSymbol)
	cv2.imwrite(path+'ashoka.png',ashoka)
	cv2.imwrite(path+'horizontalRec.png',horizontalRec)
	cv2.imwrite(path+'leftLines.png',leftLines)
	cv2.imwrite(path+'rightLines.png',rightLines)


def realFake():
	cropResizeImage('./data.jpg')
	train = pd.read_csv('/home/pranab/Desktop/fake/final.csv', sep=' ')

# We have grayscale images, so while loading the images we will keep grayscale=True, if you have RGB images, you should set grayscale as False
	train_image = []
	for a, b in train.itertuples(index=False):
	    # print(a)
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

	# TESTING PHASE
	test_image = []

	for i in listdir('/home/pranab/Desktop/fake/testImages/'):
	    # print(i)
	    img = image.load_img('/home/pranab/Desktop/fake/testImages/' + str(i), target_size=(32,32,1), grayscale=True)
	    img = image.img_to_array(img)
	    img = img/255
	    test_image.append(img)
	test = np.array(test_image)

	# making predictions
	prediction = model.predict_classes(test)

	# print(prediction)

	for i in [1, 2, 3, 4, 5, 6]:
	    if i not in prediction:
	        print('Fake')
	        return False
	    else:
	        pass
	    print('Real')
	    return True


realFake()
