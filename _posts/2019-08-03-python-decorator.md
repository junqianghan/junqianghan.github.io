---
layout: post
title: "python 装饰器"
subtitle: "python decorator"
date: 2019-08-03 09:45:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Python
---

在阅读 python 项目源码的时候，经常能够遇到 `@decorator` 的用法，本文对 python 的装饰器(decorator) 功能进行总结。

按照被装饰对象的类型，装饰器可以分为两类：

1. function decorator
2. class decorator

装饰器本身是一个可调用对象，输入 `function` 或者 `class`，装饰器返回一个被修改的`function` 或者`class`，这个过程中，`function`或者`class`可能被调用，但是其内部定义不会被修改。

即下面两种写法是等价的。

```python
@decorator
func()

func = decorator(func)
```

首先从函数装饰器谈起。

# 函数装饰器

**被装饰函数无参数**

```python
def decorator(func):
    def wrapper():
        print 'before'
        func()
        print 'after'
    return wrapper

@decorator
def func():
    print 'hello'
```

经过`decorator`的装饰，函数`func`的定义，已经被替换为`wrapper`，但是其函数名没有变。装饰后的函数在之前`func`执行的前后增加了一些操作，但是并没有改变其内部的定义。

**被装饰函数有参数**

```python
def decorator(func):
    def wrapper(a,b):
        print 'before func'
        func(a,b)
        print 'after func'
    return wrapper

@decorator
def myadd(a,b):
	return a+b
```
与前面被修饰函数无参数没有本质区别，分析方法相同。

**修饰器带参数**

```python
def decorator(arg):
    def _decor(func):
        def wrapper():
            print 'before func'
            func()
            print 'after func'
        return wrapper
    return _decor

@decorator('arg')
def func():
    print 'hello'
```

这种情况理解起来也很容易，`decorator('arg')`的返回结果时一个装饰器，即上述装饰器写法等价于：

```python
func = decorator('arg')(func)
```

当然，这种写法就可以实现，根据输入参数的不同，可以配置不同的装饰器。

**装饰器为类**

```python
class decorator:
    def __init__(self,func):
        self.func = func
    
    def __call__(self):
        print 'before call'
        return self.func

@decorator
def func():
    print 'hello'
```

装饰器本身是一个类，其构造函数能够接受参数，所以经过`decorator`之后，`func`是`decorator`类的一个对象，其拥有可调用方法，仍然是一个可调用对象。

# 类装饰器

`decorator`不仅能够作用于函数，还能作用于类，考虑下面的情况；

```python
def time_this(original_function):
    print "decorating"
    def new_function(*args,**kwargs):
        print "starting timer"
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args,**kwargs)
        after = datetime.datetime.now()
        print "Elapsed Time = {0}".format(after-before)
        return x
    return new_function
```
`time_this` 是一个decorator，用来额外统计函数的执行时间，那么，对于下面的情况，写法上就有些繁琐了。

```python
class ImportantStuff(object):
    @time_this
    def do_stuff_1(self):
        ...
    @time_this
    def do_stuff_2(self):
        ...
    @time_this
    def do_stuff_3(self):
        ...
```

所以，希望有一种装饰器，能够一次包装类内的所有函数。当不需要包装的时候，可以通过一行注释取消。如下：
```python
@time_all_class_methods
class ImportantStuff:
    def do_stuff_1(self):
        ...
    def do_stuff_2(self):
        ...
    def do_stuff_3(self):
        ...
```
这种装饰器写法，与前文的函数装饰器写法，作用基本相同，相同与下面这种写法：
```python
ImportantStuff = time_all_class_methods(ImportantStuff)
```
`time_all_class_methods`作为装饰器，要求能够输入类作为参数，同时返回一个类类型。实现方法参考下面的写法。
```python
def time_this(original_function):      
    print "decorating"                      
    def new_function(*args,**kwargs):
        print "starting timer"       
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print "Elapsed Time = {0}".format(after-before)      
        return x                                             
    return new_function  

def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            self.oInstance = Cls(*args,**kwargs)
        def __getattribute__(self,s):
            """
            this is called whenever any attribute of a NewCls object 
            is accessed. This function first tries to get the 
            attribute off NewCls. 
            If it fails then it tries to fetch the attribute from
            self.oInstance (an instance of the decorated class). 
            If it manages to fetch the attribute from self.oInstance, 
            and the attribute is an instance method then `time_this` 
            is applied.
            """
            try:    
                x = super(NewCls,self).__getattribute__(s)
            except AttributeError:      
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__): # it is an instance method
                return time_this(x)            # this is equivalent of 
                                               # just decorating the
                                               # method with time_this
            else:
                return x
    return NewCls

#now lets make a dummy class to test it out on:

@time_all_class_methods
class Foo(object):
    def a(self):
        print "entering a"
        import time
        time.sleep(3)
        print "exiting a"

oF = Foo()
oF.a()
```

