'''
3. Identify the top-performing and underperforming categories based on these 
metrics. Also, suggest reasons for their performance differences.
'''
import pandas as pd
category_profit=pd.read_csv("..\\category_profit.csv")

#sorting on the basis of Profit Margin (%)
category_profit = category_profit.sort_values(by=["Profit Margin (%)"], ascending=False)

print("Top Performing Category is ")
print(category_profit.head(1))

print("\n")

print("Under Performing Category is")
print(category_profit.tail(1))