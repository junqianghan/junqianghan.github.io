---
layout: post
title: "Linux 路由"
subtitle: "Linux route"
7date: 2020-07-15 16:00:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Linux
    - Route
    - Network
---

使用下面的 `route` 命令可以查看 Linux 内核路由表。

```shell
$ route
Kernel IP routing table
Destination   Gateway  Genmask         Flags Metric Ref    Use Iface
default       bogon    0.0.0.0         UG    600    0        0 wlp3s0
link-local    *        255.255.0.0     U     1000   0        0 wlp3s0
192.168.1.0   *        255.255.255.0   U     600    0        0 wlp3s0
```
`route` 命令的输出项说明:

| 输出项      | 说明                                                       |
| ----------- | ---------------------------------------------------------- |
| Destination | 目标网段或者主机                                           |
| Gateway     | 网关地址，”*” 表示目标是本主机所属的网络，不需要路由       |
| Genmask     | 网络掩码                                                   |
| Flags       | 标记。一些可能的标记如下：                                 |
|             | U — 路由是活动的                                           |
|             | H — 目标是一个主机                                         |
|             | G — 路由指向网关                                           |
|             | R — 恢复动态路由产生的表项                                 |
|             | D — 由路由的后台程序动态地安装                             |
|             | M — 由路由的后台程序修改                                   |
|             | ! — 拒绝路由                                               |
| Metric      | 路由距离，到达指定网络所需的中转数（linux 内核中没有使用） |
| Ref         | 路由项引用次数（linux 内核中没有使用）                     |
| Use         | 此路由项被路由软件查找的次数                               |
| Iface       | 该路由表项对应的输出接口                                   |


# 1 路由类型

## 1.1 主机路由

主机路由是路由选择表中指向单个`IP`地址或主机名的路由记录。主机路由的`Flags`字段为`H`。例如，在下面的示例中，本地主机通过`IP`地址`192.168.1.1`的路由器到达`IP`地址为`10.0.0.10`的主机。

```
Destination Gateway    Genmask Flags     Metric    Ref    Use    Iface
----------- -------    ------- -----     ------    ---    ---    -----
10.0.0.10  192.168.1.1 255.255.255.255   UH       0    0      0    eth0
```

## 1.2 网络路由

网络路由是代表主机可以到达的网络。网络路由的`Flags`字段为`N`。例如，在下面的示例中，本地主机将发送到网络`192.19.12`的数据包转发到`IP`地址为`192.168.1.1`的路由器。

```
Destination  Gateway     Genmask Flags  Metric  Ref   Use   Iface
-----------  -------     -----   -----  -----   ---   ---   -----
192.19.12   192.168.1.1  255.255.255.0    UN     0     0    0   eth0
```

## 1.3 默认路由

当主机不能在路由表中查找到目标主机的`IP`地址或网络路由时，数据包就被发送到默认路由（默认网关）上。默认路由的`Flags`字段为`G`。例如，在下面的示例中，默认路由是`IP`地址为`192.168.1.1`的路由器。

```
Destination Gateway     Genmask  Flags  Metric  Ref   Use   Iface
---------   -------     -------  -----  ------  ---   ---   -----
default    192.168.1.1  0.0.0.0   UG      0      0     0    eth0
```

# 2 配置静态路由

Linux 系统的`route`命令用于显示和操作IP路由表（show / manipulate the IP routing table）。要实现两个不同的子网之间的通信，需要一台连接两个网络的路由器，或者同时位于两个网络的网关来实现。在 Linux 系统中，设置路由通常是为了解决以下问题：该 Linux 系统在一个局域网中，局域网中有一个网关，能够让机器访问Internet，那么就需要将这台机器的IP地址设置为 Linux 机器的默认路由。要注意的是，直接在命令行下执行`route`命令来添加路由，不会永久保存，当网卡重启或者机器重启之后，该路由就失效了；可以在`/etc/rc.local`中添加`route`命令来保证该路由设置永久有效。

## 2.1 route 命令