`time_all_class_methods`装饰器对被装饰的类，所有的函数都调用了`time_this`，对所有的成员变量不作处理，直接返回。

可见，类装饰器和函数装饰器的原理是相同的，只是对于装饰器来说，一个输入的是类，一个输入的是函数。

装饰器的返回其实没有限制，因为装饰器本身只是一个可调用对象，它可以返回任何类型。但是，装饰器的初衷是"装饰"。所以，函数装饰器会返回函数，而类装饰器会返回类。

# 常见装饰器

`python`内建了很多实用装饰器[^built-in-decorator]，很实用。本小节对其功能简要描述，其原理不做赘述。

1. @property
2. @classmethod
3. @staticmethod

**property**

Python内置的`@property`装饰器负责把一个方法变成属性调用：

```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```
把一个`getter`方法变成属性，只需要加上`@property`就可以了，此时，`@property`本身又创建了另一个装饰器`@score.setter`，负责把一个`setter`方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

```python
>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```
只定义`getter`方法，不定义`setter`方法是一个只读属性：
```python
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth
```
上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

**classmethod vs staticmethod**

`classmethod`和`staticmethod`都是类级别的方法，简单理解，调用这两种方法的时候，不需要实例化的对象，直接通过类名使用。类级别的方法，在类定义时就存在。

同样，通过实例理解其用法：
```python
class A(object):
    def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x    

a = A()
```
最基本的用法是，通过实例化的对象访问类方法：
```python
a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)
```
实例化对象`a`隐式传递给第一个参数`self`。

对于`staticmethod`方法，`self`和`cls`这两个参数都不需要，可以通过类或者实例化的对象调用。与普通函数相比，静态函数可以调用类里的静态变量。`staticmethod`经常用于处理一些有关类的相同操作。

```python
a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)
```

对于`classmethod`对象的类名被隐式传递给函数的第一个参数`cls`，下面的两种用法是相同的：
```python
a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)

A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
```

`classmethod`最大的有点在于，与`method`绑定的第一个参数是实际的类，在继承体系中，子类继承父类的`classmethod`，不同的子类中，`cls`是不同的，对于工厂模式的实现非常便利。

再谈到前面的实例，三种类型的`method`，查看其类型，可以得到下面的结果：
```python
print(a.foo)
# <bound method A.foo of <__main__.A object at 0xb7d52f0c>>

print(a.class_foo)
# <bound method type.class_foo of <class '__main__.A'>>

print(a.static_foo)
# <function static_foo at 0xb7d479cc>
```
可见，`foo`和`class_foo`分别与`object`和`class`有绑定关系，但是`static_foo`没有绑定关系，是一个普通函数类型。

此处再赘述一个`classmethod`的用法，除了前面提到的工厂模式实现，下面这个用法也是很有趣的。

```python
class PrintNum(object):
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def print_num(self):
        print self.num1,self.num2,self.num3
```
`PrintNum`类接受三个数，提供打印方法。但是如果我们传入的参数时一个`list`而不是三个数，怎么便捷处理呢？除了增加一个构造函数，可以增加一个`classmethod`：
```python
class PrintNum(object):
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    @classmethod
    def list_to_num(cls,threenum):
        return cls(threenum[0],threenum[2],threenum[3])
    
    ......
```

> `list_to_num`输入一个`list`返回了一个对象，这得益于其`cls`参数。

# 参考资料

- [python装饰器--原来如此简单](https://blog.csdn.net/u013858731/article/details/54971762)
- https://www.python-course.eu/python3_decorators.php
- https://data-flair.training/blogs/python-decorator/
- [Introduction to Python Decorators](https://www.codementor.io/sheena/introduction-to-decorators-du107vo5c)
- [Advanced Uses of Python Decorators](https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv)
- [python super 函数](https://www.runoob.com/python/python-func-super.html)
- [使用@property](https://www.liaoxuefeng.com/wiki/897692888725344/923030547069856)
- [classmethod类方法跟staticmethod静态方法](https://blog.csdn.net/ljt735029684/article/details/80714274)

[^built-in-decorator]: [awesome-python-decorator](https://github.com/lord63/awesome-python-decorator)


