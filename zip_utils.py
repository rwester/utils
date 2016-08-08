# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:44:27 2015

@author: westerr

Utility functions for zip files
"""
import os, zipfile, StringIO
import pandas as pd

def compress_files(zip_name, file_list=None, file_types=None, file_path=None, zip_path=None, delete_files=False):
    """
    Compress files in list or of given file type into a zip file called zip_name
    
    if file_path is specified will use for path to file else will use working dir
    if zip_path is specified will use for path to resulting zip else will use working dir
    
    file_list must be a list even if length 1 
    
    """
    # Define input and output paths
    if not file_path:
        file_path = os.getcwd() 
    if not zip_path:
        zip_path = os.getcwd()
        
    # Get list of files to compress
    if not file_list:
        file_list = [f for f in os.listdir(file_path)]
    if file_types:
        file_list = [f for f in file_list if f.endswith(tuple(file_types))]
  
    # Compress files
    with zipfile.ZipFile(os.path.join(zip_path, zip_name), 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in file_list:
            with open(os.path.join(file_path, file), 'r') as f:
                zf.writestr("{}".format(file), f.read())
    
    # Clean up files if specified
    if delete_files == True:
        for f in file_list:
            os.remove(os.path.join(file_path, f))

def extract_content(zippath, file_list=None, file_types=None, outpath=None):
    """
    Extract files in list or of given file type from a zip file
    
    if outpath is specificed will extract file(s) to path else will use working dir
   
    file_list must be a list even if length 1 
    
    """
    # Define output paths
    if not outpath:
        outpath = os.getcwd()
        
    # Unzip files
    with zipfile.ZipFile(zippath, "r") as unzip:
        if not file_list:
            file_list = [f for f in unzip.namelist()]
        if file_types:
            file_list = [f for f in file_list if f.endswith(tuple(file_types))]
        for f in file_list:
            unzip.extract(f, outpath)

def df_from_zip(zippath, filename, **kargs):
    """
    Reads delimited text file from zip file into dataframe without extracting contents to disk
    
    kargs excepts pandas.read_csv args
    
    """    
    with zipfile.ZipFile(zippath, "r") as unzip:
        return pd.read_csv(StringIO.StringIO(unzip.read(filename)), **kargs)
        
        
    
        
        
