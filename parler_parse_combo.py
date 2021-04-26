# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:56:52 2021

@author: maahutch
"""
import csv
import os
import json
from parse_parler_html_fun import parse_parler_html


with open('parler_file_path.txt') as json_file:
    path = json.load(json_file)


summaries = os.listdir(path['input_path'])

print(len(summaries))

def main():
    all_pages = []
    count = 0
    
    numberToSkip = 45000
    
    for i in range(numberToSkip,len(summaries)): 
        if count <= len(summaries):
            
             one_page = parse_parler_html(file = summaries[i])
          
             count+=1
             
             progress = ((count/(len(summaries)-numberToSkip))*100)
            
             if one_page == 1:
                 print(summaries[i], 'has No Data -', '%f percent Done' % progress)
                
             else:
                 print(summaries[i], 'HAS DATA! - ', '%f percent Done' %  progress)
                 one_page['file_name'] = summaries[i]
                 all_pages.append(one_page)
             
        else: 
            break 
    
    
    keys = all_pages[0].keys()
    
    with open(path['output_path'], 'w+', newline='', encoding='utf-8') as file:    
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_pages)


if __name__ == '__main__':
    main()


