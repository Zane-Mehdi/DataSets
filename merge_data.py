import pandas as pd
cab = pd.read_csv('Cab_Data.csv')
customers = pd.read_csv('Customer_ID.csv')
transactions = pd.read_csv('Transaction_ID.csv')
city = pd.read_csv('City.csv')

merge1 = pd.merge(cab,transactions)
merge2 = pd.merge(merge1,customers)
final_merge = pd.merge(merge2,city)

final_merge.to_csv("merged_data.csv")
