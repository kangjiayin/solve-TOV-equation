# 程序简介
## 环境
* cpu:Apple M1
* 系统:Macos Big Sur
* 解释器:python3.9
* 库:math\time\json\pyplot
## 积分程序
直接用Python3解释即可。
## 解TOV方程
使用四阶龙格-库塔算法。

* 运行`solve.py`根据提示给定中心压强，输出压强、质量随着半径变化的图像；
* 运行`solvenew.py`**前**先得运行初始化程序 `inipre.json`；
* 运行`solvenew.py`给出一组一组可能的中子星质量与半径的组合，输入两个json文件，可能需要两个小时；
* 最后运行`show.py`画出图像。
