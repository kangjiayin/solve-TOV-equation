# !/usr/bin/python3.9

# author:kangjiayin
# time:\now?
import json
import time
import math
# import matplotlib.pyplot as plt
tik=time.time()

# 尝试给出质量半径关系 
global step
global times
beta=0.03778
r_0=1.476
A_NR=2.4216
A_R=2.8663
step=0.01
times=2500
def ini(n):
    #summass is the tot mass of R
    global pressure
    global mass
    pressure=[]
    mass=[0]
    # print("----------------------------------------------------------------------")
    # print("----------------------------------------------------------------------")
    # print('---------------made by kangjiayin,powed by inertia--------------------')
    # print("----------------------------------------------------------------------")
    # print("----------------------------------------------------------------------")
    # print('pls input pressure in the middle,ps:try 0.01')
    pressure.append(float(n))


#epsilon是压强的函数，输入一个压强x
def epsilon(p):
    ###这里我老是报错，说是上边会出现虚数，我看了下也就是p的五分之三次方会产生虚数
    ###也就是说p在某种情况下变为负数了
    ###也就是下面我们计算下一个点质量的时候，因为精度限制，会跳到负值（只有p的导数是负的，所以只限制p就可以）
    ###所以加一个判断
    # if p<=0:
    #     p=1e-10
    out=A_NR*p**0.6+A_R*p
    return out

#质量对于半径的导数
def massRight(r,p):
    out=beta*r**2*epsilon(p)
    return out

#压强对于半径的导数
def pressureRight(r,m,p):
    #之前老是报错，说是不能除以0，我就把可能出0的地方改了改
    out=-r_0*epsilon(p)*(1+p/epsilon(p))*(m+beta*r**3*p)/(r**2-2*r_0*m*r)
    return out


#这个函数输入一个n，在此n处已知半径、压强、质量，我们能得到下一组半径、压强、质量
def getNext(n):
    #将r、m、p定下来，避免整个数组传参，影响运行速度
    r=rad[n]
    p=pressure[n]
    m=mass[n]
    #进行四阶Runge-Kutta近似
    #相较于正常的做了一些改动
    #km系列是对于质量mass的导数的估计值，kp系列是对于压强p导数的估计值
    km_1=massRight(r,p)
    kp_1=pressureRight(r,m,p)
    km_2=massRight(r+step/2,p+step/2*kp_1)
    kp_2=pressureRight(r+step/2,m+step/2*km_1,p+step/2*kp_1)
    km_3=massRight(r+step/2,p+step/2*kp_2)
    kp_3=pressureRight(r+step/2,m+step/2*km_2,p+step/2*kp_2)
    km_4=massRight(r+step,p+step*kp_3)
    kp_4=pressureRight(r+step,m+step*km_3,p+step*kp_3)
    ##############################################################
    new_m=m+(km_1+2*km_2+2*km_3+km_4)*step/6
    new_p=p+(kp_1+2*kp_2+2*kp_3+kp_4)*step/6
    #本来想整个精度的，但这样会收敛到0，报错，所以就不
    # new_m=round(m+(km_1+km_2+km_3+km_4)*step/6,10)
    # new_p=round(p+(kp_1+kp_2+kp_3+kp_4)*step/6,10)
    if new_p<0:
        new_p=p/2
    mass.append(new_m)
    pressure.append(new_p)


#制作一个半径的表格
def makerad():
    global rad
    rad=[]
    for i in range(times+1):
        rad.append(i*step+0.0001)


# def showtime():
#     print('请输入您要看的图像\n1.质量半径关系（一个中子星的）\n2.压强半径关系')
#     showwhat=int(input())
#     if showwhat==1:
#         plt.plot(rad,mass)
#         plt.ylabel(r'M/$\mathrm{M_\odot}$')
#     elif showwhat==2:
#         plt.plot(rad,pressure)
#     else:
#         plt.plot(rad,mass)
#         plt.plot(rad,pressure) 
#     plt.xlabel('r/km') 
#     plt.grid(True)
#     plt.show()

def main(n):
    ini(n)
    makerad()
    for j in range(times):
        getNext(j)
        #这里做一个判断若两次质量之差小于十的五次方，则认为这个中子星到头了，我们记录这个点的质量与半径
        #这里加了几条判断，我们认为没有太小的中子星（主要因为老是出接近0质量的中子星，没有意义）
        if mass[j]-mass[j-1]<1e-5 and j>50 and rad[j]>2:
            #将这个点的中子星半径与质量记录下来
            sumMass.append(mass[j])
            sumR.append(rad[j])
            break


    #showtime()


def truemain():
    #这两个变量记录质量半径关系
    global sumMass
    global sumR
    sumMass=[]
    sumR=[]
    filepre='inipre.json'
    with open(filepre) as preData: 
        ini_pressure=json.load(preData)
        for n in ini_pressure:
            main(n)
    #将这个质量半径关系数组输入文件
    MassData='MassData.json'
    RadData='RadData.json'
    with open(RadData,'w') as datarad: 
        json.dump(sumR, datarad)
    with open(MassData,'w') as datamass: 
        json.dump(sumMass, datamass)

truemain()

tik=round(time.time()-tik,0)
print("总用时为"+str(tik)+'s')