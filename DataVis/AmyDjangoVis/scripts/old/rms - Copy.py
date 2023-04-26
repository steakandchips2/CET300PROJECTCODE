# Import packages
from asyncio.windows_events import NULL
from locale import currency
import string
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly
import json
#import plotly.offline as pyo

sales_df = pd.read_csv('scripts/sales.csv', usecols=['NA_Sales_Million', 'JP_Sales_Million', 'EU_Sales_Million', 'Other_Sales_Million'])
#print(sales_df)

# NA TOTAL SALES TO 2 DEC PLACES
NA_Total = sales_df['NA_Sales_Million'].sum()
#print(round(NA_Total, 3))

#  JP TOTAL SALES TO 2 DEC
JP_Total = sales_df['JP_Sales_Million'].sum()
#print(round(JP_Total, 3))

#  EU TOTAL 2 DEC
EU_Total = sales_df['EU_Sales_Million'].sum()
# print(round(EU_Total, 3))

#  OTHER TOTAL 2 DEC
Other_Total = sales_df['Other_Sales_Million'].sum()
# print(round(Other_Total, 3))

# # PIE CHART WITH % FOR REGIONAL SALES IN MILLIONS
# df = pd.DataFrame({'Regional Sales in million units': }, index=)
# plot = df.plot.pie(y='Regional Sales in million units', figsize=(7,5), autopct='%.2f')
# plt.show()

#2010 GRAPH
# sales = [round(NA_Total, 3), round(JP_Total, 3), round(EU_Total, 3), round(Other_Total, 3)]
# labels = ['North America', 'Japan', 'Europe', 'Other']
# fig = px.pie(values=sales, names=labels, title="Regional Sales in million units - All Time", )
# fig.update_layout(xaxis_title='Region', yaxis_title='Sales in million')
# pyo.plot(fig, auto_open=True)### delete when putting on django
# plot_json = fig.to_json()

sales = [round(NA_Total, 3), round(JP_Total, 3), round(EU_Total, 3), round(Other_Total, 3)]
labels = ['North America', 'Japan', 'Europe', 'Other']
fig = px.pie(values=sales, names=labels, title="Regional Sales in million units - All Time", hole=0.4)
fig.update_layout(xaxis_title='Region', yaxis_title='Sales in million')
plot_json = fig.to_json()
