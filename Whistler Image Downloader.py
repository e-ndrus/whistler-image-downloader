import os.path
import urllib.request
import pandas as pd


dataset = pd.read_csv('links2.csv')

li=[]
name=[]

import pathlib
pathlib.Path('downloads3').mkdir(parents=True, exist_ok=True) 

def isNaN(num):
    return num != num

for a in range(0,len(dataset.index)):
        
    for i in range(5,11):
        fileLocation = dataset.iloc[a,i]
        if isNaN(fileLocation) == False:
            li.append(fileLocation)
            Const = dataset.iloc[a,1]  
            StationNum = str(dataset.iloc[a,4])
            name.append(Const+' Участок №'+StationNum)

for a in range(len(li)):    
    filename = os.path.join('downloads3',str(a)+' '+name[a]+'.jpg')
    print(filename)
    print(li[a])
#    try:
#        urllib.request.urlretrieve(li[a], filename)
#    except Exception as inst:
#        print(inst)
#        print('  Encountered unknown error. Continuing.') 
        
