# !/usr/bin/python3.9

# author:kangjiayin
# time:\now?
import json
import matplotlib.pyplot as plt

mass='MassData.json'
rad='RadData.json'
with open(mass) as md: 
    m=json.load(md)
with open(rad) as rd: 
    r=json.load(rd)

plt.plot(r,m)
plt.xlabel('r/km',fontsize=20)
plt.ylabel(r'M/$\mathrm{M_\odot}$',fontsize=20)
plt.xlim(5,25) 
plt.grid(True)  
plt.show()