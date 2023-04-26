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

save_loc = "./datavis/templates/datavis/global/globalplatform/pf12_plot.html"


#create dataframe
vg_df = pd.read_csv('scripts/sales.csv', usecols=['Year', 'Platform', 'Global_Sales_Million'])

#       Dataframes
dfDS2012 = vg_df[(vg_df.Platform == 'DS') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
df3DS2012 = vg_df[(vg_df.Platform == '3DS') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfWii2012 = vg_df[(vg_df.Platform == 'Wii') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfWiiU2012 = vg_df[(vg_df.Platform == 'WiiU') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfPSP2012 = vg_df[(vg_df.Platform == 'PSP') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfPSV2012 = vg_df[(vg_df.Platform == 'PSV') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfPS22012 = vg_df[(vg_df.Platform == 'PS2') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfPS32012 = vg_df[(vg_df.Platform == 'PS3') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfx3602012 = vg_df[(vg_df.Platform == 'X360') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]
dfPC2012 = vg_df[(vg_df.Platform == 'PC') & (vg_df.Year == 2012) & (vg_df.Global_Sales_Million > 0)]

#   Variables

#   ds
DS2012Count = dfDS2012['Platform']
DS2012Sales = dfDS2012['Global_Sales_Million']
#   3ds
n3DS2012Count = df3DS2012['Platform']
n3DS2012Sales = df3DS2012['Global_Sales_Million']
#   wii
Wii2012Count = dfWii2012['Platform']
Wii2012Sales = dfWii2012['Global_Sales_Million']
#   wiiu
WiiU2012Count = dfWiiU2012['Platform']
WiiU2012Sales = dfWiiU2012['Global_Sales_Million']
#   psp
PSP2012Count = dfPSP2012['Platform']
PSP2012Sales = dfPSP2012['Global_Sales_Million']
#   psv
PSV2012Count = dfPSV2012['Platform']
PSV2012Sales = dfPSV2012['Global_Sales_Million']
#   ps2
PS22012Count = dfPS22012['Platform']
PS22012Sales = dfPS22012['Global_Sales_Million']
#   ps3
PS32012Count = dfPS32012['Platform']
PS32012Sales = dfPS32012['Global_Sales_Million']
#   xbox 360
x3602012Count = dfx3602012['Platform']
x3602012Sales = dfx3602012['Global_Sales_Million']
#   pc
PC2012Count = dfPC2012['Platform']
PC2012Sales = dfPC2012['Global_Sales_Million']

# Data to plot
genre2012 = [DS2012Count.sum(), n3DS2012Count.sum(), Wii2012Count.sum(), PSP2012Count.sum(), PS22012Count.sum(), PS32012Count.sum(), x3602012Count.sum(), PC2012Count.sum()]
sales2012 = [(round(DS2012Sales.sum(), 3)), (round(n3DS2012Sales.sum(), 3)), (round(Wii2012Sales.sum(), 3)), (round(PSP2012Sales.sum(), 3)), (round(PS22012Sales.sum(), 3)), (round(PS32012Sales.sum(), 3)), (round(x3602012Sales.sum(), 3)), (round(PC2012Sales.sum(), 3))]
labels = ['DS', '3DS', 'Wii', 'PSP', 'PS2', 'PS3', 'Xbox 360', 'PC']
#get values and use them, set the title of the pie.
fig = px.bar(x=labels, y=sales2012, title='2012 Global Platform sales')
# remove the background colour
fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="Green", legend_bgcolor="white", font_color="green", xaxis_title='Platform', yaxis_title='Sales in million',)
#save to html file
fig.write_html(save_loc)