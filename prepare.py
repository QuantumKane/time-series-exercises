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
    
    print(df.head())
    
    return df


def prep_germany_data(df):
    '''
    Takes in a dataframe, coverts Date to DateTime format and makes it the index, produces histograms 
    of all variables, renames "Wind+Solar" to the more python-friendly "WindSolar", fills the abundant 
    nulls/NaNs with 0, and adds the columns 'month' and 'year'. We take a look at the amended dataframe
    and the dataframe is returned.
    '''
    # Convert date to datetime for time series analysis
    df.Date = pd.to_datetime(df.Date)
    
    # Histogram of Consumption
    df.Consumption.hist()
    plt.title('Consumption')
    plt.show()
    
    # Histogram of Wind
    df.Wind.hist()
    plt.title('Wind')
    plt.show()
    
    # Histogram of Solar
    df.Solar.hist()
    plt.title('Solar')
    plt.show()
    
    # Histogram of Solar
    df['Wind+Solar'].hist()
    plt.title('WindSolar')
    plt.show()
    
    # Rename column to python ok type
    df = df.rename(columns={'Wind+Solar': 'WindSolar'})
    
    # Fill null values with 0
    df = df.fillna(0)
    
    # Set date as index for time series analysis
    df = df.set_index('Date').sort_index()
    
    # add columns to df
    df['month'] = df.index.month
    df['year'] = df.index.year
    
    print(df.head())
    
    return df