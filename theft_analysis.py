import pandas as pd

theft_df = pd.read_csv('./Bicycle_Theft.csv')

cost_sum = theft_df['Bicycle_value'].sum() # 3678514.0

total_thefts = theft_df['ID'].count() # 5652
