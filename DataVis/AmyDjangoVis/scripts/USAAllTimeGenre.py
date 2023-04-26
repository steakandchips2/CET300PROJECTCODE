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

# set where the html file will save to
save_loc = "./datavis/templates/datavis/usa/usatg_plot.html"

#create dataframe
vg_df = pd.read_csv("scripts/sales.csv",delimiter =",")

#create variables for the graph
NA_action_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Action')
NA_adv_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Adventure')
NA_fight_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Fighting')
NA_misc_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Misc')
NA_plat_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Platform')
NA_puz_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Puzzle')
NA_rac_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Racing')
NA_rp_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Role-Playing')
NA_shoot_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Shooter')
NA_sim_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Simulation')
NA_sport_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Sports')
NA_strat_sales = vg_df['NA_Sales_Million'].where(vg_df.Genre == 'Strategy')


# # Data to plot
labels = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
sales = [NA_action_sales.sum(), NA_adv_sales.sum(), NA_fight_sales.sum(), NA_misc_sales.sum(), NA_plat_sales.sum(), NA_puz_sales.sum(), NA_rac_sales.sum(), NA_rp_sales.sum(), NA_shoot_sales.sum(), NA_sim_sales.sum(), NA_sport_sales.sum(), NA_strat_sales.sum()]
#get values and use them, set the title of the pie.
fig = px.pie(values=sales, names=labels, title="USA All Time Genre Sales")
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