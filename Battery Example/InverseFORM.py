#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 04:41:00 2017

@author: Shankar
"""

from stateequation import stateupdateequation, computevoltageforthreshold,getinput
from RULPredictor import calculateRUL
from Parameters import params
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from math import sqrt


def convertoriginaltostd(X,Means,StdDev):
    
    U=[0,0,0,0,0]
    for i in range(0,len(X)):
        U[i]=(X[i]-Means[i])/StdDev[i]
        
    return U
    
    
def convertstdtooriginal(U,Means,StdDev):
    
    X=[0,0,0,0,0]
    for i in range(0,len(U)):
        X[i]=U[i]*StdDev[i]+Means[i]
        
    return X


Prm=params()
Means=[Prm.Init0,Prm.Init1,Prm.Init2,Prm.Init3,2]
StdDev=[Prm.Init0*0.1,Prm.Init1*0.1,0.1,0.1,0.2]



# For a given probability, what is the RUL value
Probability_Value=0.1
## P(RUL<=number) = Probability_Value, what is the number?

beta=0-norm.ppf(Probability_Value)



derivative=[0,0,0,0,0]
alpha=[0,0,0,0,0]

Old_U=[0,0,0,0,0]

continue_counter=1

while(continue_counter==1 or continue_counter=='1' ):
    Old_X=convertstdtooriginal(U=Old_U,Means=Means,StdDev=StdDev)
    Gfunction=calculateRUL(Old_X,Prm)
    perturb=0.01
    
    for i in range(0,len(Old_X)):
        
        argument=Old_X
        argument[i]=argument[i]+perturb
        perturbGfunction=calculateRUL(argument,Prm)
        derivative[i]=(perturbGfunction-Gfunction)/perturb
        alpha[i]=derivative[i]*StdDev[i]
    
    
    normvalue=np.linalg.norm(np.array(alpha))
    
    Array_OldU=np.array(Old_U)
    Array_alpha=np.array(alpha)
    New_U=-Array_alpha*beta/normvalue
    Old_U=New_U
    print(Gfunction)
    print(Old_X)
    continue_counter=input("Would you like to continue (if so, say 1)?")




