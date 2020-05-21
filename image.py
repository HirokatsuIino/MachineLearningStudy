# using
# pip install opencv-python
# python image.py
# https://algorithm.joho.info/programming/python-opencv-cv2-imread/

#-*- coding:utf-8 -*-
import cv2
import numpy as np


# 画像の読み込み(RGB)
img = cv2.imread("top.jpg")

# 画像の読み込み(グレースケール)
gray = cv2.imread("top.jpg", 0)

# 画像の読み込み(RGBA)
rgba = cv2.imread("top.jpg", -1)

# 画素値の表示
print("rgb=", img)
print("\n------------------------\n")
print("gray=", gray)
print("\n------------------------\n")
print("rgba=", rgba)

