# using
# pip install pandas
# python number.py
# costomer_master.head()=            日付け       終値       始値       高値       安値      出来高    前日比%
# 0  2020年05月20日  9,753.4  9,773.0  9,829.3  9,684.3  936.41K  -0.20%
# 1  2020年05月19日  9,773.3  9,730.8  9,883.9  9,498.7    1.16M   0.44%
# 2  2020年05月18日  9,730.7  9,678.4  9,930.2  9,524.4    1.18M   0.55%
# 3  2020年05月17日  9,677.7  9,376.6  9,866.0  9,327.8    1.18M   3.18%
# 4  2020年05月16日  9,379.5  9,318.1  9,579.0  9,233.0    1.10M   0.66%

# pip install matplotlib

#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

costomer_master = pd.read_csv('Investing.com2.csv', index_col=0)
print('costomer_master-----------S')
print(costomer_master)

# costomer_master.head()
# print('costomer_master.head()=', costomer_master.head(0))
# print('costomer_master.head()=', costomer_master[日付け])
# print('costomer_master.head()=', costomer_master.plot([日付け]).head())

# plt.plot(costomer_master.head())
