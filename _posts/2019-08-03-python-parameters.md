---
layout: post
title: "python 函数参数写法"
subtitle: "python function parameters"
date: 2019-08-03 10:21:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Python
---

python 中，函数传入参数有两种写法：

1. 位置参数；
2. 关键字参数

# 位置参数

如下，函数的形参和实参按照位置对应。

```python
fun(1,2)
```

# 关键字参数

如下，按照形参关键字传入。

```python
func(name='han',age=18)
```

# 混合参数

在函数定义时不写明形参名，传入参数以后，args 时一个 tuple，kwargs 是一个 dict，可以按照相关方法引用其中的值。

```python
func(*args,**kwargs)
```

例：

```python
func(1,2,3,name='h',age=18)
```

那么：

```python
args=(1,2,3)
kwargs={
	'name':'h',
	'age':18
}
```
