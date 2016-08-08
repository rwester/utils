# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:53:26 2015

@author: westerr

Common date tasks 

"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
from dateutil import parser
import pytz

def business_days(start_date, end_date):
    """
    Given a start and end datetime will return a list of datetime objects
    inclusive of the start and end dates, but only including business days (M-F)
    
    """
    # Create list of business day dates
    dates = pd.to_datetime(pd.bdate_range(start_date, end_date))
    return [datetime.utcfromtimestamp((i - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')) for i in dates]

def chunk_dates(start_date, end_date, freq='MS'):
    """
    Given a start and end datetime and a freq will return a list of time tuples containing
    date chucks ie. start date of chunk and end date of chunk, dates can be strings or datetime objects
    
    """
    
    if isinstance(start_date, date):
        start_dt = start_date
    else:
        start_dt = parser.parse(start_date)
    if isinstance(end_date, date):
        end_dt = end_date
    else:
        end_dt = parser.parse(end_date)
    
    
    # Generate a list of dates
    dates = pd.to_datetime(pd.date_range(start_dt, end_dt, freq=freq)).values
    clean_dates = [datetime.utcfromtimestamp((i - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')) for i in dates]  
    if start_dt not in clean_dates:    
        clean_dates.append(start_dt)
    if end_dt not in clean_dates:
        clean_dates.append(end_dt)
    clean_dates.sort()
    
    # Creating time tuples
    time_tuples = []
    for n in xrange(len(clean_dates) - 1):
        if n < len(clean_dates) - 2:
            time_tuples.append((clean_dates[n], clean_dates[n+1] - timedelta(days=1)))
        else:
            time_tuples.append((clean_dates[n], clean_dates[n+1]))
    return time_tuples

def convert_tz(df, cols, from_tz='utc', to_tz='utc', append_col_name=True):
    """
    Convert timezone of dataframe columns
    
    cols must be a list of column names, even if lenght = 1
    """
    if df.index.name:
        return_index = df.index.name
        df.reset_index(inplace=True)
    else:
        return_index = None
    if type(cols) == list:
        for col in cols:
            df.set_index(col, inplace=True)
            df.index = df.index.tz_localize(pytz.timezone(from_tz)).tz_convert(pytz.timezone(to_tz))
            if append_col_name == True:
                df.index.name = df.index.name + '_' + to_tz
            df.reset_index(inplace=True)
        if return_index:
            df.set_index(return_index, inplace=True)
        return df
    else:
        raise TypeError("cols must be of type list")

def fiscalyear(fy_start, input_date=None):
    """
    Defines the current fiscal year based on the FY start date
    
    fy_start should be in format "MMDD"
    
    input_date can be string or datetime obj
    
    """
    # Assessing input_date
    if not input_date:
        dt = datetime.today()
    else:
        if isinstance(input_date, date):
            dt = input_date
        else:
            dt = parser.parse(input_date)
    
    # Define this years fy change
    fy_change = dt.replace(day=int(fy_start[2:]), month=int(fy_start[:2]),
                           hour=0, minute=0, second=0, microsecond=0)

    # Return current fiscal year start 
    return fy_change.replace(year=dt.year-1) if dt < fy_change else fy_change

def fiscalweek(current_fy, input_date=None):
    """
    Determines the current fiscal year week.
    
    current_fy is the output of fiscalyear
    
    The first partial week of the fy is week 0, otherwise
    the final week would be week 53
    
    input_date can be string or datetime obj
    
    """
    # Assessing input_date
    if not input_date:
        dt = datetime.today()
    else:
        if isinstance(input_date, date):
            dt = input_date
        else:
            dt = parser.parse(input_date)

    # Calculate fiscal week
    firstmonday = (current_fy - timedelta(days=current_fy.weekday())) # finds first monday of the fiscal year
    monday_now = (dt - timedelta(days=dt.weekday())) # finds monday of current week
    return (monday_now - firstmonday).days / 7  # subtracts mondays to get days then divids by 7 for weeks

# Example implementation 
if __name__ == '__main__':
    #print business_days('2016-01-01', '2016-02-01')
    #print chunk_dates('2016-01-01', '2016-05-01')
    print fiscalweek(fiscalyear('0401'))







