# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:10:42 2021

@author: thebe
"""


import csv


def read_data(filename):
    #Loading the data into traindata list.
    with open(filename,"r") as csvfile:
        datareader=csv.reader(csvfile,delimiter=',')
        traindata=[]
        for row in datareader:
            traindata.append(row) 
        return traindata
        
def finds():
    dataarr=read_data('ENJOYSPORT.CSV')
    h=['0','0','0','0','0','0']
    row=len(dataarr)
    column=7
    for x in range(1,row):
        t=dataarr[x]
        print(t)
        if t[column-1]=='1':
            for y in range(0,column-1):
                if h[y]==t[y]:
                    pass
                elif h[y]!=t[y] and h[y]=='0':
                    h[y]=t[y]
                elif h[y]!=t[y] and h[y]!='0':
                    h[y]='?'
            print(h)
            
    print('maximally specific set')        
    print('<',end=' ')
    for i in range(0,len(h)):
        print(h[i],',',end=' ')
    print('>')
    
finds()
        
