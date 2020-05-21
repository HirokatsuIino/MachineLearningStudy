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

# 各種データファイル読み込み -S
item_master = pd.read_csv('sample_20200325/1章/item_master.csv', index_col=0)
print('item_master-----------S')
print(item_master)

transaction_1 = pd.read_csv('sample_20200325/1章/transaction_1.csv')
print('transaction_1-----------S')
print(transaction_1)

transaction_2 = pd.read_csv('sample_20200325/1章/transaction_2.csv')
print('transaction_2-----------S')
print(transaction_2)

transaction_detail_1 = pd.read_csv('sample_20200325/1章/transaction_detail_1.csv')
print('transaction_detail_1-----------S')
print(transaction_detail_1)

customer_master = pd.read_csv('sample_20200325/1章/customer_master.csv')
print('customer_master-----------S')
print(customer_master)

# 各種データファイル読み込み -E

# 表示列調整
print('customer_master=', customer_master[["customer_id", "customer_name"]])



# データ結合
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
print('transaction-----------S')
print(transaction)


# mergeでデータ結合
# 結合先 transaction_detail_1
# 結合データ transaction
# 結合先で表示するデータ transaction の "transaction_id", "payment_date", "customer_id"
# 結合条件 transaction_id
join_data = pd.merge(
    transaction_detail_1,
    transaction[
        ["transaction_id", "payment_date", "customer_id"]],
    on="transaction_id",
    how="left"
)

print('join_data=', join_data)


# mergeでデータ結合
# 結合先 join_data
# 結合データ customer_master
# 結合条件 customer_id
join_data = pd.merge(
    join_data,
    customer_master,
    on="customer_id",
    how="left"
)

print('join_data=', join_data)

# mergeでデータ結合
# 結合先 join_data
# 結合データ item_master
# 結合条件 customer_id
join_data = pd.merge(
    join_data,
    item_master,
    on="item_id",
    how="left"
)

print('join_data=', join_data)
# print('join_data=', join_data["detail_id"])
print('join_data=', join_data["item_price"].sum())

# 表示列調整
print('join_data2=', join_data[["transaction_id", "age"]])

# 散布図で表示
plt.scatter(join_data["birth"],
         join_data["age"],
         label='age')

# 折れ線グラフで表示
# plt.plot(join_data["transaction_id"],
#          join_data["age"],
#          label='age')

# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.show()

# costomer_master.head()
# print('costomer_master.head()=', costomer_master.head(0))
# print('costomer_master.head()=', costomer_master[日付け])
# print('costomer_master.head()=', costomer_master.plot([日付け]).head())

# plt.plot(costomer_master.head())
