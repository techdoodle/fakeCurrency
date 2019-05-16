# import numpy as np
import cv2
# # from matplotlib import pyplot as plt

# # img = cv2.imread('/home/pranab/Desktop/rupee.jpg',0)
img = cv2.imread('/home/pranab/Desktop/fake/IM9/8.jpg',0)

# cv2.imshow('/home/pranab/Desktop/rupee.jpg',0)
# # plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# # plt.show()
# # cropped_img = img.crop((w//2 - 50//2, h//2 - 50//2, w//2 + 50//2, h//2 + 50//2))

# height, width = img.shape
# print(height, width)

# x=100
# y=100
# h=50
# w=100

# # crop_img = img[y:y+h, x:x+w]
crop_img = img[0:373,0:946]
cv2.imshow("cropped", crop_img)


cv2.waitKey(5000000)

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
# # cv2.imshow(cropped_img)

# import os
# from os import listdir

# for i in listdir('/home/pranab/Desktop/fake/testImages/'):
#     print(i)


# cv2.imwrite(path+'seeThrough.png',seeThrough)
# cv2.imwrite(path+'latentImg45.png',latentImg45)
# # cv2.imwrite('/home/pranab/Desktop/fake/IM/devnagiri.png',devnagiri)
# cv2.imwrite(path+'gandhi.png',gandhi)
# # cv2.imwrite('/home/pranab/Desktop/fake/IM/greenBlue.png',greenBlue)
# cv2.imwrite(path+'govSignature.png',govSignature)
# # cv2.imwrite('/home/pranab/Desktop/fake/IM4/electrotypeWatermark.png',electrotypeWatermark)
# cv2.imwrite(path+'numberPanel.png',numberPanel)
# cv2.imwrite(path+'rupeeSymbol.png',rupeeSymbol)
# cv2.imwrite(path+'ashoka.png',ashoka)
# # cv2.imwrite('/home/pranab/Desktop/fake/IM/horizontalRec.png',horizontalRec)
# cv2.imwrite(path+'leftLines.png',leftLines)
# cv2.imwrite(path+'rightLines.png',rightLines)
