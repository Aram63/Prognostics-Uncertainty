#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 04:00:47 2017

@author: Shankar
"""
from stateequation import stateupdateequation, computevoltageforthreshold,getinput
from RULPredictor import calculateRUL
from Parameters import params
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde



Prm=params()
stateTimeofPrediction=[Prm.Init0,Prm.Init1,Prm.Init2,Prm.Init3]
stddev_State=[0.1*stateTimeofPrediction[0],0.1*stateTimeofPrediction[1],0.1,0.1]


RUL=[]

for i in range(0,15):
    
    initstate0=np.random.normal(stateTimeofPrediction[0],stddev_State[0], 1)
    initstate1=np.random.normal(stateTimeofPrediction[1],stddev_State[1], 1)
    initstate2=np.random.normal(stateTimeofPrediction[2],stddev_State[2], 1)
    initstate3=np.random.normal(stateTimeofPrediction[3],stddev_State[3], 1)
    loading=np.random.normal(2,0.2,1)
    
    listofvariables=[initstate0,initstate1,initstate2,initstate3,loading]
    
    R=calculateRUL(listofvariables,Prm)
    RUL.append(R)





#PLOTTING
density = gaussian_kde(RUL)
xs = np.linspace(min(RUL)*0.9,max(RUL)*1.1,1000)
density.covariance_factor = lambda : 0.25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.show()


    
