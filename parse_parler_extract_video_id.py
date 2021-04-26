# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:13:23 2021

@author: maahutch
"""

def url_split(addr):
    if(addr.find('parler')!=-1):
        
      addr_list = addr.split('/')
      
      name=addr_list[-1]
    
      if(name.find('.')!=-1):
          name_list = name.split('.')
          
          id = name_list[0]
          
          if(id.find('_')!=-1):
              id_list=id.split('_')
              
              sub_id = id_list[0]
          
              return(sub_id)
          else:
              return(id)
      else:
          return(name)
      
    else:
        return('')
     
        
