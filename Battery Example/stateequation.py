from math import exp,sqrt
from Parameters import params
import numpy as np

# https://github.com/nasa/PrognosticsModelLibrary
# https://github.com/nasa/PrognosticsModelLibrary/tree/master/MATLAB/%2BBatteryCircuit


def getinput(time,L,T):
  
#     for x in range(0,len(T)):
#         if time<=T[x]:
#             return L[x]
     return 2        


    
def stateupdateequation(listofstates,current,parameters):

    Tb = listofstates[0]
    qb = listofstates[1]    
    qcp = listofstates[2]
    qcs = listofstates[3]
    
    i = current
    
    Vcs = qcs/parameters.Cs;
    Vcp = qcp/parameters.Ccp;
    SOC = (parameters.CMax - parameters.qMax + qb)/parameters.CMax;
    Cb = parameters.Cbp0*SOC*SOC*SOC + parameters.Cbp1*SOC*SOC + parameters.Cbp2*SOC + parameters.Cbp3;
    Rcp = parameters.Rcp0 + parameters.Rcp1*exp(parameters.Rcp2*(-SOC + 1));
    Vb = qb/Cb;
    Tbdot = (Rcp*parameters.Rs*parameters.ha*(parameters.Ta - Tb) + Rcp*Vcs*Vcs*parameters.hcs + parameters.Rs*Vcp*Vcp*parameters.hcp)/(parameters.Jt*Rcp*parameters.Rs);
    Vp = Vb - Vcp - Vcs;
    ip = Vp/parameters.Rp;
    ib = i + ip;
    icp = ib - Vcp/Rcp;
    qcpdot = icp;
    qbdot = -ib;
    ics = ib - Vcs/parameters.Rs;
    qcsdot = ics;

    
    
    new0 = Tb + Tbdot*parameters.dt;
    new1 = qb + qbdot*parameters.dt;
    new2 = qcp + qcpdot*parameters.dt;
    new3 = qcs + qcsdot*parameters.dt;
    
    #new0 = Tb + Tbdot*parameters.dt + np.random.normal(0,sqrt(parameters.PN0), 1);
    #new1 = qb + qbdot*parameters.dt + np.random.normal(0,sqrt(parameters.PN1), 1);
    #new2 = qcp + qcpdot*parameters.dt + np.random.normal(0,sqrt(parameters.PN2), 1);
    #new3 = qcs + qcsdot*parameters.dt + np.random.normal(0,sqrt(parameters.PN3), 1);
    
    newstate = [new0, new1, new2, new3]
    
    return newstate

def computevoltageforthreshold(listofstates,current,parameters):


    
    Tb = listofstates[0]
    qb = listofstates[1]    
    qcp = listofstates[2]
    qcs = listofstates[3]
    
    i = current
    
    Vcs = qcs/parameters.Cs;
    Vcp = qcp/parameters.Ccp;
    SOC = (parameters.CMax - parameters.qMax + qb)/parameters.CMax;
    Cb = parameters.Cbp0*SOC*SOC*SOC + parameters.Cbp1*SOC*SOC + parameters.Cbp2*SOC + parameters.Cbp3;
    Rcp = parameters.Rcp0 + parameters.Rcp1*exp(parameters.Rcp2*(-SOC + 1));
    Vb = qb/Cb;
    Tbdot = (Rcp*parameters.Rs*parameters.ha*(parameters.Ta - Tb) + Rcp*Vcs*Vcs*parameters.hcs + parameters.Rs*Vcp*Vcp*parameters.hcp)/(parameters.Jt*Rcp*parameters.Rs);
    Vp = Vb - Vcp - Vcs;

    return Vp