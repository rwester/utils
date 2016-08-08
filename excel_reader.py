# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:39:02 2015

@author: westerr

Util for reading xls, xlsx, and xlsm into pandas

"""
import os, shutil, random, string
import pandas as pd

def excel_xls(filepath, **kargs):
    """
    Reads .xls file to dataframe, if path fails will return empty dataframe
    
    kargs excepts pandas.read_excel args
    
    """
    return pd.read_excel(pd.ExcelFile(filepath), **kargs)
    
def excel_xml(filename, **kargs):
    """
    Reads xml formatted excel files (.xlsx or .xlsm), if path fails will return empty dataframe
    
    kargs excepts pandas.read_excel args
    
    
    """
    if filename[-4:] == 'xlsm':
        # Define temp file with random key generator, done for running parallel processes
        tempfile = 'temp_' + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(9)) + ".xlsx"
        shutil.copyfile(filename, tempfile)
        df  = pd.read_excel(tempfile, **kargs)
        if os.path.isfile(tempfile):
            os.remove(tempfile)
    elif filename[-4:] == 'xlsx':
        df  = pd.read_excel(filename, **kargs)
    else:
        raise IOError("File must be xlsx or xlsm")
    return df
    
    
    
    
    
    
    
    
    
