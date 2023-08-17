#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:45:43 2020

@author: Andrew Ostensen

This function creates helper data to test the 'string_conversion' script created for 
the Disney analysis for the Python Programming for Data Science project.

"""

from string_conversion import string_conversion as sc
import pandas as pd

def test_shape():

    # Create helper data and write tests for the 'string_conversion' function
    raw = {'vehicle': ['Toyota Highlander', 'Nissan Frontier', 'Ford Fiesta', 'Chevy Silverado', 'Porsche Boxster', 
                       'Honda Civic', 'Ford F-150'], 
           'cost': ['$32,777', '$18,899', '$12,344', '$27,555', '$87,566', '$21,444', '$45,655'],
           'year': [2012, 2017, 2006, 2002, 2019, 2014, 2018]}

    helper_data = pd.DataFrame.from_dict(raw)

    res = sc(helper_data, 'cost')
    assert res.shape == helper_data.shape, 'Function has incorrectly modified the DataFrame'
    return
    
    
def test_type_int():

    # Create helper data and write tests for the 'string_conversion' function
    raw = {'vehicle': ['Toyota Highlander', 'Nissan Frontier', 'Ford Fiesta', 'Chevy Silverado', 'Porsche Boxster', 
                       'Honda Civic', 'Ford F-150'], 
           'cost': ['$32,777', '$18,899', '$12,344', '$27,555', '$87,566', '$21,444', '$45,655'],
           'year': [2012, 2017, 2006, 2002, 2019, 2014, 2018]}

    helper_data = pd.DataFrame.from_dict(raw)

    res = sc(helper_data, 'cost')
    assert res['cost'].dtype == 'int64', 'Function has not converted the data to an int datatype'
    return
    
    
def test_type_float():

    # Create helper data and write tests for the 'string_conversion' function
    raw = {'vehicle': ['Toyota Highlander', 'Nissan Frontier', 'Ford Fiesta', 'Chevy Silverado', 'Porsche Boxster', 
                       'Honda Civic', 'Ford F-150'], 
           'cost': ['$32,777', '$18,899', '$12,344', '$27,555', '$87,566', '$21,444', '$45,655'],
           'year': [2012, 2017, 2006, 2002, 2019, 2014, 2018]}

    helper_data = pd.DataFrame.from_dict(raw)

    res = sc(helper_data, 'cost', 'float')
    assert res['cost'].dtype == 'float64', 'Function has not converted the data to a float datatype'  
    return