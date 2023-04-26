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
save_loc = "./datavis/templates/datavis/global/globalgenre/gg16_plot.html"


#create dataframe from csv
vg_df = pd.read_csv("scripts/sales.csv",delimiter =",")
#create more specific dataframes
df2016action = vg_df[(vg_df.Genre == 'Action') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016adventure = vg_df[(vg_df.Genre == 'Adventure') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016fighting = vg_df[(vg_df.Genre == 'Fighting') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016misc = vg_df[(vg_df.Genre == 'Misc') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016plat = vg_df[(vg_df.Genre == 'Platform') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016puz = vg_df[(vg_df.Genre == 'Puzzle') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016rac = vg_df[(vg_df.Genre == 'Racing') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016rpg = vg_df[(vg_df.Genre == 'Role-Playing') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016shoot = vg_df[(vg_df.Genre == 'Shooter') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016sim = vg_df[(vg_df.Genre == 'Simulation') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016sports = vg_df[(vg_df.Genre == 'Sports') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]
df2016strat = vg_df[(vg_df.Genre == 'Strategy') & (vg_df.Year == 2016) & (vg_df.Global_Sales_Million > 0)]

#create variables
action_sales = vg_df['Global_Sales_Million'].where(df2016action.Genre == 'Action')
adv_sales = vg_df['Global_Sales_Million'].where(df2016adventure.Genre == 'Adventure')
fight_sales = vg_df['Global_Sales_Million'].where(df2016fighting.Genre == 'Fighting')
misc_sales = vg_df['Global_Sales_Million'].where(df2016misc.Genre == 'Misc')
plat_sales = vg_df['Global_Sales_Million'].where(df2016plat.Genre == 'Platform')
puz_sales = vg_df['Global_Sales_Million'].where(df2016puz.Genre == 'Puzzle')
rac_sales = vg_df['Global_Sales_Million'].where(df2016rac.Genre == 'Racing')
rp_sales = vg_df['Global_Sales_Million'].where(df2016rpg.Genre == 'Role-Playing')
shoot_sales = vg_df['Global_Sales_Million'].where(df2016shoot.Genre == 'Shooter') 
sim_sales = vg_df['Global_Sales_Million'].where(df2016sim.Genre == 'Simulation')
sport_sales = vg_df['Global_Sales_Million'].where(df2016sports.Genre == 'Sports')
strat_sales = vg_df['Global_Sales_Million'].where(df2016strat.Genre == 'Strategy') 

# Data to plot
sales = [action_sales.sum(), adv_sales.sum(), fight_sales.sum(), misc_sales.sum(), plat_sales.sum(), puz_sales.sum(), rac_sales.sum(), rp_sales.sum(), shoot_sales.sum(), sim_sales.sum(), sport_sales.sum(), strat_sales.sum()]
labels = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
#get values and use them, set the title of the pie.
fig = px.pie(values=sales, names=labels, title="2016 Global genre sales", )
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