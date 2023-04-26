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
save_loc = "./datavis/templates/datavis/japan/genre/jpg14_plot.html"

#create dataframe from csv
vg_df = pd.read_csv("scripts/sales.csv",delimiter =",")
#create more specific dataframes
df2014action = vg_df[(vg_df.Genre == 'Action') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014adventure = vg_df[(vg_df.Genre == 'Adventure') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014fighting = vg_df[(vg_df.Genre == 'Fighting') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014misc = vg_df[(vg_df.Genre == 'Misc') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014plat = vg_df[(vg_df.Genre == 'Platform') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014puz = vg_df[(vg_df.Genre == 'Puzzle') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014rac = vg_df[(vg_df.Genre == 'Racing') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014rpg = vg_df[(vg_df.Genre == 'Role-Playing') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014shoot = vg_df[(vg_df.Genre == 'Shooter') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014sim = vg_df[(vg_df.Genre == 'Simulation') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014sports = vg_df[(vg_df.Genre == 'Sports') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]
df2014strat = vg_df[(vg_df.Genre == 'Strategy') & (vg_df.Year == 2014) & (vg_df.JP_Sales_Million > 0)]

#create variables
action_sales = vg_df['JP_Sales_Million'].where(df2014action.Genre == 'Action')
adv_sales = vg_df['JP_Sales_Million'].where(df2014adventure.Genre == 'Adventure')
fight_sales = vg_df['JP_Sales_Million'].where(df2014fighting.Genre == 'Fighting')
misc_sales = vg_df['JP_Sales_Million'].where(df2014misc.Genre == 'Misc')
plat_sales = vg_df['JP_Sales_Million'].where(df2014plat.Genre == 'Platform')
puz_sales = vg_df['JP_Sales_Million'].where(df2014puz.Genre == 'Puzzle')
rac_sales = vg_df['JP_Sales_Million'].where(df2014rac.Genre == 'Racing')
rp_sales = vg_df['JP_Sales_Million'].where(df2014rpg.Genre == 'Role-Playing')
shoot_sales = vg_df['JP_Sales_Million'].where(df2014shoot.Genre == 'Shooter') 
sim_sales = vg_df['JP_Sales_Million'].where(df2014sim.Genre == 'Simulation')
sport_sales = vg_df['JP_Sales_Million'].where(df2014sports.Genre == 'Sports')
strat_sales = vg_df['JP_Sales_Million'].where(df2014strat.Genre == 'Strategy') 

# Data to plot
sales = [action_sales.sum(), adv_sales.sum(), fight_sales.sum(), misc_sales.sum(), plat_sales.sum(), puz_sales.sum(), rac_sales.sum(), rp_sales.sum(), shoot_sales.sum(), sim_sales.sum(), sport_sales.sum(), strat_sales.sum()]
labels = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
#get values and use them, set the title of the pie.
fig = px.pie(values=sales, names=labels, title="2014 Japan genre sales", )
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