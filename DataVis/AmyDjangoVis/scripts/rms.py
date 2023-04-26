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
save_loc = "./datavis/templates/datavis/global/rms_plot.html"

#create dataframe - only use sales columns
sales_df = pd.read_csv('scripts/sales.csv', usecols=['NA_Sales_Million', 'JP_Sales_Million', 'EU_Sales_Million', 'Other_Sales_Million'])

#NA TOTAL SALES
NA_Total = sales_df['NA_Sales_Million'].sum()
# JP TOTAL SALES
JP_Total = sales_df['JP_Sales_Million'].sum()
# EU TOTAL
EU_Total = sales_df['EU_Sales_Million'].sum()
# OTHER TOTAL
Other_Total = sales_df['Other_Sales_Million'].sum()

# Data to plot
sales = [round(NA_Total, 3), round(JP_Total, 3), round(EU_Total, 3), round(Other_Total, 3)]
labels = ['America', 'Japan', 'Europe', 'Other']
#get values and use them, set the title of the pie.
fig = px.pie(values=sales, names=labels, title="Regional Sales in million units - All Time", hole=0.4)
# remove the background colour
fig.update_layout(
    paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="green", legend_bgcolor="white", xaxis_title='Genre', yaxis_title='Sales in million',)
#set colour and size of the % in the pie to make it clear
fig.update_traces(
    textfont=dict(
        color="black",
        size=16,
    )
)
#save to html file
fig.write_html(save_loc)