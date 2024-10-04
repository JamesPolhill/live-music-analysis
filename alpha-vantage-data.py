# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:02:29 2024

@author: james
"""
import alpha_vantage

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='1MUHR75IBFU1BEG3', output_format='pandas')
data, meta_data = ts.get_daily(symbol='LYV', outputsize='full')

print(data)