'''
2. For each category, calculate the average profit per order and total profit margin 
  (profit as a percentage of Amount). 
'''
import pandas as pd

category_sales=pd.read_csv("..\\category_sales.csv")
df_merged=pd.read_csv("..\\df_merged.csv")
# I was getting unicode escape error for the above two lines because python
# because Python interprets \U as the start of a Unicode escape sequence.
# So I replaced \ with \\ and it worked. 

# Average Profit per order in each category
category_profit = df_merged.groupby("Category")["Profit"].agg(["sum", "mean"]).reset_index()
category_profit.columns = ["Category", "Total Profit", "Avg Profit per Order"]


#Total Profit Margin in each category
category_profit = pd.merge(category_profit, category_sales, on="Category")
category_profit["Profit Margin (%)"] = (category_profit["Total Profit"] / category_profit["Total Sales"]) * 100

print(category_profit)

category_profit.to_csv("category_profit.csv", index=False)


