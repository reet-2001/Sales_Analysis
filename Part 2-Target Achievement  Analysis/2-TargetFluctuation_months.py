'''
2. Analyse the trends to identify months with significant target fluctuations. 
Suggest strategies for aligning target expectations with actual performance 
trends.
'''
import pandas as pd
furniture_target=pd.read_csv("..\\furniture_target.csv")

# Identify months with significant target fluctuations
significant_changes = furniture_target[furniture_target["Target Change (%)"].abs() > 1.5]
print(significant_changes)
