# !/usr/bin/python3.9

# author:kangjiayin
# time:\now?


# this program is for integral
import math
import time

# 思路简介
# 打算做一个数值积分程序，思路如下：
# 用户输入一个函数，若不输入，默认为某个指定函数；
# 用户输入积分上下限与需求精度（这里应该输入成对数），根据此我们可以估算需要分割多少次；
# 貌似上一个不太容易实现，那就让用户指定分割次数；
# 接下来就是算梯形面积，求和；

##先做一维的

def ini():
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("====================积分程序正在初始化====================")
    print("====================powered by kang====================")
#为了界面美观，加点废话
    print("选择你的积分函数\n1.默认\n2.自定义函数")
    print("你的选择为：",end="")
    global myFuction
    myFuction="8*x**2"
#这里可以选择自定义函数或者使用默认函数
    if str(input())==str(2):
        print("==============================请输入时遵循如下规则==============================")
        print("====================  加 减 乘 除 乘方 分别表示为 + - * / **  ====================")
        print("===如需其他函数，请引用math库的函数规则进行输入，如三角函数可以表示为math.sin()或math.exp()等等===")
        print('例如：',myFuction)
        print('请输入你的函数=  ',end="")
        myFuction=input()
    else:
        print("使用默认函数积分,默认函数=8*x**2")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    #设定一个全局变量myData，储存积分上下限和划分情况
    global myData
    myData=[]
    print("请输入积分下限：",end='')
    myData.append(float(input()))
    print("请输入积分上限：",end='')
    myData.append(float(input()))
    print("请输入划分次数：",end='')
    myData.append(int(abs(float(input()))))
    #防止下分成0段出错
    if myData[2]==0:
        myData[2]=1
        print('不能划分为0段，已切换为1')
    #防止积分上下限输反
    if myData[1] < myData[0]:
        exchange=myData[1]
        myData[1]=myData[0]
        myData[0]=exchange



def users_fuction(x):
    #print('Begin your jurny!')
    #这个函数是程序中用户设定的函数的指代函数，输入一个点，给出这个函数在这个点的值
    x=float(x)
    #print(myFuction)
    output=eval(myFuction)
    return output

def maketable():
    #制作一个每个点对应函数值的表格
    global tabley
    global delta
    delta=(myData[1]-myData[0])/myData[2]
    tabley=[]
    for i in range(myData[2]+1): 
        x=myData[0]+i*delta
        y=users_fuction(x)
        tabley.append(y)
    
        
def sum():
    #根据表格算梯形面积
    global tot
    tot=0
    for i in range(myData[2]): 
        tot+=(tabley[i]+tabley[i+1])*delta/2
    
def main():
    ini()
    begin=time.time()
    maketable()
    print("----------------------------------------------------------------")
    sum()
    begin=time.time()-begin
    print("----------------------------------------------------------------")
    print("从"+str(myData[0])+"到"+str(myData[1])+"，对函数= "+myFuction+' 积分')
    print("结果为   "+str(tot))
    print("----------------------------------------------------------------")
    print('总用时为'+str(round(begin,0))+'s')

main()