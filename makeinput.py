# !/usr/bin/python3.9

# author:kangjiayin
# time:\now?

#制作需要的压强列表
import json
filepre='inipre.json'
pre=[]

##遍历压强从0到2000
for i in range(200000):
    step=0.005
    new=round((i+1)*step,3)
    pre.append(new)
#写入文件
with open(filepre,'w') as preData: 
    json.dump(pre, preData)

# with open(filepre) as preData: 
#     #json.dump(pre, preData)
#     aa=json.load(preData)
