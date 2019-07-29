---
layout:       post
title:        "Linux 查看 IP 地址"
subtitle: "linux check ip address"
date:         2019-07-02 21:02:00
author:       "Randle"
comments: true
tags:
    - Linux
---
Linux 中查看本机 ip 地址有两种方式：

```shell
1. ifconfig
2. ip addr
```

其中 ifconfig 在 net-tools 软件包中，ip 命令在 iproute2 软件包中。

net-tools 起源于 BSD，自 2001 年起，Linux社区已经对其停止维护，而iproute2旨在取代net-tools，并提供了一些新功能。一些Linux发行版已经停止支持net-tools，只支持iproute2。

net-tools通过procfs(/proc)和ioctl系统调用去访问和改变内核网络配置，而iproute2则通过netlink套接字接口与内核通讯。

net-tools中工具的名字比较杂乱，而iproute2则相对整齐和直观，基本是ip命令加后面的子命令。
虽然取代意图很明显，但是这么多年过去了，net-tool依然还在被广泛使用。