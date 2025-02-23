'''
1. From the List of Orders dataset, identify the top 5 states with the highest order 
count. For each of these states, calculate the total sales and average profit. 
'''
import pandas as pd
orders=pd.read_csv("..\\Excel_Files\\List_of_Orders_55FFC79CF8.csv")
details = pd.read_csv("..\\Excel_Files\\Order_Details_19795F61CF.csv")

# Identify top 5 states with the highest order count
top_states = orders["State"].value_counts().head(5).index.tolist()
print("Top 5 states with the highest order count is:\n")
print(top_states)


# Filter orders for top states
top_states_orders = orders[orders["State"].isin(top_states)]

# Merge with order details
top_states_merged = pd.merge(top_states_orders, details, on="Order ID")

# Calculate total sales and average profit per state
state_performance = top_states_merged.groupby("State").agg(
    Total_Sales=("Amount", "sum"),
    Avg_Profit=("Profit", "mean")
).reset_index()


print("\n")

print("Regional Performance Insights:\n")
print(state_performance)

state_performance.to_csv("state_performance.csv",index=False)