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
save_loc = "./datavis/templates/datavis/europe/platform/eup16_plot.html"

#create dataframe
vg_df = pd.read_csv('scripts/sales.csv', usecols=['Year', 'Platform', 'EU_Sales_Million'])
##       Dataframes for all consoles out and making sales in the year.       ##
df3DS2016 = vg_df[(vg_df.Platform == '3DS') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfWii2016 = vg_df[(vg_df.Platform == 'Wii') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfWiiU2016 = vg_df[(vg_df.Platform == 'WiiU') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfPSV2016 = vg_df[(vg_df.Platform == 'PSV') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfPS32016 = vg_df[(vg_df.Platform == 'PS3') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfPS42016 = vg_df[(vg_df.Platform == 'PS4') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfx3602016 = vg_df[(vg_df.Platform == 'X360') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfxbone2016 = vg_df[(vg_df.Platform == 'XOne') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]
dfPC2016 = vg_df[(vg_df.Platform == 'PC') & (vg_df.Year == 2016) & (vg_df.EU_Sales_Million > 0)]

# 3ds 
n3DS2016Count = df3DS2016['Platform']
n3DS2016Sales = df3DS2016['EU_Sales_Million']
# wii 
Wii2016Count = dfWii2016['Platform']
Wii2016Sales = dfWii2016['EU_Sales_Million']
# wii u
WiiU2016Count = dfWiiU2016['Platform']
WiiU2016Sales = dfWiiU2016['EU_Sales_Million']
# psv 
PSV2016Count = dfPSV2016['Platform']
PSV2016Sales = dfPSV2016['EU_Sales_Million']
# ps3 
PS32016Count = dfPS32016['Platform']
PS32016Sales = dfPS32016['EU_Sales_Million']
# ps4 
PS42016Count = dfPS42016['Platform']
PS42016Sales = dfPS42016['EU_Sales_Million']
# x360 
x3602016Count = dfx3602016['Platform']
x3602016Sales = dfx3602016['EU_Sales_Million']
# xOne 
xbone2016Count = dfxbone2016['Platform']
xbone2016Sales = dfxbone2016['EU_Sales_Million']
# pc 
PC2016Count = dfPC2016['Platform']
PC2016Sales = dfPC2016['EU_Sales_Million']


# Data to plot
genre2016 = [n3DS2016Count.sum(), Wii2016Count.sum(), WiiU2016Count.sum(), PSV2016Count.sum(), PS32016Count.sum(), PS42016Count.sum(), x3602016Count.sum(), xbone2016Count.sum(), PC2016Count.sum()]
sales2016 = [(round(n3DS2016Sales.sum(), 3)), (round(Wii2016Sales.sum(), 3)), (round(WiiU2016Sales.sum(), 3)), (round(PSV2016Sales.sum(), 3)), (round(PS32016Sales.sum(), 3)), (round(PS42016Sales.sum(), 3)), (round(x3602016Sales.sum(), 3)), (round(xbone2016Sales.sum(), 3)), (round(PC2016Sales.sum(), 3))]
#get values and use them, set the title of the pie.
labels = ['3DS', 'Wii', 'Wii U', 'PSV', 'PS3', 'PS4', 'Xbox 360', 'Xbox One', 'PC']
fig = px.bar(x=labels, y=sales2016, title='2016 Europe Platform sales')
# remove the background colour
fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="Green", legend_bgcolor="white", font_color="green", xaxis_title='Platform', yaxis_title='Sales in million',)
#save to html file
fig.write_html(save_loc)