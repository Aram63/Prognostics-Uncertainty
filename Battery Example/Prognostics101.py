#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:49:20 2017

@author: Shankar
"""
from stateequation import stateupdateequation, computevoltageforthreshold,getinput
from RULPredictor import calculateRUL
from Parameters import params
import matplotlib.pyplot as plt

Prm=params()


stateTimeofPrediction=[Prm.Init0,Prm.Init1,Prm.Init2,Prm.Init3]
#stddev_State=[0.1*stateTimeofPrediction[0],0.1*stateTimeofPrediction[1],0.1,0.1]

RULsamples=[]
Loadvector=[2,3,4,5,2,1]
Timevector=[200, 500, 1000, 2000, 3000, 10000]


timeofprediction=0


#listinputs=[timeofprediction]
#listinputs=listinputs+stateTimeofPrediction
#listinputs=listinputs+Loadvector
#listinputs=listinputs+Timevector  or 
#R=calculateRUL(listofvariables=listinputs,Prm=Prm)
#print(R)

#initstate0=np.random.normal(stateTimeofPrediction[0],stddev_State[0], 1)
#initstate1=np.random.normal(stateTimeofPrediction[1],stddev_State[1], 1)
#initstate2=np.random.normal(stateTimeofPrediction[2],stddev_State[2], 1)
#initstate3=np.random.normal(stateTimeofPrediction[3],stddev_State[3], 1)



#statecurrent=[initstate0,initstate1,initstate2,initstate3]
statecurrent=stateTimeofPrediction

voltage=Prm.V0
t=timeofprediction

plotvariable_voltage=[voltage]
plotvariable_time=[t]

while(voltage>Prm.VEOD):

    t=t+1
    currentvalue=getinput(time=t,L=Loadvector,T=Timevector)
    newstate=stateupdateequation(listofstates=statecurrent,current=currentvalue,parameters=Prm)
    voltage=computevoltageforthreshold(listofstates=statecurrent,current=currentvalue,parameters=Prm)
    plotvariable_voltage.append(voltage)
    plotvariable_time.append(t)
    statecurrent=newstate


plt.plot(plotvariable_time,plotvariable_voltage)    
print("RUL Value is")
print(t)





