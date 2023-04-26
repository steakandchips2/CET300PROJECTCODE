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
save_loc = "./datavis/templates/datavis/USA/platform/usap13_plot.html"
#create dataframe
vg_df = pd.read_csv('scripts/sales.csv', usecols=['Year', 'Platform', 'NA_Sales_Million'])

#dataframe 2013
dfDS2013 = vg_df[(vg_df.Platform == 'DS') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
df3DS2013 = vg_df[(vg_df.Platform == '3DS') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfWii2013 = vg_df[(vg_df.Platform == 'Wii') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfWiiU2013 = vg_df[(vg_df.Platform == 'WiiU') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfPSP2013 = vg_df[(vg_df.Platform == 'PSP') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfPSV2013 = vg_df[(vg_df.Platform == 'PSV') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfPS22013 = vg_df[(vg_df.Platform == 'PS2') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfPS32013 = vg_df[(vg_df.Platform == 'PS3') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfPS42013 = vg_df[(vg_df.Platform == 'PS4') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfx3602013 = vg_df[(vg_df.Platform == 'X360') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfxbone2013 = vg_df[(vg_df.Platform == 'XOne') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]
dfPC2013 = vg_df[(vg_df.Platform == 'PC') & (vg_df.Year == 2013) & (vg_df.NA_Sales_Million > 0)]

#   ds
DS2013Count = dfDS2013['Platform']
DS2013Sales = dfDS2013['NA_Sales_Million']
#   3ds
n3DS2013Count = df3DS2013['Platform']
n3DS2013Sales = df3DS2013['NA_Sales_Million']
#   wii
Wii2013Count = dfWii2013['Platform']
Wii2013Sales = dfWii2013['NA_Sales_Million']
#   wiiu
WiiU2013Count = dfWiiU2013['Platform']
WiiU2013Sales = dfWiiU2013['NA_Sales_Million']
#   psp
PSP2013Count = dfPSP2013['Platform']
PSP2013Sales = dfPSP2013['NA_Sales_Million']
#   psv
PSV2013Count = dfPSV2013['Platform']
PSV2013Sales = dfPSV2013['NA_Sales_Million']
#   ps2
PS22013Count = dfPS22013['Platform']
PS22013Sales = dfPS22013['NA_Sales_Million']
#   ps3
PS32013Count = dfPS32013['Platform']
PS32013Sales = dfPS32013['NA_Sales_Million']
#   ps4
PS42013Count = dfPS42013['Platform']
PS42013Sales = dfPS42013['NA_Sales_Million']
#   xbox 360
x3602013Count = dfx3602013['Platform']
x3602013Sales = dfx3602013['NA_Sales_Million']
#   xbox one
xbone2013Count = dfxbone2013['Platform']
xbone2013Sales = dfxbone2013['NA_Sales_Million']
#   pc
PC2013Count = dfPC2013['Platform']
PC2013Sales = dfPC2013['NA_Sales_Million']



# Data to plot
genre2013 = [DS2013Count.sum(), n3DS2013Count.sum(), Wii2013Count.sum(), WiiU2013Count.sum(), PSP2013Count.sum(), PSV2013Count.sum(), PS22013Count.sum(), PS32013Count.sum(), PS42013Count.sum(), x3602013Count.sum(), xbone2013Count.sum(), PC2013Count.sum()]
sales2013 = [(round(DS2013Sales.sum(), 3)), (round(n3DS2013Sales.sum(), 3)), (round(Wii2013Sales.sum(), 3)), (round(WiiU2013Sales.sum(), 3)), (round(PSP2013Sales.sum(), 3)), (round(PSV2013Sales.sum(), 3)), (round(PS22013Sales.sum(), 3)), (round(PS32013Sales.sum(), 3)), (round(PS42013Sales.sum(), 3)), (round(x3602013Sales.sum(), 3)), (round(xbone2013Sales.sum(), 3)), (round(PC2013Sales.sum(), 3))]
labels = ['DS', '3DS', 'Wii', 'Wii U', 'PSP', 'PSV', 'PS2', 'PS3', 'PS4', 'Xbox 360', 'Xbox One', 'PC']
#get values and use them, set the title of the pie.
fig = px.bar(x=labels, y=sales2013, title='2013 American Platform sales')
# remove the background colour
fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="Green", legend_bgcolor="white", font_color="green", xaxis_title='Platform', yaxis_title='Sales in million',)
#save to html file
fig.write_html(save_loc)