---
layout:       post
title:        "Markdown 实现页内跳转"
subtitle: "markdown jump in one page"
date:         2018-05-15 23:45:00
author:       "Randle"
catalog:      true
comments: true
tags:
    - Markdown
---

利用 Markdown 写文档的时候遇到一个问题，同一个页内跳转，下面这篇博客经过实验是靠谱的，下面简要的总结一下这个方法。

> [MarkDown技巧：两种方式实现页内跳转](https://www.cnblogs.com/JohnTsai/p/4027229.html)

实际理解是一种方式，锚点定义和跳转两个步骤。

<a id="1"></a>
# 锚点定义


```html
<h2 id="1">1.语法示例</h2>
<span id="jump">跳转到的地方</span>
<a id="jump">here</a>
```
<a id="2"></a>
# 跳转


[点击跳转到第一个标题](#1)

jump 对应锚点定义时候的 id，不加引号。

[点击跳转到第二个标题](#2)

**注** ： 这个方法在有道云笔记 Windows 客户端测试可行，网页版测试不能使用，跳转到一个空的标签页。本网站可以使用。