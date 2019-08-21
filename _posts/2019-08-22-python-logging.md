---
layout: post
title: "python logging"
subtitle: "python logging"
date: 2019-08-22 00:05:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Python
---

`logging` 是 python 中一个很有用的模块，在此记录一下常用的用法，参考资料中的链接，写的很详细也很明白，有时间再做翻译转载。

其中有一个问题需要注意，在`logging`中，`logger`和`handler`都有`level`的属性，`logger`若没有设置`level`，则会继承 `root logger` 的`level`属性，而`root logger`的默认`level`属性为`WARNING`，所以若没有设置，会发生比`WARNING`严重程度低的日志不能打印的情况。

每个`logger`可以有多个`handler`，每条日志会先经过`logger`的`level`过滤，才到`handler`的`level`过滤，所以在自定义`logger`的时候，注意设定其`level`属性。


# 参考资料
[Logging in Python](https://realpython.com/python-logging/)