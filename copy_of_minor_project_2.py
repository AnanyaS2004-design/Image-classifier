# -*- coding: utf-8 -*-
"""Copy of Minor project 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FW_xKhso-E9BoxQwcpnW_Rl2kLGUhlwC
"""

import numpy as np
import cv2
from google.colab.patches import cv2_imshow

!wget https://as2.ftcdn.net/v2/jpg/01/97/83/69/1000_F_197836949_QTkBYuzNy97g8VmBdUCs12TQLcD2Udtl.jpg -O p10.jpg

a=cv2.imread("/content/p10.jpg")
a

img=cv2.imread("/content/p10.jpg")
cv2_imshow(img)

!wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

img=cv2.imread("/p10.jpg")
faces=cv2.CascadeClassifier("/content/haarcascade_frontalface_default.xml")
f=faces.detectMultiScale(img,1.12,5)
#cv2_imshow(img)
for(x,y,w,h) in f:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2_imshow(img)

!wget https://t3.ftcdn.net/jpg/06/56/01/70/360_F_656017050_HS7zv9aP1SIw1oDXm9FlyN0GfGK83XuU.jpg -O p11.jpg

img=cv2.imread("/p11.jpg")
cv2_imshow(img)

!wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_smile.xml

img=cv2.imread("/p11.jpg")
smile=cv2.CascadeClassifier("/content/haarcascade_smile.xml")
s=smile.detectMultiScale(img,1.9,6)
#cv2_imshow(img)
for(x,y,w,h) in s:
    cv2.rectangle(img,(x,y),(x+w,y+h),(128,0,255),2)
cv2_imshow(img)

!wget https://i.pinimg.com/564x/e8/d6/f9/e8d6f9e2114fdead8f1e1e69a25ab439.jpg -O p12.jpg

img=cv2.imread("/p12.jpg")
cv2_imshow(img)

!wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml

img=cv2.imread("/p12.jpg")
eye=cv2.CascadeClassifier("/content/haarcascade_eye.xml")
e=eye.detectMultiScale(img,2.2,4)
#cv2_imshow(img)
for(x,y,w,h) in e:
    cv2.rectangle(img,(x,y),(x+w,y+h),(128,255,0),2)
cv2_imshow(img)

!wget https://previews.123rf.com/images/prometeus/prometeus1801/prometeus180100437/93394480-two-pretty-girls-in-glasses-are-posing-in-studio-over-blue-background-beauty-fashion-optics-eyewear.jpg -O p21.jpg

