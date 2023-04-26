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


#set save location for the html file so it can be displayed on django
save_loc = "./datavis/templates/datavis/japan/platform/jpp15_plot.html"

#create dataframe
vg_df = pd.read_csv('scripts/sales.csv', usecols=['Year', 'Platform', 'JP_Sales_Million'])

df3DS2015 = vg_df[(vg_df.Platform == '3DS') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfWii2015 = vg_df[(vg_df.Platform == 'Wii') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfWiiU2015 = vg_df[(vg_df.Platform == 'WiiU') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfPSV2015 = vg_df[(vg_df.Platform == 'PSV') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfPS32015 = vg_df[(vg_df.Platform == 'PS3') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfPS42015 = vg_df[(vg_df.Platform == 'PS4') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfx3602015 = vg_df[(vg_df.Platform == 'X360') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfxbone2015 = vg_df[(vg_df.Platform == 'XOne') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]
dfPC2015 = vg_df[(vg_df.Platform == 'PC') & (vg_df.Year == 2015) & (vg_df.JP_Sales_Million > 0)]

# 3ds 
n3DS2015Count = df3DS2015['Platform']
n3DS2015Sales = df3DS2015['JP_Sales_Million']
# wii 
Wii2015Count = dfWii2015['Platform']
Wii2015Sales = dfWii2015['JP_Sales_Million']
# wii u
WiiU2015Count = dfWiiU2015['Platform']
WiiU2015Sales = dfWiiU2015['JP_Sales_Million']
# psv 
PSV2015Count = dfPSV2015['Platform']
PSV2015Sales = dfPSV2015['JP_Sales_Million']
# ps3 
PS32015Count = dfPS32015['Platform']
PS32015Sales = dfPS32015['JP_Sales_Million']
# ps4
PS42015Count = dfPS42015['Platform']
PS42015Sales = dfPS42015['JP_Sales_Million']
# x360 
x3602015Count = dfx3602015['Platform']
x3602015Sales = dfx3602015['JP_Sales_Million']
# xOne 
xbone2015Count = dfxbone2015['Platform']
xbone2015Sales = dfxbone2015['JP_Sales_Million']
# pc 
PC2015Count = dfPC2015['Platform']
PC2015Sales = dfPC2015['JP_Sales_Million']

# Data to plot
genre2015 = [n3DS2015Count.sum(), Wii2015Count.sum(), WiiU2015Count.sum(), PSV2015Count.sum(), PS32015Count.sum(), PS42015Count.sum(), x3602015Count.sum(), xbone2015Count.sum(), PC2015Count.sum()]
sales2015 = [(round(n3DS2015Sales.sum(), 3)), (round(Wii2015Sales.sum(), 3)), (round(WiiU2015Sales.sum(), 3)), (round(PSV2015Sales.sum(), 3)), (round(PS32015Sales.sum(), 3)), (round(PS42015Sales.sum(), 3)), (round(x3602015Sales.sum(), 3)), (round(xbone2015Sales.sum(), 3)), (round(PC2015Sales.sum(), 3))]
labels = ['3DS', 'Wii', 'Wii U', 'PSV', 'PS3', 'PS4', 'Xbox 360', 'Xbox One', 'PC']
#get values and use them, set the title of the pie.
fig = px.bar(x=labels, y=sales2015, title='2015 Japan Platform sales')
# remove the background colour
fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="Green", legend_bgcolor="white", font_color="green", xaxis_title='Platform', yaxis_title='Sales in million',)
#save to html file
fig.write_html(save_loc)