import cv2
import os
os.chdir("~/Users/sahil/rari-pics")
img = cv2.imread("cam-2018-11-20_2156.jpeg")
crop_img = img[0:2597,100:630]
cv2.imshow("cropped", crop_img)
