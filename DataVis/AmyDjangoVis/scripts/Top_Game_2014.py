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


#set save location for html file
save_loc = "./datavis/templates/datavis/global/topgames/topg16_plot.html"
#create dataframe from csv
vg_df = pd.read_csv("scripts/sales.csv",delimiter =",")

#Filtering the dataframe to include only rows where the Year is correct
action_2014 = vg_df[(vg_df['Year'] == 2014)]
#Identifying the top game based on global sales:
top_game_index = action_2014['Global_Sales_Million'].idxmax()
top_game = action_2014.loc[top_game_index]
#get sales data for the top game in region
region_sales = top_game[['NA_Sales_Million', 'EU_Sales_Million', 'JP_Sales_Million', 'Other_Sales_Million']]

#scatter plot
# find name of top game and add it into the title
fig = px.scatter(x=['USA', 'Europe', 'Japan', 'Other Regions'], y=region_sales, title="Regional sales for top game of 2014: " + top_game['Name'])
#add axis labels
fig.update_layout(xaxis_title='Region', yaxis_title='Sales (in millions)')
#remove background set text colour
fig.update_layout(
    paper_bgcolor="rgba(0, 0, 0, 0)", title_font_color="green", legend_bgcolor="white",  font_color="green", xaxis_title='Region', yaxis_title='Sales in million',)
#change plot colour
fig.update_traces(mode='markers', marker=dict(size=15, color='red'))
#save to html file
fig.write_html(save_loc)