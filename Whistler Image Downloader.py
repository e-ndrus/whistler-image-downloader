import numpy as np
import os.path
import urllib.request
import pandas as pd


dataset = pd.read_csv('links2.csv')
dataset.loc[dataset['Station'] == 4]

X = dataset.iloc[0, [5,6,7,8,9,10]].values
df = pd.DataFrame(X)

li=[]
name=[]

import pathlib
pathlib.Path('downloads3').mkdir(parents=True, exist_ok=True) 

def isNaN(num):
    return num != num

for a in range(0,25):
        
    for i in range(5,11):
        fileLocation = dataset.iloc[a,i]
        if isNaN(fileLocation) == False:
            li.append(fileLocation)
            Const = dataset.iloc[a,1]  
            StationNum = str(dataset.iloc[a,4])
            name.append(Const+' Участок №'+StationNum)

for a in range(len(li)):    
    filename = os.path.join('downloads3', name[a]+'.jpg')
    print(li[a])
    try:
        urllib.request.urlretrieve(li[a], filename)
    except Exception as inst:
        print(inst)
        print('  Encountered unknown error. Continuing.') 
        
