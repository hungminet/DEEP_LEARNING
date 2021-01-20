# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:00:57 2021

@author: ntruo

some about the dataset, the data is recorded every 10 minustes,
you get 144 data points per day

"""
#%% import dataset not use pandas

import os

f = open('jena_climate_2009_2016.csv')
data = f.read()
f.close()

lines = data.split('\n')
header = lines[0].split(',')
lines = lines[1:]

import numpy as np

float_data = np.zeros((len(lines),len(header)-1))

for i, line in enumerate(lines):
    values = [float(x) for x in line.split(',')[1:]]
    float_data[i,:] = values 
    
#%% visualize data
import matplotlib.pyplot as plt
temp = float_data[:, 1] 
plt.plot(range(len(temp)),temp)

