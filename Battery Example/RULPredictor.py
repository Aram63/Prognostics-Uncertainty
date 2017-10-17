#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 02:58:51 2017

@author: Shankar
"""
from stateequation import stateupdateequation, computevoltageforthreshold,getinput

def calculateRUL(listofvariables,Prm):
    
    
    timeofprediction=0
    stateTimeofPrediction=listofvariables[0:4]
    #Loadvector=listofvariables[5:11]    #[2,3,4,5,2,1]
    #Timevector=listofvariables[11:17]   #[200, 500, 1000, 2000, 3000, 10000]
    
    t=timeofprediction
    
    statecurrent=stateTimeofPrediction

    voltage=Prm.VEOD+1
    while(voltage>Prm.VEOD):

        t=t+1
        #currentvalue=getinput(time=t,L=Loadvector,T=Timevector)
        currentvalue=listofvariables[4]
        newstate=stateupdateequation(listofstates=statecurrent,current=currentvalue,parameters=Prm)
        voltage=computevoltageforthreshold(listofstates=statecurrent,current=currentvalue,parameters=Prm)
        statecurrent=newstate
    
    
    return t
    