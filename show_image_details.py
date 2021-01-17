#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:19:17 2020

@author: lion
"""

from PIL import Image 
import cv2
import numpy as np
image = "../dataset/4.jpg"
cv2.waitKey(0)
img = Image.open(image)
print("{}" .format(img.format))
print("size: {}" .format(img.size))
print("image mode: {}".format(img.mode))

