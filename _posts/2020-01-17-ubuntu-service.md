---
layout: post
title: "Ubuntu Service"
subtitle: "ubuntu service control"
date: 2020-01-17 15:00:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - service
    - ubuntu
---

本文介绍`/etc/init.d`下服务的查询和控制。`init.d`文件夹内的可执行文件，都是一种服务，建立到`/etc/rc{RUNLEVEL}.d/`的软连接，即可实现开机自启动。

以下命令详见:
```
man service(8)
man update-rc.d(8)
```
很详细。

# Service 控制
查看所有服务状态：

```
service --status-all
```

给服务传递参数：
```
service SCRIPT COMMAND [OPTIONS]
```
这里的`COMMAND`和`OPTIONS`作为参数传递给`SCRIPT`，常见的`COMMAND`有：

- start
- stop
- restart

这里的`COMMAND`对应的执行逻辑，是由`service`自身决定的，`service`可以按照捕获参数的方式，捕获到这个`COMMAND`，决定执行逻辑。

# Service 配置

可以通过建立软连接的方式配置一个服务自启动，删除软连接取消自启动。也可以通过`update-rc.d`实现服务配置。

下面的`SERVICE_NAME`，指的是`/etc/init.d/SERVICE_NAME`对应的可执行文件。要配置一个自启动服务，首先要在`/etc/init.d`中有可执行入口。

**自启动**

```
update-rc.d SERVICE_NAME defaults
```

**取消自启动**

标记服务不再自启动，并不删除软连接。
```
update-rc.d SERVICE_NAME disable
```

**恢复自启动**

```
update-rc.d SERVICE_NAME disable
```
`disable`的逆操作。

**移除服务**
```
update-rc.d SERVICE_NAME remove
```
移除所有`/etc/rc{RUNLEVEL}.d/`目录中对应的软连接，此时，`/etc/init.d`中对应的脚本应该已删除，否则`update-rc.d`会放弃此次操作，`remove`操作一般用在软件包删除的时候，清理所有的脚本和连接。

# 参考资料
- [20200117-01-Linux-查看所有服务状态](https://www.cnblogs.com/allen2333/p/8904223.html)
- [20200117-02-Ubuntu Service系统服务说明与使用方法](http://www.mikewootc.com/wiki/linux/usage/ubuntu_service_usage.html)