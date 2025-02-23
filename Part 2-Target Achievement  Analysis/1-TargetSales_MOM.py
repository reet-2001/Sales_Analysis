'''
1. Using the Sales Target dataset, calculate the percentage change in target sales 
   for the Furniture category month-over-month.
'''
import pandas as pd
sales_target=pd.read_csv("..\\Excel_Files\\Sales_target_DD2E9B96A0.csv")

furniture_target = sales_target[sales_target["Category"] == "Furniture"]

# Converting date column to datetime format
furniture_target["Month"] = pd.to_datetime(furniture_target["Month of Order Date"], format="%b-%y", errors="coerce")


# Sorting by month
furniture_target = furniture_target.sort_values(by="Month")

# Calculating month-over-month percentage change in target sales
furniture_target["Target Change (%)"] = furniture_target["Target"].pct_change() * 100


print(furniture_target)
furniture_target.to_csv("furniture_target.csv",index=False)
