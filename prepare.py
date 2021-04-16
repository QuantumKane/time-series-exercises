# necessary imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

######## time series prepare ######

def prep_store_data(df):
    '''
    Takes in a dataframe, coverts sale_date to DateTime format and makes it the index, produces 
    histograms of sale_amount and item_price and creates 3 new columns: month, day_of_week, and 
    sales_total. Returns the updated df.
    '''
    # Convert date to datetime for time series analysis
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    
    # Histogram of sale_amount
    df.sale_amount.hist()
    plt.title('Sale Amount')
    plt.show()
    
    # Histogram of item_price
    df.item_price.hist()
    plt.title('Item Price')
    plt.show()
    
    # Make sale_date the index
    df = df.set_index('sale_date').sort_index()
    
    # Create 3 new columns
    df['month'] = df.index.month
    df['day_week'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df


def prep_german_data(germany):
    '''
    prepare dataset for explore
    '''
    # Convert date to datetime for time series analysis
    germany.Date = pd.to_datetime(germany.Date)
    germany = germany[germany.Date >= '2012']
    
    # Fill null values with 0
    germany = germany.fillna(0)
    
    # Rename column to python ok type
    germany = germany.rename(columns={'Wind+Solar': 'orig_windsolar'})
    
    # Add calculated wind + solar column
    germany['windsolar'] = germany.Wind + germany.Solar
    
    # Set date as index for time series analysis
    germany = germany.set_index('Date').sort_index()
    
    # add columns for explore
    # germany['month'] = germany.index.month
    # germany['weekday'] = germany.index.day_name()
    # germany['year'] = germany.index.year
    # from Corey, make year, month, weekday into categories
    # germany = (germany.astype({'year': 'category', 'month': 'category', 'weekday': 'category'}))
    # if I make them categories bar and box plots don't work
    return germany