Route命令是用于操作基于内核ip路由表，它的主要作用是创建一个静态路由让指定一个主机或者一个网络通过一个网络接口，如`eth0`。当使用 `add` 或者 `del` 参数时，路由表被修改，如果没有参数，则显示路由表当前的内容。

命令格式是：

```shell
route [-f] [-p] [add|del] [-net|-host] target [netmask Nm] [gw Gw] [[dev] If]
route [-f] [-p] [Command [Destination] [mask Netmask] [Gateway] [metric Metric]] [if Interface]] 
```

其中：

- -f : 清除所有网关入口的路由表。 

- -p : 与 add 命令一起使用时使路由具有永久性。
- -n : 不解析名字

- add : 添加一条路由规则
- del : 删除一条路由规则
- -net : 目的地址是一个网络
- -host : 目的地址是一个主机
- target : 目的网络或主机
- netmask : 目的地址的网络掩码
- gw : 路由数据包通过的网关
- dev : 为路由指定的网络接口

## 2.2 route 命令使用举例

添加到主机的路由

```shell
route add -host 192.168.1.2 dev eth0 
#添加到10.20.30.148的网关
route add -host 10.20.30.148 gw 10.20.30.40     
```

添加到网络的路由

```shell
#添加10.20.30.40的网络
route add -net 10.20.30.40 netmask 255.255.255.248 eth0
#添加10.20.30.48的网络
route add -net 10.20.30.48 netmask 255.255.255.248 gw 10.20.30.41 
route add -net 192.168.1.0/24 eth1
```

添加默认路由

```shell
route add default gw 192.168.1.1
```

删除路由

```shell
route del -host 192.168.1.2 dev eth0:0
route del -host 10.20.30.148 gw 10.20.30.40
route del -net 10.20.30.40 netmask 255.255.255.248 eth0
route del -net 10.20.30.48 netmask 255.255.255.248 gw 10.20.30.41
route del -net 192.168.1.0/24 eth1
route del default gw 192.168.1.1
```

屏蔽一条路由

```shell
[root]# route add -net 224.0.0.0 netmask 240.0.0.0 reject
[root]# route
Kernel IP routing table
Destination   Gateway         Genmask       Flags Metric Ref  Use Iface
10.0.0.0      192.168.120.1   255.0.0.0     UG    0      0      0 eth0
224.0.0.0     -               240.0.0.0     !     0      -      0 -
224.0.0.0     *               240.0.0.0     U     0      0      0 eth0
default       192.168.120.240 0.0.0.0       UG    0      0      0 eth0
```

## 2.3 设置永久路由

在`/etc/rc.local`里添加

```shell
route add -net 192.168.3.0/24 dev eth0
route add -net 192.168.2.0/24 gw 192.168.3.254
```

在`/etc/sysconfig/network`里添加到末尾

```
GATEWAY=gw-ip
#或者
GATEWAY=gw-dev
```

在`/etc/sysconfig/static-router`中配置

```shell
any net x.x.x.x/24 gw y.y.y.y
```

# 3 配置包转发

在 `CentOS` 中默认的内核配置已经包含了路由功能，但默认并没有在系统启动时启用此功能。开启 `Linux` 的路由功能可以通过调整内核的网络参数来实现。要配置和调整内核参数可以使用 `sysctl` 命令。例如：要开启 `Linux` 内核的数据包转发功能可以使用如下的命令。

```shell
sysctl -w net.ipv4.ip_forward=1
```

这样设置之后，当前系统就能实现包转发，但下次启动计算机时将失效。为了使在下次启动计算机时仍然有效，需要将下面的行写入配置文件`/etc/sysctl.conf`。

```shell
$ vi /etc/sysctl.conf
net.ipv4.ip_forward = 1
```

用户还可以使用如下的命令查看当前系统是否支持包转发。

```shell
sysctl net.ipv4.ip_forward
```

# 参考资料
- [linux 路由表设置 之 route 指令详解](https://blog.csdn.net/vevenlcf/article/details/48026965)
- [ubuntu16.04网卡信息配置](https://www.cnblogs.com/wucaiyun1/p/11115182.html)
