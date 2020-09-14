import pandas as pd
import numpy as np
import plotly.express as px

theft_df = pd.read_csv('./Bicycle_Theft.csv')

cost_sum = theft_df['Bicycle_Value'].sum()  # 3678514.0

total_thefts = theft_df['ID'].count()  # 5652

px.set_mapbox_access_token("pk.eyJ1IjoidmxhZGpkayIsImEiOiJja2YydWRiN2YwMjV6MnVydjd5NzQzdXJ2In0.FK1eN7UGZkrHj7qTdz_sBA")
fig = px.scatter_mapbox(theft_df, lat="y", lon="x",
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
fig.show()
