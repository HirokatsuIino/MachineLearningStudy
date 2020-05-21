# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 入力画像とテンプレート画像をで取得
image = "top.jpg"
image2 = "top_1.jpg"
image_sum = "top_1-2.jpg"

img = cv2.imread(image)
temp = cv2.imread(image2)

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)

# テンプレート画像の高さ・幅
h, w = temp.shape

# テンプレートマッチング（OpenCVで実装）
match = cv2.matchTemplate(gray, temp, cv2.TM_SQDIFF)
min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
pt = min_pt

# テンプレートマッチングの結果を出力
cv2.rectangle(img, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0, 0, 200), 3)
cv2.imwrite(image_sum, img)



# 画像の読み込み(グレースケール)
# img = cv2.imread(image, 0)
# temp = cv2.imread(image2, 0)
#
# # テンプレート画像の高さ・幅
# h, w = temp.shape
#
# # テンプレートマッチング（OpenCVで実装）
# match = cv2.matchTemplate(img, temp, cv2.TM_SQDIFF)
# min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
# pt = min_pt
#
# # テンプレートマッチングの結果を出力
# cv2.rectangle(img, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0, 0, 200), 3)
# cv2.imwrite(image_sum, img)

