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
save_loc = "./datavis/templates/datavis/USA/platform/usap10_plot.html"
#create dataframe
vg_df = pd.read_csv('scripts/sales.csv', usecols=['Year', 'Platform', 'NA_Sales_Million'])

##       Dataframes for all consoles out and making sales in the year.       ##

#       2010        
dfDS2010 = vg_df[(vg_df.Platform == 'DS') & (vg_df.Year == 2010) & (vg_df.NA_Sales_Million > 0)]
dfWii2010 = vg_df[(vg_df.Platform == 'Wii') & (vg_df.Year == 2010) & (vg_df.NA_Sales_Million > 0)]
dfPSP2010 = vg_df[(vg_df.Platform == 'PSP') & (vg_df.Year == 2010) & (vg_df.NA_Sales_Million > 0)]
dfPS22010 = vg_df[(vg_df.Platform == 'PS2') & (vg_df.Year == 2010) & (vg_df.NA_Sales_Million > 0)]
dfPS32010 = vg_df[(vg_df.Platform == 'PS3') & (vg_df.Year == 2010) & (vg_df.NA_Sales_Million > 0)]
dfx3602010 = vg_df[(vg_df.Platform == 'X360') & (vg_df.Year == 2010) & (vg_df.NA_Sales_Million > 0)]
dfPC2010 = vg_df[(vg_df.Platform == 'PC') & (vg_df.Year == 2010) & (vg_df.NA_Sales_Million > 0)]

##      This is the variables that add up the total sales and sum of each copnsoles releases


########################
#####     DS 2004 - 2014
########################
#2010
DS2010Count = dfDS2010['Platform']
DS2010Sales = dfDS2010['NA_Sales_Million']

########################
####     WII 2006 - 2020
########################
#2010
Wii2010Count = dfWii2010['Platform']
Wii2010Sales = dfWii2010['NA_Sales_Million']

########################
####     PSP 2005 - 2014
########################
#2010
PSP2010Count = dfPSP2010['Platform']
PSP2010Sales = dfPSP2010['NA_Sales_Million']

########################
####     PS2 2000 - 2014 
########################
#2010
PS22010Count = dfPS22010['Platform']
PS22010Sales = dfPS22010['NA_Sales_Million']

########################
####     PS3 2006 - 2020 
########################
#2010
PS32010Count = dfPS32010['Platform']
PS32010Sales = dfPS32010['NA_Sales_Million']

########################
####    x360 2005 - 2019
########################
#2010
x3602010Count = dfx3602010['Platform']
x3602010Sales = dfx3602010['NA_Sales_Million']

########################
####          PC forever
########################
#2010
PC2010Count = dfPC2010['Platform']
PC2010Sales = dfPC2010['NA_Sales_Million']

# Data to plot
genre2010 = [DS2010Count.sum(), Wii2010Count.sum(), PSP2010Count.sum(), PS22010Count.sum(), PS32010Count.sum(), x3602010Count.sum(), PC2010Count.sum()]
sales2010 = [(round(DS2010Sales.sum(), 3)), (round(Wii2010Sales.sum(), 3)), (round(PSP2010Sales.sum(), 3)), (round(PS22010Sales.sum(), 3)), (round(PS32010Sales.sum(), 3)), (round(x3602010Sales.sum(), 3)), (round(PC2010Sales.sum(), 3))]
labels = ['DS', 'Wii', 'PSP', 'PS2', 'PS3', 'Xbox 360', 'PC']
#get values and use them, set the title of the pie.
fig = px.bar(x=labels, y=sales2010, title='2010 American Platform sales')
# remove the background colour
fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="Green", legend_bgcolor="white", font_color="green", xaxis_title='Platform', yaxis_title='Sales in million',)
#save to html file
fig.write_html(save_loc)