#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:19:17 2020

@author: lion
"""


import time
from PIL import Image  
from natsort import natsorted
import glob
from datetime import datetime
#image = cv2.imread("dataset/ezgif-frame-001.jpg")

#im = Image.open(image)
#give the size of the you want. you can also ignore and remove it and next line


img_list= []
resized_img= []
for filename in natsorted(glob.glob("dataset/*.jpg")):
    print(filename)
    #time.sleep(1)

    img = Image.open(filename)
    img_list.append(img)
    width, height = img.size
    left = 200
    top = 300
    right = 1200
    bottom = 750
    
    cropp = img.crop((left, top, right, bottom))
    resized_img.append(cropp)
    #cropp.show()
    print("{}".format(cropp.format))
    print("size: {}".format(cropp.size))
    print("image mode: {}".format(cropp.mode))
for (i, new) in enumerate(resized_img):
    new.save("{}{}{}".format("cropped/aircraft",i+1,".jpg"))
