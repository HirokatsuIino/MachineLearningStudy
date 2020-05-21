# using
# pip install pandas
# pip install matplotlib

#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# 各種データファイル読み込み -S
Investing = pd.read_csv('Investing.com2.csv')
print('Investing-----------S')
print(Investing)

# 各種データファイル読み込み -E

# 表示列調整
print('Investing-----------S')
print(Investing[["data", "end"]])


# 散布図で表示
plt.scatter(Investing["data"],
         Investing["end"]
            )
plt.title("scatter data vqs end")
plt.xlabel("data")
plt.ylabel("end")

# 凡例の表示
# plt.legend()

# プロット表示(設定の反映)
plt.show()
