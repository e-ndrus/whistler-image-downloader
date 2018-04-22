"""
Created on Sun Apr 22 10:54:35 2018

@author: Andrei Khrapavitski
"""

import os.path
import urllib.request
import pandas as pd
import re

dataset = pd.read_csv('unformatted.csv')

def urlClean(vert, hor):
    url = dataset.iloc[vert, hor]
    url = url.replace(';', '')
    url = url.replace('https://whistlerapp.org/attachments/', 'https://whistlerapp.org/xmedias/download/id/')
    return url

li=[]
name=[]

import pathlib
pathlib.Path('downloads3').mkdir(parents=True, exist_ok=True) 

for a in range(0,len(dataset.index)):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', urlClean(a,5))
        
    for i in range(len(urls)):
        li.append(urls[i])
        Const = dataset.iloc[a,1]  
        StationNum = str(dataset.iloc[a,4])
        name.append(Const+' Участок №'+StationNum)

for a in range(len(li)):    
    filename = os.path.join('downloads3',str(a)+' '+name[a]+'.jpg')
    print(filename)
    print(li[a])
    try:
        urllib.request.urlretrieve(li[a], filename)
    except Exception as inst:
        print(inst)
        print('  An error occured. Continuing.') 
        
