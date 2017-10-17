#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 00:18:48 2017

@author: Shankar
"""

# FirstSetupParameters    
class params(object):

    #Basics
    dt=1
    Id = 2.02;
    td = 3850;
    V0 = 4.183;
    qd = Id*td;
    #If Cb was linear then: Cb = qd/Vd; but Cb is not linear so guessing that
    # initial charge is more than qd it must be large enough such that CbEnd >Cb0
    q0 = 1.0102*qd;
    #And assuming that "max" charge is initial charge (when qMax==qb SOC is 1)
    qMax = q0;
    # When qMax-qb=qd, SOC is 0 if CMax is the following (=qd) (CMax here is
    # more like max current that can be drawn, like a qdMax)
    CMax = qMax - (q0-qd);
    # Given those assumptions assumption it follows that
    Cb0 = q0/V0;
    
    # Then we can set the following:
    V0 = 4.183;       # nominal battery voltage
    Rp = 1e4;         # battery parasitic resistance
    qMax = qMax;      # max charge
    CMax = CMax;      # max capacity
    
    # Capacitance
    Cb0 = Cb0;        # battery capacitance
    Cbp0 = -230;
    Cbp1 = 1.2;
    Cbp2 = 2079.9;
    Cbp3 = Cb0-(Cbp0+Cbp1+Cbp2);
    
    # R-C pairs
    Rs = 0.0538926;
    Cs = 234.387;
    Rcp0 = 0.0697776;
    Rcp1 = 1.50528e-17;
    Rcp2 = 37.223;
    Ccp = 14.8223;
    
    #% Temperature parameters
    Ta = 18.95;      # ambient temperature (deg C)
    Jt = 800;
    ha = 0.5;        # heat transfer coefficient, ambient
    hcp = 19;
    hcs = 1;
    
    # End of discharge voltage threshold
    VEOD = 3.2;
    
    #Default initial states (fully charged)
    Init1 = Cb0*V0;
    Init2 = 0;
    Init3 = 0;
    Init0 = Ta;
    
    # Process noise variances
    PN1 = 1e-1;
    PN2 = 1e-2;
    PN3 = 1e-2;
    PN0 = 1e-5;
    
    # Sensor noise variances
    SN0 = 1e-3;
    SN1 = 1e-3;