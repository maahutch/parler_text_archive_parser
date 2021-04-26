# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:59:09 2021

@author: maahutch
"""
from bs4 import BeautifulSoup
from parse_parler_estimated_date_fun import calc_estimated_time
from parse_parler_extract_video_id import url_split

def parse_parler_html(file):
    
    path = 'D:/parler_text/parler_2020-01-06_posts-partial/' + file
    
    f = open(path, "r", encoding='utf8')    
    
    page = BeautifulSoup(f.read(),"html.parser")
    
    try:
        noscript = page.find('noscript').getText()
    except:
        noscript = 'null'
    
    if noscript =='Please enable JavaScript to continue using this application.':
        return 1
    else:
        #Title
        try:
            title = page.find('title').getText()
        except: 
            title = None
            
        if title is None:
            title = ''
            
        #Echoed
        try:
            echoed = page.body.main.div.find('div', {'class': 'eb--col eb--statement'}).text
            echoed = echoed.replace("\n", "")
        except:
            echoed = None
            
        if echoed is None: 
            echoed = ''
            
        #Time Stamp
        try:
            time = page.body.main.div.find('span', {'class': 'post--timestamp'}).text
        except:
            time = None
            
        if time is None: 
            time = ''
        
        #Estimated Time
        
        try:
            estimated_time = calc_estimated_time(time)
        except: 
            estimated_time = ''
        
        #Author
        try: 
            author = page.body.main.div.find('span', {'class': 'author--name'}).text
        except:
            author = None
            
        if author is None: 
            time = ''
        
        #Username
        try: 
            username = page.body.main.div.find('span', {'class': 'author--username'}).text
        except: 
            username = None
            
        if username is None:
            username = ''
            
        #Impressions
        try: 
            impressions = page.body.main.div.find('span', {'class': 'impressions--count'}).text
        except: 
            impressions = None
            
        if impressions is None:
            impressions = ''
        
        #Body
        try: 
            body = page.body.main.div.p.string
        except: 
            body = None
            
        if body is None: 
            body = ''
        
        #Media
        try:  
            media = page.body.main.div.a.contents[-1]
            media = media.replace("\n", "")
        except: 
            media = None
            
        if media is None: 
            media = ''
            
        #video/gif id
        try:
            video_id = url_split(media)
        except:
            video_id = ''
        
        
        one_page = {'title': title, 
                    'echoed': echoed,
                    'time': time,
                    'estimated time': estimated_time,
                    'author': author,
                    'username': username,
                    'impressions': impressions, 
                    'body': body, 
                    'media': media,
                    'parler_content_file_id': video_id}

    return one_page

        

        
