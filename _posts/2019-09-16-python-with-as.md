---
layout: post
title: "Python With As 使用方法"
subtitle: "Python with as introduction"
date: 2019-09-16 23:10:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Python
---
# with 语句是什么
有一些任务，可能事先需要设置，事后做清理工作。对于这种场景，Python的`with`语句提供了一种非常方便的处理方式。一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。
如果不用`with`语句，代码如下：
```python
file = open("/tmp/foo.txt")
data = file.read()
file.close()
```
这里有两个问题。一是可能忘记关闭文件句柄；二是文件读取数据发生异常，没有进行任何处理。下面是处理异常的加强版本：
```python
file = open("/tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()
```
虽然这段代码运行良好，但是太冗长了。这时候就是`with`一展身手的时候了。除了有更优雅的语法，`with`还可以很好的处理上下文环境产生的异常。下面是`with`版本的代码：
```python
with open("/tmp/foo.txt") as file:
    data = file.read()
```

# with 如何工作
这看起来充满魔法，但不仅仅是魔法，Python对`with`的处理还很聪明。基本思想是`with`所求值的对象必须有一个`__enter__()`方法，一个`__exit__()`方法。
紧跟`with`后面的语句被求值后，返回对象的`__enter__()`方法被调用，这个方法的返回值将被赋值给`as`后面的变量。当`with`后面的代码块全部被执行完之后，将调用前面返回对象的`__exit__()`方法。

下面例子可以具体说明`with`如何工作：
```python
#!/usr/bin/env python
# with_example01.py
 
class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
 
    def __exit__(self, type, value, trace):
        print "In __exit__()"
 
def get_sample():
    return Sample()
 
with get_sample() as sample:
    print "sample:", sample
```
运行代码，输出如下:
```shell
In __enter__()
sample: Foo
In __exit__()
```
正如你看到的:
1. `__enter__()`方法被执行
2. `__enter__()`方法返回的值(这个例子中是`Foo`，赋值给变量`sample`
3. 执行代码块，打印变量`sample`的值为`Foo`
4. `__exit__()`方法被调用

`with`真正强大之处是它可以处理异常。可能你已经注意到`Sample`类的`__exit__`方法有三个参数(`val`, `type` 和 `trace`)。 这些参数在异常处理中相当有用。我们来改一下代码，看看具体如何工作的。
```python
#!/usr/bin/env python
# with_example02.py
 
class Sample:
    def __enter__(self):
        return self
 
    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace
 
    def do_something(self):
        bar = 1/0
        return bar + 10
 
with Sample() as sample:
    sample.do_something()
```
这个例子中，`with`后面的`get_sample()`变成了`Sample()`。这没有任何关系，只要紧跟`with`后面的语句所返回的对象有`__enter__()`和`__exit__()`方法即可。此例中，`Sample()`的`__enter__()`方法返回新创建的`Sample`对象，并赋值给变量`sample`。
代码执行后：
```shell
bash-3.2$ ./with_example02.py
type: <type 'exceptions.ZeroDivisionError'>
value: integer division or modulo by zero
trace: <traceback object at 0x1004a8128>
Traceback (most recent call last):
  File "./with_example02.py", line 19, in <module>
    sample.do_something()
  File "./with_example02.py", line 15, in do_something
    bar = 1/0
ZeroDivisionError: integer division or modulo by zero
```
实际上，在`with`后面的代码块抛出任何异常时，`__exit__()`方法被执行。正如例子所示，异常抛出时，与之关联的`type`，`value`和`stack trace`传给`__exit__()`方法，因此抛出的`ZeroDivisionError`异常被打印出来了。开发库时，清理资源，关闭文件等等操作，都可以放在`__exit__`方法当中。
因此，Python的`with`语句提供了一个有效的机制，让代码更简练，同时在异常产生时，清理工作更简单。

# 参考资料
- https://www.cnblogs.com/DswCnblog/p/6126588.html
- http://effbot.org/zone/python-with-statement.htm
- https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/