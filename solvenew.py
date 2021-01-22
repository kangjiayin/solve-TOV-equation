# !/usr/bin/python3.9

# author:kangjiayin
# time:\now?
import json
import time
import math
# import matplotlib.pyplot as plt
tik=time.time()
beta=0.03778
r_0=1.476
A_NR=2.4216
A_R=2.8663
step=0.01
times=2500
def ini(n):
    global pressure
    global mass
    pressure=[]
    mass=[0]
    pressure.append(float(n))


def epsilon(p):
    if p<=0:
        p=1e-10
    out=A_NR*p**0.6+A_R*p
    return out

def massRight(r,p):
    out=beta*r**2*epsilon(p)
    return out

def pressureRight(r,m,p):
    if r**2-2*r_0*m*r==0:
        m=m*1.00000000001
    out=-r_0*epsilon(p)*(1+p/epsilon(p))*(m+beta*r**3*p)/(r**2-2*r_0*m*r)
    return out

def getNext(n):
    r=rad[n]
    p=pressure[n]
    m=mass[n]
    km_1=massRight(r,p)
    kp_1=pressureRight(r,m,p)
    km_2=massRight(r+step/2,p+step/2*kp_1)
    kp_2=pressureRight(r+step/2,m+step/2*km_1,p+step/2*kp_1)
    km_3=massRight(r+step/2,p+step/2*kp_2)
    kp_3=pressureRight(r+step/2,m+step/2*km_2,p+step/2*kp_2)
    km_4=massRight(r+step,p+step*kp_3)
    kp_4=pressureRight(r+step,m+step*km_3,p+step*kp_3)
    new_m=m+(km_1+2*km_2+2*km_3+km_4)*step/6
    new_p=p+(kp_1+2*kp_2+2*kp_3+kp_4)*step/6
    if new_p<0:
        new_p=p/2
    mass.append(new_m)
    pressure.append(new_p)

def makerad():
    global rad
    rad=[]
    for i in range(times+1):
        rad.append(i*step+0.0001)

def main(n):
    ini(n)
    makerad()
    for j in range(times):
        getNext(j)
        if mass[j]-mass[j-1]<1e-5 and j>50 and rad[j]>2:
            sumMass.append(mass[j])
            sumR.append(rad[j])
            break

def truemain():
    global sumMass
    global sumR
    sumMass=[]
    sumR=[]
    filepre='inipre.json'
    with open(filepre) as preData: 
        ini_pressure=json.load(preData)
        for n in ini_pressure:
            main(n)
    MassData='MassData.json'
    RadData='RadData.json'
    with open(RadData,'w') as datarad: 
        json.dump(sumR, datarad)
    with open(MassData,'w') as datamass: 
        json.dump(sumMass, datamass)
truemain()
tik=round(time.time()-tik,0)
print("总用时为"+str(tik)+'s')