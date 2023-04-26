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
save_loc = "./datavis/templates/datavis/japan/jpatg_plot.html"

#create dataframe
vg_df = pd.read_csv("scripts/sales.csv",delimiter =",")

#create variables to use in the graph.
JP_action_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Action')
JP_adv_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Adventure')
JP_fight_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Fighting')
JP_misc_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Misc')
JP_plat_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Platform')
JP_puz_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Puzzle')
JP_rac_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Racing')
JP_rp_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Role-Playing')
JP_shoot_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Shooter')
JP_sim_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Simulation')
JP_sport_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Sports')
JP_strat_sales = vg_df['JP_Sales_Million'].where(vg_df.Genre == 'Strategy')

# # Data to plot
labels = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
sales = [JP_action_sales.sum(), JP_adv_sales.sum(), JP_fight_sales.sum(), JP_misc_sales.sum(), JP_plat_sales.sum(), JP_puz_sales.sum(), JP_rac_sales.sum(), JP_rp_sales.sum(), JP_shoot_sales.sum(), JP_sim_sales.sum(), JP_sport_sales.sum(), JP_strat_sales.sum()]
#get values and use them, set the title of the pie.
fig = px.pie(values=sales, names=labels, title=" Japan All Time Genre Sales")
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