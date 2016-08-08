# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:01:06 2015

@author: westerr

"""
import logging

def file_logging(file_name, loglevel=logging.INFO, fileformat='[%(asctime)s] %(levelname)s: %(message)s',
                 filedatefmt='%m/%d/%Y %I:%M:%S %p', filemode='w'):
    """
    Initiates logging to file and logging to console
    
    """  
    # logging to file
    logging.basicConfig(filename = file_name,
                        level = loglevel,
                        format = fileformat,
                        datefmt = filedatefmt,
                        filemode = filemode)
                        
    # logging to console
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    
# Example implementation 
if __name__ == '__main__':
    from datetime import datetime
    file_logging('test.log')
    logger = logging.getLogger(__name__)    
    logger.info('Date: %s', datetime.now().strftime('%Y%m%d'))
