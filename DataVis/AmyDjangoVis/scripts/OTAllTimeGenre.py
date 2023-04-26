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
import plotly.graph_objects as go

#set save location for the html file so it can be displayed on django
save_loc = "./datavis/templates/datavis/other/otatg_plot.html"


#create dataframe
vg_df = pd.read_csv("scripts/sales.csv",delimiter =",")

#create variables to use in the graph.
OT_action_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Action')
OT_adv_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Adventure')
OT_fight_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Fighting')
OT_misc_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Misc')
OT_plat_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Platform')
OT_puz_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Puzzle')
OT_rac_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Racing')
OT_rp_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Role-Playing')
OT_shoot_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Shooter')
OT_sim_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Simulation')
OT_sport_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Sports')
OT_strat_sales = vg_df['Other_Sales_Million'].where(vg_df.Genre == 'Strategy')


# # Data to plot
labels = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
sales = [OT_action_sales.sum(), OT_adv_sales.sum(), OT_fight_sales.sum(), OT_misc_sales.sum(), OT_plat_sales.sum(), OT_puz_sales.sum(), OT_rac_sales.sum(),
    OT_rp_sales.sum(), OT_shoot_sales.sum(), OT_sim_sales.sum(), OT_sport_sales.sum(), OT_strat_sales.sum()]
#get values and use them, set the title of the pie.
fig = px.pie(values=sales, names=labels, title="Other Regions All Time Genre Sales")
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

