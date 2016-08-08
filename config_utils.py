# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:41:13 2015

@author: westerr

"""
import yaml, json

def load_yaml(filepath):
    """
    Load yaml config file as python dictionary, if path fails will return blank dictionary
    """
    with open(filepath, 'r') as reader:
        return yaml.load(reader)

def load_json(filepath):
    """
    Load json config file as python dictionary, if path fails will return blank dictionary
    """
    with open(filepath, 'r') as reader:
        return json.load(reader)
    
def output_yaml(yamlpath, dictionary, default_flow_style=False):
    """
    Writes python dictionary to yaml file
    """
    with open(yamlpath, 'w') as outfile:
        outfile.write(yaml.dump(dictionary, default_flow_style=default_flow_style))
        
def output_json(jsonpath, dictionary):
    """
    Writes python dictionary to json file
    """
    with open(jsonpath, 'w') as outfile:
        json.dump(dictionary, outfile)
        
