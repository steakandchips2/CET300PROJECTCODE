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


#testing data visualisation accuracy.

vg_df = pd.read_csv("sales.csv",delimiter =",")

with open('output.txt', 'w') as f:
    

#test the top genre for each year in random regions
#scripts haver been randomly selected from the options of 

#EU 2010 - 2016 Genre -- Selected : 2010
#EU 2010 - 2016 Platform -- Selected :  2010
#JP 2010 - 2016 Genre -- Selected : 2012
#JP 2010 - 2016 Platform -- Selected : 2013
#US 2010 - 2016 Genre -- Selected : 2013
#US 2010 - 2016 Platform -- Selected : 2015
#OTHER 2010 - 2016 Genre -- Selected : 2012
#OTHER 2010 - 2016 Platform -- Selected : 2013
#GLOBAL 2010 - 2016 Genre -- Selected : 2016
#GLOBAL 2010 - 2016 Platform -- Selected : 2014

# #EU 2010 - 2016 Genre -- Selected : 2010
# #find the best selling genre EU 2010
      f.write(f'\n -- EUROPE --')
      f.write(f'\n -- Genre -')
      EUGenre2010 = vg_df.loc[(vg_df['EU_Sales_Million'] > 0) & (vg_df['Year'] == 2010), ['Genre', 'EU_Sales_Million']]
      genre_sales = EUGenre2010.groupby('Genre')['EU_Sales_Million'].sum()
      genre_count = EUGenre2010.groupby('Genre')['EU_Sales_Million'].count()
      best_selling_genre = genre_sales.idxmax()
      total_sales = genre_sales.max()
      genre_sales_pct = total_sales / genre_sales.sum() * 100
      game_count = genre_count[best_selling_genre]
      f.write(f'\n The best-selling genre in Europe in 2010 was {best_selling_genre} with total sales of {total_sales:.2f} million, '
            f'which represents {genre_sales_pct:.1f}% of the total sales for all genres in 2010. '
            f'There were {game_count} games released in the {best_selling_genre} genre.')

      #EU 2010 - 2016 Platform -- Selected :  2010
      f.write(f'\n --  Platform - ')
      EUPlatform2010 = vg_df.loc[(vg_df['EU_Sales_Million'] > 0) & (vg_df['Year'] == 2010), ['Platform', 'EU_Sales_Million', 'Name']]
      platform_sales = EUPlatform2010.groupby('Platform')['EU_Sales_Million'].sum()
      best_selling_platform = platform_sales.idxmax()
      total_sales = platform_sales.max()
      platform_sales_pct = total_sales / platform_sales.sum() * 100
      num_released = EUPlatform2010[EUPlatform2010['Platform'] == best_selling_platform]['Name'].nunique()
      f.write(f'\n The best-selling platform in Europe in 2010 was {best_selling_platform} with total sales of {total_sales:.2f} million, '
            f'which represents {platform_sales_pct:.1f}% of the total sales for all platforms in 2010. '
            f'{num_released} games were released for this platform in 2010.')


      f.write(f'\n -- ############################################################ --')
      f.write(f'\n ')
      f.write(f'\n ')


      #JP 2010 - 2016 Genre -- Selected : 2012
      f.write(f'\n --  JAPAN -- ')
      f.write(f'\n --  Genre - ')
      JPGenre2012 = vg_df.loc[(vg_df['JP_Sales_Million'] > 0) & (vg_df['Year'] == 2012), ['Genre', 'JP_Sales_Million']]
      genre_sales = JPGenre2012.groupby('Genre')['JP_Sales_Million'].sum()
      genre_count = JPGenre2012.groupby('Genre')['JP_Sales_Million'].count()
      best_selling_genre = genre_sales.idxmax()
      total_sales = genre_sales.max()
      genre_sales_pct = total_sales / genre_sales.sum() * 100
      game_count = genre_count[best_selling_genre]
      f.write(f'\n The best-selling genre in Japan in 2012 was {best_selling_genre} with total sales of {total_sales:.2f} million, '
            f'which represents {genre_sales_pct:.1f}% of the total sales for all genres in 2012. '
            f'There were {game_count} games released in the {best_selling_genre} genre.')

      #JP 2010 - 2016 Platform -- Selected : 2013
      f.write(f'\n --  Platform - ')

      JPPlatform2013 = vg_df.loc[(vg_df['JP_Sales_Million'] > 0) & (vg_df['Year'] == 2013), ['Platform', 'JP_Sales_Million', 'Name']]
      platform_sales = JPPlatform2013.groupby('Platform')['JP_Sales_Million'].sum()
      best_selling_platform = platform_sales.idxmax()
      total_sales = platform_sales.max()
      platform_sales_pct = total_sales / platform_sales.sum() * 100
      num_released = JPPlatform2013[JPPlatform2013['Platform'] == best_selling_platform]['Name'].nunique()
      f.write(f'\n The best-selling platform in Japan in 2013 was {best_selling_platform} with total sales of {total_sales:.2f} million, '
            f'which represents {platform_sales_pct:.1f}% of the total sales for all platforms in 2013. '
            f'{num_released} games were released for this platform in 2013.')

      f.write(f'\n -- ############################################################ --')
      f.write(f'\n ')
      f.write(f'\n ')

      #US 2010 - 2016 Genre -- Selected : 2013
      f.write(f'\n --  USA -- ')
      f.write(f'\n --  Genre - ')
      USGenre2013 = vg_df.loc[(vg_df['NA_Sales_Million'] > 0) & (vg_df['Year'] == 2013), ['Genre', 'NA_Sales_Million']]
      genre_sales = USGenre2013.groupby('Genre')['NA_Sales_Million'].sum()
      genre_count = USGenre2013.groupby('Genre')['NA_Sales_Million'].count()
      best_selling_genre = genre_sales.idxmax()
      total_sales = genre_sales.max()
      genre_sales_pct = total_sales / genre_sales.sum() * 100
      game_count = genre_count[best_selling_genre]
      f.write(f'\n The best-selling genre in USA in 2013 was {best_selling_genre} with total sales of {total_sales:.2f} million, '
            f'which represents {genre_sales_pct:.1f}% of the total sales for all genres in 2013. '
            f'There were {game_count} games released in the {best_selling_genre} genre.')


      #US 2010 - 2016 Platform -- Selected : 2015
      f.write(f'\n --  Platform - ')

      USPlatform2015 = vg_df.loc[(vg_df['NA_Sales_Million'] > 0) & (vg_df['Year'] == 2015), ['Platform', 'NA_Sales_Million', 'Name']]
      platform_sales = USPlatform2015.groupby('Platform')['NA_Sales_Million'].sum()
      best_selling_platform = platform_sales.idxmax()
      total_sales = platform_sales.max()
      platform_sales_pct = total_sales / platform_sales.sum() * 100
      num_released = USPlatform2015[USPlatform2015['Platform'] == best_selling_platform]['Name'].nunique()
      f.write(f'\n The best-selling platform in USA in 2015 was {best_selling_platform} with total sales of {total_sales:.2f} million, '
            f'which represents {platform_sales_pct:.1f}% of the total sales for all platforms in 2015. '
            f'{num_released} games were released for this platform in 2015.')

      f.write(f'\n -- ############################################################ --')
      f.write(f'\n ')
      f.write(f'\n ')



      #OTHER 2010 - 2016 Genre -- Selected : 2012
      f.write(f'\n --  OTHER -- ')
      f.write(f'\n --  Genre - ')
      OTGenre2012 = vg_df.loc[(vg_df['Other_Sales_Million'] > 0) & (vg_df['Year'] == 2012), ['Genre', 'Other_Sales_Million']]
      genre_sales = OTGenre2012.groupby('Genre')['Other_Sales_Million'].sum()
      genre_count = OTGenre2012.groupby('Genre')['Other_Sales_Million'].count()
      best_selling_genre = genre_sales.idxmax()
      total_sales = genre_sales.max()
      genre_sales_pct = total_sales / genre_sales.sum() * 100
      game_count = genre_count[best_selling_genre]
      f.write(f'\n The best-selling genre in Other regions in 2012 was {best_selling_genre} with total sales of {total_sales:.2f} million, '
            f'which represents {genre_sales_pct:.1f}% of the total sales for all genres in 2012. '
            f'There were {game_count} games released in the {best_selling_genre} genre.')


      #OTHER 2010 - 2016 Platform -- Selected : 2013
      f.write(f'\n --  Platform - ')

      OTPlatform2013 = vg_df.loc[(vg_df['Other_Sales_Million'] > 0) & (vg_df['Year'] == 2013), ['Platform', 'Other_Sales_Million', 'Name']]
      platform_sales = OTPlatform2013.groupby('Platform')['Other_Sales_Million'].sum()
      best_selling_platform = platform_sales.idxmax()
      total_sales = platform_sales.max()
      platform_sales_pct = total_sales / platform_sales.sum() * 100
      num_released = OTPlatform2013[OTPlatform2013['Platform'] == best_selling_platform]['Name'].nunique()
      f.write(f'\n The best-selling platform in Other regions in 2013 was {best_selling_platform} with total sales of {total_sales:.2f} million, '
            f'which represents {platform_sales_pct:.1f}% of the total sales for all platforms in 2013. '
            f'{num_released} games were released for this platform in 2013.')


      f.write(f'\n -- ############################################################ --')
      f.write(f'\n ')
      f.write(f'\n ')

      #GLOBAL 2010 - 2016 Genre -- Selected : 2016
      f.write(f'\n --  GLOBAL --')
      f.write(f'\n -Genre -')
      glob_Genre2016 = vg_df.loc[(vg_df['Global_Sales_Million'] > 0) & (vg_df['Year'] == 2016), ['Genre', 'Global_Sales_Million']]
      genre_sales = glob_Genre2016.groupby('Genre')['Global_Sales_Million'].sum()
      genre_count = glob_Genre2016.groupby('Genre')['Global_Sales_Million'].count()
      best_selling_genre = genre_sales.idxmax()
      total_sales = genre_sales.max()
      genre_sales_pct = total_sales / genre_sales.sum() * 100
      game_count = genre_count[best_selling_genre]
      f.write(f'\n The best-selling genre globally in 2016 was {best_selling_genre} with total sales of {total_sales:.2f} million, '
            f'which represents {genre_sales_pct:.1f}% of the total sales for all genres in 2016. '
            f'There were {game_count} games released in the {best_selling_genre} genre.')

      #GLOBAL 2010 - 2016 Platform -- Selected : 2014
      f.write(f'\n - Platform -')

      glob_Platform2014 = vg_df.loc[(vg_df['Global_Sales_Million'] > 0) & (vg_df['Year'] == 2014), ['Platform', 'Global_Sales_Million', 'Name']]
      platform_sales = glob_Platform2014.groupby('Platform')['Global_Sales_Million'].sum()
      best_selling_platform = platform_sales.idxmax()
      total_sales = platform_sales.max()
      platform_sales_pct = total_sales / platform_sales.sum() * 100
      num_released = glob_Platform2014[glob_Platform2014['Platform'] == best_selling_platform]['Name'].nunique()
      f.write(f'\n The best-selling platform globally in 2014 was {best_selling_platform} with total sales of {total_sales:.2f} million, '
            f'which represents {platform_sales_pct:.1f}% of the total sales for all platforms in 2014. '
            f'{num_released} games were released for this platform in 2014.')
      

      f.write(f'\n -- ############################################################ --')
      f.write(f'\n ')
      f.write(f'\n ')