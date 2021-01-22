# !/usr/bin/python3.9

# author:kangjiayin
# time:\now?

import time
import math
import matplotlib.pyplot as plt
tik=time.time()

# 这个程序用来解TOV方程,输入初值p


#归一化系数
beta=0.03778
r_0=1.476
A_NR=2.4216
A_R=2.8663

def ini():
    global pressure
    global mass
    pressure=[]
    mass=[0]
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print('---------------made by kangjiayin,powed by inertia--------------------')
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")

    print('pls input pressure in the middle,ps:try 0.01')
    pressure.append(float(input()))


#epsilon是压强的函数，输入一个压强x
def epsilon(p):
    ###这里我老是报错，说是上边会出现虚数，我看了下也就是p的五分之三次方会产生虚数
    ###也就是说p在某种情况下变为负数了
    ###也就是下面我们计算下一个点质量的时候，因为精度限制，会跳到负值（只有p的导数是负的，所以只限制p就可以）
    ###所以加一个判断
    if p<=0:
        p=1e-10
    out=A_NR*p**0.6+A_R*p
    return out

#质量对于半径的导数
def massRight(r,p):
    out=beta*r**2*epsilon(p)
    return out

#压强对于半径的导数
def pressureRight(r,m,p):
    if r**2-2*r_0*m*r==0:
        m=m*1.00000000001
    out=-r_0*epsilon(p)*(1+p/epsilon(p))*(m+beta*r**3*p)/(r**2-2*r_0*m*r)
    return out


#这个函数输入一个n，在此n处，已知半径、压强、质量，我们能得到下一组半径、压强、质量
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
    global step
    global times
    rad=[]
    step=0.01
    times=2500
    for i in range(times+1):
        rad.append(i*step+0.0001)


def showtime():
    print('请输入您要看的图像\n1.质量半径关系（一个中子星的）\n2.压强半径关系')
    showwhat=int(input())
    if showwhat==1:
        plt.plot(rad,mass)
        plt.ylabel(r'M/$\mathrm{M_\odot}$')
    elif showwhat==2:
        plt.plot(rad,pressure)
    else:
        plt.plot(rad,mass)
        plt.plot(rad,pressure) 
    plt.xlabel('r/km') 
    plt.grid(True)
    plt.show()

def main():
    ini()
    makerad()
    for j in range(times):
        getNext(j)
    showtime()


main()



tik=round(time.time()-tik,0)
print("总用时为"+str(tik)+'s')
#有很多算力浪费