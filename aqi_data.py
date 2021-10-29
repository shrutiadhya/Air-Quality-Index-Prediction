# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:20:28 2021

@author: Shruti
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24):
        data_add=0
        avg_data =0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                data_add = data_add+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp = float(i)
                    data_add=data_add+temp
        avg_data=data_add/24
        temp_i=temp_i+1
        average.append(avg_data)
    return average

def avg_data_2014():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24):
        data_add=0
        avg_data =0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                data_add = data_add+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp = float(i)
                    data_add=data_add+temp
        avg_data=data_add/24
        temp_i=temp_i+1
        average.append(avg_data)
    return average

def avg_data_2015():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24):
        data_add=0
        avg_data =0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                data_add = data_add+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp = float(i)
                    data_add=data_add+temp
        avg_data=data_add/24
        temp_i=temp_i+1
        average.append(avg_data)
    return average

def avg_data_2016():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24):
        data_add=0
        avg_data =0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                data_add = data_add+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp = float(i)
                    data_add=data_add+temp
        avg_data=data_add/24
        temp_i=temp_i+1
        average.append(avg_data)
    return average

def avg_data_2017():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize=24):
        data_add=0
        avg_data =0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                data_add = data_add+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp = float(i)
                    data_add=data_add+temp
        avg_data=data_add/24
        temp_i=temp_i+1
        average.append(avg_data)
    return average

def avg_data_2018():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize=24):
        data_add=0
        avg_data =0.0
        data=[]
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                data_add = data_add+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp = float(i)
                    data_add=data_add+temp
        avg_data=data_add/24
        temp_i=temp_i+1
        average.append(avg_data)
    return average

if __name__=="__main__":
    data_2013 = avg_data_2013()
    data_2014 = avg_data_2014()
    data_2015 = avg_data_2015()
    data_2016 = avg_data_2016()
    data_2017 = avg_data_2017()
    data_2018 = avg_data_2018()
    plt.plot(range(365),data_2013,label="2013 data")
    plt.plot(range(364),data_2014,label="2014 data")
    plt.plot(range(365),data_2015,label="2015 data")
    plt.show()