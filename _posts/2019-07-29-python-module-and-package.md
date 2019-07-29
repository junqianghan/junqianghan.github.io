---
layout:       post
title:        "python 模块和包"
subtitle: "python module and package"
date:         2019-07-29 13:38:00
author:       "Randle"
catalog:	true
mathjax:	false
comments:	true
tags:
    - Python
---

# 模块(module)

Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。比如:

```python
# func_add.py
def add(a,b):
    return a+b
```

# 包(package)

包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包。

考虑如下 `compute` 的包结构，test.py 为测试调用包的代码：

```python
test.py
compute
|---__init__.py
|---addFunc.py
|---subFunc.py
|---multiFunc.py
|---divFunc.py
```
## init

`__init__.py`,可以作为包的初始化例程执行, 也可以当做主程序运行, 如下所示:

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    print '作为主程序运行'
else:
    print 'compute 初始化'
```

测试:

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入 Phone 包
from compute.addFunc import myadd
from compute.subFunc import mysub
 
myadd(1,2)
mysub(4,3)
```

结论:

```shell
compute 初始化
I'm in myadd
I'm in mysub
```

第一次导入包的时候， 初始化例程被执行。

# all

`__all__`变量是一个列表，可以在模块中和`__init__.py`中使用。
`__all__`变量结合`from  ... import *`语句使用，`__all__`变量就是控制`*`所表示要引入的东西（模块，函数，类等）。

## 模块中使用__all__

如果在模块中使用`__all__`变量，如下所示：

```python
__all__ = ['add1']     #只导入add1，而不会导入add2
 
def add1(*variaties):
    sum = 0
    for i in variaties:
        sum += i
    return sum
```
在导入该模块下的所有函数时，只会导入列表中声明的函数：

```python
from compute.addFunc import *
print(add1(1,1))
```
使用其他函数会报错。

## init 中使用 __all__

如果在`__init__.py`模块中设置`__all__`变量，则列表内容规定了`import *`所导入的模块。我们在compute下的`__init__.py`模块中添加`__all__`变量，如下所示：

```python
__all__ = ['addFunc','divFunc','mulFunc'] #列表中填写被引入模块的名称
```

然后在import * 时，只引入被声明的模块。

```python
from compute import *
print(divFunc.div(2,3))
print(addFunc.add1(1,2))
print(addFunc.add2(1,2))
print(mulFunc.mul(2,3))
```
而没有被声明的subFunc.py模块则不能使用。


---
# 参考资料

- [Python 模块](https://www.runoob.com/python/python-modules.html)
- [自定义包结构及__init__.py模块和__all__变量的使用](https://blog.csdn.net/qq_32166627/article/details/59481503)