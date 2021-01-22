# Brief Introduction
[toc]
ps:write in python3,noted by Chinese.
## Environment
* cpu:Apple M1
* sys:Macos Big Sur
* Compiler:python3.9
* model:math\time\json\pyplot
## Integral Program
Just a normal integral program.
Use terminal:
```bash
python3 int.py
```
Follow the order and you will draw the conclusion.
## Sovle TOV Equation
The most widely known member of the Runge–Kutta family is generally referred to as "RK4", the "classic Runge–Kutta method" or simply as "the Runge–Kutta method".

And we use this method to solve this Equation.
* Running `solve.py` will ask you to give a pressure in the middle of nuestar, and will ask you to chioce which picture you are likely to get.
* Befor run `solvenew.py` or `solve_new_.py`( two programs will draw the same file), you should run `inipre.py` to initial.
* Running `makeinput.py` will write a file whose name is `inipre.json`. `inipre.json` include all the initialize pressure.
* Then you can run `solvenew.py`, it will takes about two hours.
* In the end, you can run `show.py` to show the relation between mass and rad.