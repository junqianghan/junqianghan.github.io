---
layout:       post
title:        'Linux 开源框架学习'
subtitle: "linux opensource frame"
date:         2018-05-15 00:10:00
author:       "Randle"
catalog:      true
comments: true
tags:
    - Linux
    - OpenSource
    - C
---
> [在学习linux下的C编程，想下载一些linux下的程序源码研究学习，应该去哪获得？
](https://www.zhihu.com/question/20681995)

有一些比较好的开源框架可以学习，比如：
## 1. Webbench
Webbench 是一个在linux下使用的非常简单的网站压测工具。它使用fork()模拟多个客户端同时访问我们设定的URL，测试网站在压力下工作的性能，最多可以模拟3万个并发连接去测试网站的负载能力。Webbench使用C语言编写, 代码实在太简洁，源码加起来不到600行。

下载链接：[LippiOuYang/WebBench · GitHub](https://github.com/EZLippi/WebBench)

## 2. Tinyhttpd
tinyhttpd 是一个超轻量型Http Server，使用C语言开发，全部代码只有502行(包括注释)，附带一个简单的Client，可以通过阅读这段代码理解一个 Http Server 的本质。

下载链接：[LippiOuYang/Tinyhttpd · GitHub](https://github.com/EZLippi/Tinyhttpd)

## 3. cJSON
cJSON 是C语言中的一个JSON编解码器，非常轻量级，C文件只有500多行，速度也非常理想。cJSON也存在几个弱点，虽然功能不是非常强大，但cJSON的小身板和速度是最值得赞赏的。其代码被非常好地维护着，结构也简单易懂，可以作为一个非常好的C语言项目进行学习。

项目主页:[cJSON | SourceForge.net](https://sourceforge.net/projects/cjson/)

## 4. CMockery
cmockery 是google发布的用于C单元测试的一个轻量级的框架。它很小巧，对其他开源包没有依赖，对被测试代码侵入性小。cmockery的源代码行数不到3K，你阅读一下will_return和mock的源代码就一目了然了。主要特点：免费且开源，google提供技术支持；轻量级的框架，使测试更加快速简单；避免使用复杂的编译器特性，对老版本的编译器来讲，兼容性好;并不强制要求待测代码必须依赖C99标准，这一特性对许多嵌入式系统的开发很有用。

下载链接：[Downloads - cmockery - A lightweight library to simplify and generalize the process of writing unit tests for C applications.](https://code.google.com/p/cmockery/downloads/list)

## 5. Libev
libev 是一个开源的事件驱动库，基于epoll，kqueue等OS提供的基础设施。其以高效出名，它可以将IO事件，定时器，和信号统一起来，统一放在事件处理这一套框架下处理。基于Reactor模式，效率较高，并且代码精简（4.15版本8000多行），是学习事件驱动编程的很好的资源。

下载链接：http://software.schmorp.de/pkg/libev.html

## 6. Memcached
Memcached 是一个高性能的分布式内存对象缓存系统，用于动态Web应用以减轻数据库负载。它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提供动态数据库驱动网站的速度。Memcached 基于一个存储键/值对的 hashmap。Memcached-1.4.7的代码量还是可以接受的，只有10K行左右。

下载地址：[memcached - a distributed memory object caching system](http://memcached.org/)

## 7. Lua
Lua 很棒，Lua是巴西人发明的，这些都令我不爽，但是还不至于脸红，最多眼红。让我脸红的是Lua的源代码，百分之一百的ANSI C，一点都不掺杂。在任何支持ANSI C编译器的平台上都可以轻松编译通过。我试过，真是一点废话都没有。Lua的代码数量足够小，5.1.4仅仅1.5W行，去掉空白行和注释估计能到1W行。

下载地址：[The Programming Language Lua](http://www.lua.org/)

## 8. SQLite
SQLite 是一个开源的嵌入式关系数据库，实现自包容、零配置、支持事务的SQL数据库引擎。 其特点是高度便携、使用方便、结构紧凑、高效、可靠。足够小，大致3万行C代码，250K。

下载地址：[SQLite Home Page.](http://www.sqlite.org/index.html)

## 9 高性能键值对存储系统antirez/redis
下载地址：[antirez/redis·GitHub](https://github.com/antirez/redis)

## 10 Google的键/值对（Key/Value Pair）
嵌入式数据库:[google/leveldb · GitHub](https://github.com/google/leveldb)
