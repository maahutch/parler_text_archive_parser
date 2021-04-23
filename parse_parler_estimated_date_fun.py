# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:11:16 2021

@author: maahutch
"""

#from datetime import datetime
#from dateutil.relativedelta import relativedelta


def calc_estimated_time(timeFromHtml):

    start = '1/6/21'
    
    dt_str = datetime.strptime(start, '%m/%d/%y')
    
    period = timeFromHtml.split()[1]
    
    
    if period == 'day' or period == 'days':
        
        rel_time = relativedelta(days = int(timeFromHtml.split()[0]))
        
    elif period == 'week' or period == 'weeks':
        
        rel_time = relativedelta(weeks = int(timeFromHtml.split()[0]))
    
    elif period == 'month' or period == 'months':
        
        rel_time = relativedelta(months = int(timeFromHtml.split()[0]))
        
    elif period == 'year' or period == 'years':
    
          rel_time = relativedelta(years = int(timeFromHtml.split()[0]))
          
    estimated_date = dt_str - rel_time

    return(estimated_date.date())


