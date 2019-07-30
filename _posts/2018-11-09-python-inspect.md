---
layout:       post
title:        "Python Inspect"
subtitle: "python inspect"
date:         2018-11-09 19:32:00
author:       "Randle"
catalog:      true
comments: true
tags:
    - Python
---

## inspect 主要功能

inspect模块用于收集python对象的信息，主要几个功能： - 获取类或函数的参数的信息， - 源码， - 解析堆栈， - 对对象进行类型检查

## 获取参数信息

**getargspec(func)**

返回一个命名元组ArgSpect(args, varargs, keywords, defaults)，args是函数位置参数名列表，varargs是\*参数名，keywords是\**参数名，defaults是默认参数值的元组。

获取函数的特殊参数：

```python
import inspect
def attr_from_locals(locals_dict):
    self = locals_dict.pop('self')
    args = inspect.getargspec(self.__init__.__func__).args[1:]
    for k in args:
        setattr(self, k, locals_dict[k])
    keywords = inspect.getargspec(self.__init__.__func__).keywords
    if keywords:
        keywords_dict = locals_dict[keywords]
        for k in keywords_dict:
            setattr(self, k, keywords_dict[k])


class Foo(object):
    def __init__(self, name, **kwargv):
        attr_from_locals(locals())


f = Foo('bar', color='yellow', num=1)
print f.__dict__
```

返回结果：
```shell
    {'color': 'yellow', 'num': 1, 'name': 'bar'}
```


## 解析堆栈

先直接上代码
```python
import inspect
def tet(a):
    print inspect.stack()

def main():
    tet(1)

if __name__ == '__main__':
    main()
```

输出为：

```shell
    [
        FrameInfo(
            frame=<frame object at 0x1810d28>, 
            filename='log.py', 
            lineno=10, 
            function='tet', 
            code_context=['    print(inspect.stack())\n'], 
            index=0
            ), 
        FrameInfo(
            frame=<frame object at 0x7f50c006fa20>, 
            filename='log.py', 
            lineno=15, 
            function='main', 
            code_context=['    tet()\n'], 
            index=0
            ), 
        FrameInfo(
            frame=<frame object at 0x7f50c00f8828>, 
            filename='log.py', 
            lineno=21, 
            function='<module>', 
            code_context=['    main()\n'], 
            index=0
            )
    ]
```

可根据需要获得堆栈内容，譬如

```shell
inspect.stack()[0][3]
```


是指当前函数的名字，以此类推。此项功能在函数异常时可以很容易保存现场。

## 其他功能

getmembers(object[, predicate])

返回一个包含对象的所有成员的(name, value)列表。返回的内容比对象的**dict**包含的内容多，源码是通过dir()实现的。

predicate是一个可选的函数参数，被此函数判断为True的成员才被返回。

getmodule(object)

返回定义对象的模块

getsource(object)

返回对象的源代码

getsourcelines(object)

返回一个元组，元组第一项为对象源代码行的列表，第二项是第一行源代码的行号

ismodule,isclass,ismethod,isfunction,isbuiltin

一系列判断对象类型的方法，大都是包装了isinstance(object, types.FunctionType)之类语句的函数。

现在可以用类型判断来返回一个类的方法了：
```python
    class Foo(object):
        '''Foo doc'''
        def __init__(self, name):
            self.__name = name
    
        def getname(self):
            return self.__name
    
    inspect.getmembers(Foo, inspect.ismethod)

```

参考资料

1.  [Python标准库inspect](https://www.cnblogs.com/linxiyue/p/7989947.html)
2.  [python获取对象信息模块inspect](https://blog.csdn.net/csdn_kerrsally/article/details/80615109)
3.  [Python使用inspect查看代码参数](https://www.cnblogs.com/gjwork/p/4253925.html)
