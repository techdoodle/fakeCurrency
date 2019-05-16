import cv2
from os import listdir

sampleNum = 40
for i in listdir('/home/pranab/Desktop/fake/new_images/'):
	img = cv2.imread('/home/pranab/Desktop/fake/new_images/'+str(i),0)

	print(img)
	# width = 1198
	# height = 502
	width = 946
	height = 373

	# print(img)
	# cv2.imshow('test',img)
	# cv2.waitKey(0)
	correctSize = cv2.resize(img,(width,height))

	# seeThrough = correctSize[224:288, 74:110]
	# latentImg45 = correctSize[300:360, 90:235]
	# devnagiri = correctSize[177:336, 212:274]
	# gandhi = correctSize[80:354, 314:500]
	# rbi = correctSize[]
	# greenBlue = correctSize[77:326, 663:704]
	govSignature = correctSize[160:252, 585:680]
	# electrotypeWatermark = correctSize[98:291, 854:1060]
	# numberPanel = correctSize[310:350, 730:870]
	rupeeSymbol = correctSize[250:312, 700:860]
	ashoka = correctSize[210:317, 860:930]
	horizontalRec = correctSize[179: 235, 863:925]
	leftLines = correctSize[85:187, 1:33]
	rightLines = correctSize[90:191, 914:943]

	sampleNum = sampleNum + 1

	path = '/home/pranab/Desktop/fake/FINALIMAGES/'

	# cv2.imwrite(path+'front-1_'+sampleNum+'.png',seeThrough)
	# cv2.imwrite(path+'front-2_'+sampleNum+'.png',latentImg45)
	# cv2.imwrite('/home/pranab/Desktop/fake/IM/devnagiri.png',devnagiri)
	# cv2.imwrite(path+'front-4_'+sampleNum+'.png', gandhi)
	# cv2.imwrite('/home/pranab/Desktop/fake/IM/rbi.png',rbi)
	# cv2.imwrite('/home/pranab/Desktop/fake/IM/greenBlue.png',greenBlue)
	cv2.imwrite(path+'front-7_'+str(sampleNum)+'.png',govSignature)
	# cv2.imwrite('/home/pranab/Desktop/fake/IM4/electrotypeWatermark.png',electrotypeWatermark)
	# cv2.imwrite(path+'front-9_'+sampleNum+'.png',numberPanel)
	cv2.imwrite(path+'front-10_'+str(sampleNum)+'.png',rupeeSymbol)
	cv2.imwrite(path+'front-11_'+str(sampleNum)+'.png',ashoka)
	cv2.imwrite(path+'front-12_'+str(sampleNum)+'.png',horizontalRec)
	cv2.imwrite(path+'front-13_'+str(sampleNum)+'.png',leftLines)
	cv2.imwrite(path+'front-14_'+str(sampleNum)+'.png',rightLines)

