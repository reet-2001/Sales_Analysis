'''
2. Highlight any regional disparities in sales or profitability. Suggest regions or cities 
that should be prioritized for improvement.
'''
import pandas as pd
df_merged = pd.read_csv("..\\df_merged.csv")

# State-level analysis
state_wise_analysis = df_merged.groupby("State").agg(
    Total_Sales=("Amount", "sum"),
    Average_Profit=("Profit", "mean")
).reset_index()

# City-level analysis
city_wise_analysis = df_merged.groupby(["State", "City"]).agg(
    Total_Sales=("Amount", "sum"),
    Average_Profit=("Profit", "mean")
).reset_index()

# Top 5 most profitable states
most_profitable_states = state_wise_analysis.nlargest(5, "Average_Profit")
# Top 5 least profitable states
least_profitable_states = state_wise_analysis.nsmallest(5, "Average_Profit")
# Top 5 most profitable cities
most_profitable_cities = city_wise_analysis.nlargest(5, "Average_Profit")
# Top 5 least profitable cities
least_profitable_cities = city_wise_analysis.nsmallest(5, "Average_Profit")
# Top 5 highest sales states
highest_sales_states = state_wise_analysis.nlargest(5, "Total_Sales")
# Top 5 lowest sales states
lowest_sales_states = state_wise_analysis.nsmallest(5, "Total_Sales")
# Top 5 highest sales cities
highest_sales_cities = city_wise_analysis.nlargest(5, "Total_Sales")
# Top 5 lowest sales cities
lowest_sales_cities = city_wise_analysis.nsmallest(5, "Total_Sales")


print("Disparity in terms of Profitability\n")
print("\nMost Profitable States:\n", most_profitable_states)
print("\nLeast Profitable States:\n", least_profitable_states)
print("\nMost Profitable Cities:\n", most_profitable_cities)
print("\nLeast Profitable Cities:\n", least_profitable_cities)
print("\nDisparity in terms of Total Sales\n")
print("\nHighest Sales States:\n", highest_sales_states)
print("\nLowest Sales States:\n", lowest_sales_states)
print("\nHighest Sales Cities:\n", highest_sales_cities)
print("\nLowest Sales Cities:\n", lowest_sales_cities)

state_wise_analysis.to_csv("state_wise_analysis.csv",index=False)
city_wise_analysis.to_csv("city_wise_analysis.csv",index=False)

