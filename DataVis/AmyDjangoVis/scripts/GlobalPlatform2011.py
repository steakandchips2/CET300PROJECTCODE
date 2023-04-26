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
import plotly.offline as pyo
# from django.shortcuts import render

#set save location for the html file so it can be displayed on django
save_loc = "./datavis/templates/datavis/global/globalplatform/pf11_plot.html"


#create dataframe
vg_df = pd.read_csv('scripts/sales.csv', usecols=['Year', 'Platform', 'Global_Sales_Million'])

#       2011 Dataframes
dfDS2011 = vg_df[(vg_df.Platform == 'DS') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
df3DS2011 = vg_df[(vg_df.Platform == '3DS') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
dfWii2011 = vg_df[(vg_df.Platform == 'Wii') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
dfPSP2011 = vg_df[(vg_df.Platform == 'PSP') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
dfPS22011 = vg_df[(vg_df.Platform == 'PS2') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
dfPS32011 = vg_df[(vg_df.Platform == 'PS3') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
dfPS42011 = vg_df[(vg_df.Platform == 'PS4') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
dfx3602011 = vg_df[(vg_df.Platform == 'X360') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]
dfPC2011 = vg_df[(vg_df.Platform == 'PC') & (vg_df.Year == 2011) & (vg_df.Global_Sales_Million > 0)]

# DS
DS2011Count = dfDS2011['Platform']
DS2011Sales = dfDS2011['Global_Sales_Million']
# 3DS
n3DS2011Count = df3DS2011['Platform']
n3DS2011Sales = df3DS2011['Global_Sales_Million']
# Wii
Wii2011Count = dfWii2011['Platform']
Wii2011Sales = dfWii2011['Global_Sales_Million']
# PSP
PSP2011Count = dfPSP2011['Platform']
PSP2011Sales = dfPSP2011['Global_Sales_Million']
# PS2
PS22011Count = dfPS22011['Platform']
PS22011Sales = dfPS22011['Global_Sales_Million']
# PS3
PS32011Count = dfPS32011['Platform']
PS32011Sales = dfPS32011['Global_Sales_Million']
# Xbox 360
x3602011Count = dfx3602011['Platform']
x3602011Sales = dfx3602011['Global_Sales_Million']
# PC
PC2011Count = dfPC2011['Platform']
PC2011Sales = dfPC2011['Global_Sales_Million']

# Data to plot
genre2011 = [DS2011Count.sum(), n3DS2011Count.sum(), Wii2011Count.sum(), PSP2011Count.sum(), PS22011Count.sum(), PS32011Count.sum(), x3602011Count.sum(), PC2011Count.sum()]
sales2011 = [(round(DS2011Sales.sum(), 3)), (round(n3DS2011Sales.sum(), 3)), (round(Wii2011Sales.sum(), 3)), (round(PSP2011Sales.sum(), 3)), (round(PS22011Sales.sum(), 3)), (round(PS32011Sales.sum(), 3)), (round(x3602011Sales.sum(), 3)), (round(PC2011Sales.sum(), 3))]
labels = ['DS', '3DS', 'Wii', 'PSP', 'PS2', 'PS3', 'Xbox 360', 'PC']
#get values and use them, set the title of the pie.
fig = px.bar(x=labels, y=sales2011, title='2011 Global Platform sales')
# remove the background colour
fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="Green", legend_bgcolor="white", font_color="green", xaxis_title='Platform', yaxis_title='Sales in million',)
#save to html file
fig.write_html(save_loc)