'''
1. Merge the List of Orders and Order Details datasets on the basis of Order ID. 
   Calculate the total sales (Amount) for each category across all orders. 
'''
import pandas as pd

orders=pd.read_csv("..\\Excel_Files\\List_of_Orders_55FFC79CF8.csv")
details = pd.read_csv("..\\Excel_Files\\Order_Details_19795F61CF.csv")
# I was getting unicode escape error for the above two lines because python
# because Python interprets \U as the start of a Unicode escape sequence.
# So I replaced \ with \\ and it worked. 

 # Merging the two lists
df_merged=pd.merge(details,orders,on="Order ID")    
print("Merged data:")
print(df_merged)


# Calculating the total sales (Amount)
category_sales = df_merged.groupby("Category")["Amount"].sum().reset_index()
category_sales.columns = ["Category", "Total Sales"]
print("Total sales (Amount) for each category")
print(category_sales)

df_merged.to_csv("df_merged.csv", index=False)
category_sales.to_csv("category_sales.csv", index=False)


