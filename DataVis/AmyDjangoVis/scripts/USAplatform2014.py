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
save_loc = "./datavis/templates/datavis/USA/platform/usap14_plot.html"
#create dataframe
vg_df = pd.read_csv('scripts/sales.csv', usecols=['Year', 'Platform', 'NA_Sales_Million'])

###
dfDS2014 = vg_df[(vg_df.Platform == 'DS') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
df3DS2014 = vg_df[(vg_df.Platform == '3DS') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfWii2014 = vg_df[(vg_df.Platform == 'Wii') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfWiiU2014 = vg_df[(vg_df.Platform == 'WiiU') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfPSP2014 = vg_df[(vg_df.Platform == 'PSP') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfPSV2014 = vg_df[(vg_df.Platform == 'PSV') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfPS22014 = vg_df[(vg_df.Platform == 'PS2') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfPS32014 = vg_df[(vg_df.Platform == 'PS3') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfPS42014 = vg_df[(vg_df.Platform == 'PS4') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfx3602014 = vg_df[(vg_df.Platform == 'X360') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfxbone2014 = vg_df[(vg_df.Platform == 'XOne') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]
dfPC2014 = vg_df[(vg_df.Platform == 'PC') & (vg_df.Year == 2014) & (vg_df.NA_Sales_Million > 0)]

#ds
DS2014Count = dfDS2014['Platform']
DS2014Sales = dfDS2014['NA_Sales_Million']

#3ds
n3DS2014Count = df3DS2014['Platform']
n3DS2014Sales = df3DS2014['NA_Sales_Million']

#wii
Wii2014Count = dfWii2014['Platform']
Wii2014Sales = dfWii2014['NA_Sales_Million']

#wiiu
WiiU2014Count = dfWiiU2014['Platform']
WiiU2014Sales = dfWiiU2014['NA_Sales_Million']

#psp
PSP2014Count = dfPSP2014['Platform']
PSP2014Sales = dfPSP2014['NA_Sales_Million']

#psv
PSV2014Count = dfPSV2014['Platform']
PSV2014Sales = dfPSV2014['NA_Sales_Million']

#ps2
PS22014Count = dfPS22014['Platform']
PS22014Sales = dfPS22014['NA_Sales_Million']

#ps3
PS32014Count = dfPS32014['Platform']
PS32014Sales = dfPS32014['NA_Sales_Million']

#ps4
PS42014Count = dfPS42014['Platform']
PS42014Sales = dfPS42014['NA_Sales_Million']

#xbox 360
x3602014Count = dfx3602014['Platform']
x3602014Sales = dfx3602014['NA_Sales_Million']

#xbox one
xbone2014Count = dfxbone2014['Platform']
xbone2014Sales = dfxbone2014['NA_Sales_Million']

#pc
PC2014Count = dfPC2014['Platform']
PC2014Sales = dfPC2014['NA_Sales_Million']

# Data to plot
genre2014 = [DS2014Count.sum(), n3DS2014Count.sum(), Wii2014Count.sum(), WiiU2014Count.sum(), PSP2014Count.sum(), PSV2014Count.sum(), PS22014Count.sum(), PS32014Count.sum(), PS42014Count.sum(), x3602014Count.sum(), xbone2014Count.sum(), PC2014Count.sum()]
sales2014 = [(round(DS2014Sales.sum(), 3)), (round(n3DS2014Sales.sum(), 3)), (round(Wii2014Sales.sum(), 3)), (round(WiiU2014Sales.sum(), 3)), (round(PSP2014Sales.sum(), 3)), (round(PSV2014Sales.sum(), 3)), (round(PS22014Sales.sum(), 3)), (round(PS32014Sales.sum(), 3)), (round(PS42014Sales.sum(), 3)), (round(x3602014Sales.sum(), 3)), (round(xbone2014Sales.sum(), 3)), (round(PC2014Sales.sum(), 3))]
labels = ['DS', '3DS', 'Wii', 'Wii U', 'PSP', 'PSV', 'PS2', 'PS3', 'PS4', 'Xbox 360', 'Xbox One', 'PC']
#get values and use them, set the title of the pie.
fig = px.bar(x=labels, y=sales2014, title='2014 American Platform sales')
# remove the background colour
fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="Green", legend_bgcolor="white", font_color="green", xaxis_title='Platform', yaxis_title='Sales in million',)
#save to html file
fig.write_html(save_loc)