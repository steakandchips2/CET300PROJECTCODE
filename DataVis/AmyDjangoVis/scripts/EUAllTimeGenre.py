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
save_loc = "./datavis/templates/datavis/europe/EUAllTime_plot.html"

#create dataframe
vg_df = pd.read_csv("scripts/sales.csv",delimiter =",")


#create variables to use in the graph.
EU_action_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Action')
EU_adv_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Adventure')
EU_fight_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Fighting')
EU_misc_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Misc')
EU_plat_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Platform')
EU_puz_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Puzzle')
EU_rac_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Racing')
EU_rp_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Role-Playing')
EU_shoot_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Shooter')
EU_sim_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Simulation')
EU_sport_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Sports')
EU_strat_sales = vg_df['EU_Sales_Million'].where(vg_df.Genre == 'Strategy')

# Data to plot
sales = [EU_action_sales.sum(), EU_adv_sales.sum(), EU_fight_sales.sum(), EU_misc_sales.sum(), EU_plat_sales.sum(), EU_puz_sales.sum(), EU_rac_sales.sum(), EU_rp_sales.sum(), EU_shoot_sales.sum(), EU_sim_sales.sum(), EU_sport_sales.sum(), EU_strat_sales.sum()]
labels = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
#get values and use them, set the title of the pie.
fig = px.pie(values=sales, names=labels, title="Europe All Time Genre Sales")
# remove the background colour
fig.update_layout(
    paper_bgcolor="rgba(0, 0, 0, 0)", plot_bgcolor="rgba(0,0,0,0)", title_font_color="green", legend_bgcolor="white", xaxis_title='Genre', yaxis_title='Sales in million',)
#set colour and size of the % in the pie to make it clear
fig.update_traces(
    textfont=dict(
        color="black",
        size=16,
    )
)
#save to html file
fig.write_html(save_loc)