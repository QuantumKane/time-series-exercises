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


def prep_german_data(df):
    '''
    prepare dataset for explore
    '''
    # Convert date to datetime for time series analysis
    opsd_df.Date = pd.to_datetime(opsd_df.Date)
    
    # Histogram of Consumption
    opsd_df.Consumption.hist()
    plt.title('Consumoption')
    plt.show()
    
    # Histogram of Wind
    opsd_df.Wind.hist()
    plt.title('Wind')
    plt.show()
    
    # Histogram of Solar
    opsd_df.Solar.hist()
    plt.title('Solar')
    plt.show()
    
    # Histogram of Solar
    opsd_df['Wind+Solar'].hist()
    plt.title('WindSolar')
    plt.show()
    
    # Rename column to python ok type
    opsd_df = opsd_df.rename(columns={'Wind+Solar': 'WindSolar'})
    
    # Fill null values with 0
    opsd_df = opsd_df.fillna(0)
    
    # Set date as index for time series analysis
    opsd_df = opsd_df.set_index('Date').sort_index()
    
    # add columns to df
    opsd_df['month'] = opsd_df.index.month
    opsd_df['weekday'] = opsd_df.index.day_name()
    opsd_df['year'] = opsd_df.index.year
    
    df.head()
    
    return df