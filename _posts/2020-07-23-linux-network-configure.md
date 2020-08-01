---
layout: post
title: "Linux 网络配置"
subtitle: "Linux Network Configuration"
7date: 2020-07-23 20:00:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Linux
    - Network
---

在我的印象中，Linux 的网络配置命令似乎很混乱，查看主机的 ip 地址，有时候用 `ifconfig` 有时用 `ip a`。同样配置网卡的 ip 地址，启动网卡，`ifconfig` 和 `ip` 好像也都能做到。配置路由，arp，mac 地址，各个场景都有不同的命令可以实现，这些命令的对应关系是什么呢？当我看到下面这个图的时候，豁然开朗。

![](/img/20200723-linux-network-configuration/net-tools_iproute2.jpg)

net-tools 起源于 BSD，自 2001 年起，Linux 社区已经对其停止维护，而 iproute2 旨在取代 net-tools，并提供了一些新功能。一些 Linux 发行版已经停止支持 net-tools，只支持 iproute2。

net-tools 通过 procfs(/proc) 和 ioctl 系统调用去访问和改变内核网络配置，而 iproute2 则通过 netlink 套接字接口与内核通讯。

net-tools 中工具的名字比较杂乱，而 iproute2 则相对整齐和直观，基本是 ip 命令加后面的子命令。 虽然取代意图很明显，但是这么多年过去了，net-tool 依然还在被广泛使用。


# 1 net-tools 基本命令

如前所述，net-tools 命令规律性不强，这里列举几个常用的用法，后面慢慢补充。

- ifconfig
- route
- arp
- netstat

## 1.1 ifconfig

使用 `ifconfig` 命令配置并查看网络接口情况。

配置 eth0 的 IP，同时激活设备:

```shell
ifconfig eth0 192.168.4.1 netmask 255.255.255.0 up
```
配置 eth0 别名设备 eth0:1 的 IP，并添加路由

```shell
ifconfig eth0:1 192.168.4.2
route add –host 192.168.4.2 dev eth0:1
```
激活（禁用）设备

```shell
ifconfig eth0:1 up(down)
```
查看所有（指定）网络接口配置

```shell
ifconfig (eth0)
```

## 1.2 route

`route` 命令用来配置路由表。

添加到主机路由

```shell
route add –host 192.168.4.2 dev eth0:1
route add –host 192.168.4.1 gw 192.168.4.250
```

添加到网络的路由

```shell
route add –net IP netmask MASK eth0
route add –net IP netmask MASK gw IP
route add –net IP/24 eth1
```

添加默认网关

```shell
route add default gw IP
```
删除路由

```shell
route del –host 192.168.4.1 dev eth0:1
```
查看路由信息

```shell
route 或 route -n (-n 表示不解析名字,列出速度会比route 快)
```

## 1.3 arp

查看 ARP 缓存

```shell
arp
```

添加

```shell
arp –s IP MAC
```

删除

```shell
arp –d IP
```

## 1.4 netstat

`netstat` 命令用于显示与 IP、TCP、UDP 和 ICMP 协议相关的统计数据，一般用于检验本机各端口的网络连接情况。`netstat` 是在内核中访问网络及相关信息的程序，它能提供 TCP 连接，TCP 和 UDP 监听，进程内存管理的相关报告。

查看所有 tcp 连接状态，同时显示 pid 和进程名。
```
netstat -plant
-p, --programs             display PID/Program name for sockets
-l, --listening            display listening server sockets
-a, --all, --listening     display all sockets (default: connected)
-n, --numeric              don't resolve names
-i, --interfaces           display interface table
-r, --route                display routing table
<Socket>={-t|--tcp} {-u|--udp} {-S|--sctp} {-w|--raw} 
			{-x|--unix} --ax25 --ipx --netrom
```

> [Linux netstat命令详解](https://www.cnblogs.com/ftl1012/p/netstat.html)

常用选项：

```
# 显示网卡列表
netstat -i

# 显示路由信息
netstat -r
```


# 2 iproute2 基本命令

iproute2 的命令相对整齐和直观，基本是 ip 命令加后面的子命令。

## 2.1  ip

ip命令的用法如下：

```shell
ip [OPTIONS] OBJECT [COMMAND [ARGUMENTS]]
```
这里的 OBJECT 和 COMMAND，有全称，也有简称。例如，网上搜用 ip 命令配置 ip 地址，可能 `ip addr` 和 `ip address` 都有，看起来是两个命令，其实 `addr` 只是 `address`的简称。

`man ip` 可以得到详细参数解释：

```
$man ip
OBJECT := { link | address | addrlabel | route | rule | neigh | ntable | tunnel | tuntap | maddress |
               mroute | mrule | monitor | xfrm | netns | l2tp | tcp_metrics }

OPTIONS := { -V[ersion] | -h[uman-readable] | -s[tatistics] | -r[esolve] | -f[amily] { inet | inet6 | ipx |
               dnet | link } | -o[neline] | -n[etns] name | -a[ll] | -c[olor] }

```

下面介绍一些 OBJECT 的用法，随时补充。

- link
- addr
- route
- neigh
- maddr
- netns

### 2.1.1 link

| command | abbreviation         |
| ------- | -------------------- |
| show    | sh、list、lst、ls、l |
| add     |                      |
| delete  |                      |
| set     |                      |


#### show

ip link show -- 显示设备属性。`-s`选项出现两次或者更多次，ip 会输出更为详细的错误信息统计。

- 不指定设备：显示所有设备。
- 指定设备：显示该设备信息。

**示例**:

```
# ip -s -s link ls eth0

eth0: mtu 1500 qdisc cbq qlen 100
link/ether 00:a0:cc:66:18:78 brd ff:ff:ff:ff:ff:ff
RX: bytes packets errors dropped overrun mcast
2449949362 2786187 0 0 0 0
RX errors: length crc fifo missed
0 0 0 0 0
TX: bytes packets errors dropped carrier collsns
178558497 1783946 332 0 332 35172
TX errors: aborted fifo window heartbeat
0 0 0 332
```

这个命令等价于 `ifconfig eth0`

#### set

ip link set -- 改变设备的属性。

**示例1**：up/down 起动／关闭设备。

```shell
ip link set dev eth0 up
```

这个等于传统的 `ifconfig eth0 up(down)`

**示例2**：改变设备传输队列的长度。

参数:`txqueuelen NUMBER` 或者 `txqlen NUMBER`

```shell
ip link set dev eth0 txqueuelen 100
```

**示例3**：改变网络设备 `MTU` (最大传输单元)的值。

```shell
ip link set dev eth0 mtu 1500
```

**示例4**： 修改网络设备的`MAC`地址。

参数: address LLADDRESS

```shell
ip link set dev eth0 address 00:01:4f:00:15:f1
```

### 2.1.2 addr

| command | abbreviation         |
| ------- | -------------------- |
| show    | sh、list、lst、ls、l |
| add     | a                    |
| delete  | del、d               |
| flush   | f                    |


#### show

ip address show -- 显示协议地址. 缩写：show、list、lst、sh、ls、l

```shell
ip addr ls eth0
```
#### add

`ip address add` -- 添加一个新的协议地址. 缩写：add、a

```
ip addr add 10.1.1.230/24 dev eth0
```

> [ip addr 操作ip时需要注意](https://blog.csdn.net/u012599988/article/details/82683440)

**示例1**：为每个地址设置一个字符串作为标签。为了和 Linux-2.0 的网络别名兼容，这个字符串必须以设备名开头，接着一个冒号。

```shell
ip addr add local 192.168.4.1/28 brd + label eth0:1 dev eth0
```
**示例2**: 在以太网接口`eth0`上增加一个地址`192.168.20.0`，掩码长度为24位(255.255.255.0)，标准广播地址，标签为`eth0:Alias`：

```shell
ip addr add 192.168.4.2/24 brd + dev eth1 label eth1:1
```
这个命令等于传统的: `ifconfig eth1:1 192.168.4.2`

#### delete

`ip address delete` -- 删除一个协议地址. 缩写：delete、del、d

```shell
ip addr del 10.1.1.230/24 dev eth0
ip addr del 192.168.4.1/24 brd + dev eth0 label eth0:Alias1
```


#### flush

`ip address flush` -- 清除协议地址. 缩写：flush、f

**示例1** : 删除属于私网`10.0.0.0/8`的所有地址：

```shell
ip -s -s a f to 10/8
```

**示例2** : 取消所有以太网卡的IP地址

```shell
ip -4 addr flush eth0
```

### 2.1.3 route

| command | abbreviation    | meaning      |
| ------- | --------------- | ------------ |
| route   | r、ro           | 路由配置     |
| add     | a               | 添加新路由   |
| delete  | del、d          | 删除路由     |
| change  | chg             | 修改路由     |
| show    | list、sh、ls、l | 列出路由     |
| replace | repl            | 替换已有路由 |
| flush   | f               | 擦除路由表   |
| get     | g               | 获得单个路由 |



从 Linux-2.2 开始，内核把路由归纳到许多路由表中，这些表都进行了编号，编号数字的范围是 1 到 255。另外，为了方便，还可以在 `/etc/iproute2/rt_tables` 中为路由表命名。默认情况下，所有的路由都会被插入到表 `main` (编号254)中。在进行路由查询时，内核只使用路由表 `main`。

#### add

设置到网络10.0.0/24的路由经过网关193.233.7.65

```
# ip route add 10.0.0/24 via 193.233.7.65
```

#### change

修改到网络10.0.0/24的直接路由，使其经过设备dummy

```
# ip route chg 10.0.0/24 dev dummy
```


#### replace

实现数据包级负载平衡,允许把数据包随机从多个路由发出。weight 可以设置权重.

```
# ip route replace default equalize nexthop via 211.139.218.145 dev eth0 weight 1 nexthop via 211.139.218.145 dev eth1 weight 1
```

#### delete

删除上一节命令加入的多路径路由

```
# ip route del default scope global nexthop dev ppp0 nexthop dev ppp1
```

#### show
列出默认路由表的内容

```
# ip route ls
```
这个命令等于传统的: `route`

列出路由表TABLEID里面的路由。缺省设置是table main。TABLEID或者是一个真正的路由表ID或者是`/etc/iproute2/rt_tables`文件定义的字符串，或者是以下的特殊值：

- all -- 列出所有表的路由；
- cache -- 列出路由缓存的内容。

```
ip ro ls 193.233.7.82 tab cache
```

列出某个路由表的内容
```
# ip route ls table fddi153
```

#### flush

清除所有ipv4路由cache

```
# ip route flush cache
```
IPv4 routing cache is flushed.


删除路由表main中的所有网关路由（示例：在路由监控程序挂掉之后）：

```
# ip -4 ro flush scope global type unicast
```

清除所有被克隆出来的IPv6路由：

```
# ip -6 -s -s ro flush cache
```

在gated程序挂掉之后，清除所有的BGP路由：

```
# ip -s ro f proto gated/bgp
```

#### get

使用这个命令可以获得到达目的地址的一个路由以及它的确切内容。

`ip route get`命令和`ip route show`命令执行的操作是不同的。`ip route show`命令只是显示现有的路由，而`ip route get`命令在必要时会派生出新的路由。

搜索到 193.233.7.82 的路由

```
# ip route get 193.233.7.82
193.233.7.82 dev eth0 src 193.233.7.65 realms inr.ac cache mtu 1500 rtt 300
```

搜索目的地址是 193.233.7.82，来自 193.233.7.82，从 eth0 设备到达的路由（这条命令会产生一条非常有意思的路由，这是一条到 193.233.7.82 的回环路由）

```
# ip r g 193.233.7.82 from 193.233.7.82 iif eth0
　　193.233.7.82 from 193.233.7.82 dev eth0 src 193.233.7.65 realms inr.ac/inr.ac cache mtu 1500 rtt 300 iif eth0
```

#### 示例

**示例3**: 实现链路负载平衡.加入缺省多路径路由，让 ppp0 和 ppp1 分担负载(注意：scope值并非必需，它只不过是告诉内核，这个路由要经过网关而不是直连的。实际上，如果你知道远程端点的地址，使用via参数来设置就更好了)。

```
# ip route add default scope global nexthop dev ppp0 nexthop dev ppp1
# ip route replace default scope global nexthop dev ppp0 nexthop dev ppp1
```

**示例4**: 设置NAT路由。在转发来自192.203.80.144的数据包之前，先进行网络地址转换，把这个地址转换为193.233.7.83

```
# ip route add nat 192.203.80.142 via 193.233.7.83
```

**示例7**: 计算使用 gated/bgp 协议的路由个数

```
# ip route ls proto gated/bgp |wc
　　1413 9891 79010
```

**示例8**: 计算路由缓存里面的条数，由于被缓存路由的属性可能大于一行，以此需要使用 `-o` 选项

```
# ip -o route ls cloned |wc
　　159 2543 18707
```


### 2.1.4 neigh

| command   | abbreviation    | Meaning       |
| --------- | --------------- | ------------- |
| neighbour | neighbor、neigh | arp表管理命令 |
| add       | a               | 添加          |
| change    | chg             | 修改          |
| replace   | repl            | 替换          |
| delete    | del             | 删除          |
| show      | lish、sh、ls    | 显示网络邻居  |
| flush     | f               | 清除邻接条目  |

`ip neighbour` -- neighbour/arp 表管理命令。

#### add

在设备`eth0`上，为地址`10.0.0.3`添加一个permanent ARP条目：

```
# ip neigh add 10.0.0.3 lladdr 0:0:0:0:0:1 dev eth0 nud perm
```

#### change

把状态改为 reachable

```
# ip neigh chg 10.0.0.3 dev eth0 nud reachable
```

#### delete

删除设备 eth0 上的一个 ARP 条目 10.0.0.3

```
# ip neigh del 10.0.0.3 dev eth0
```

#### show

显示网络邻居的信息.

```
# ip -s n ls 193.233.7.254
193.233.7.254. dev eth0 lladdr 00:00:0c:76:3f:85 ref 5 used 12/13/20 nud reachable
```

#### flush

清除邻接条目. (-s 可以显示详细信息)

```
# ip -s -s n f 193.233.7.254
```



### 2.1.5 netns

`ip netns` 命令用来管理 network namespace。它可以创建命名的 network namespace，然后通过名字来引用 network namespace，所以使用起来很方便。

```
ip netns list
ip netns add Name
ip netns set Name NETNSID
ip netns delete Name
ip netns idenfity PID
ip netns exec Name cmd
```
### 2.1.6 maddr

| command  | abbreviation    | Meaning      |
| -------- | --------------- | ------------ |
| maddress | maddr           | 多播地址管理 |
| show     | list、sh、ls、l | 列出多播地址 |
| add      | a               | 加入多播地址 |
| delete   | del、d          | 删除多播地址 |

#### show

`ip maddress show` -- 列出多播地址

```
# ip maddr ls dummy
```

查看 

```
# ip -O maddr ls dummy
2: dummy
link 33:33:00:00:00:01 users 2 static
link 01:00:5e:00:00:01
```

使用`add/delete`这两个命令，我们可以添加／删除在网络接口上监听的链路层多播地址。这个命令只能管理链路层地址。

#### add

增加

```
# ip maddr add 33:33:00:00:00:01 dev dummy
```
#### delete

删除

```
# ip maddr del 33:33:00:00:00:01 dev dummy
```

### 2.1.7 ip rule

ip rule -- 路由策略数据库管理命令.

命令 : add、delete、show(或者list)

>注意：策略路由(policy routing)不等于路由策略(rouing policy)。

在某些情况下，我们不只是需要通过数据包的目的地址决定路由，可能还需要通过其他一些域：源地址、IP协议、传输层端口甚至数据包的负载。这就叫做：策略路由(policy routing)。

- ip rule add -- 插入新的规则
- ip rule delete -- 删除规则
- ip rule show -- 列出路由规则

缩写：

- add、a
- delete、del、d
- show、list、sh、ls、l

示例1: 通过路由表inr.ruhep路由来自源地址为192.203.80/24的数据包

```
ip ru add from 192.203.80/24 table inr.ruhep prio 220
```

示例2:把源地址为193.233.7.83的数据报的源地址转换为192.203.80.144，并通过表1进行路由

```
ip ru add from 193.233.7.83 nat 192.203.80.144 table 1 prio 320
```

示例3:删除无用的缺省规则

```
ip ru del prio 32767
```

示例4: 

```
# ip ru ls
0: from all lookup local
32762: from 192.168.4.89 lookup fddi153
32764: from 192.168.4.88 lookup fddi153
32766: from all lookup main
32767: from all lookup 253
```



### 2.1.8 ip mroute

| command | abbreviation    | Meaning              |
| ------- | --------------- | -------------------- |
| mroute  |                 | 多播路由缓存管理     |
| show    | list、sh、ls、l | 列出多播路由缓存条目 |

`ip mroute show` -- 列出多播路由缓存条目


示例1:查看 
```
# ip mroute ls
(193.232.127.6, 224.0.1.39) Iif: unresolved
(193.232.244.34, 224.0.1.40) Iif: unresolved
(193.233.7.65, 224.66.66.66) Iif: eth0 Oifs: pimreg
```
示例2:查看 
```
# ip -s mr ls 224.66/16
(193.233.7.65, 224.66.66.66) Iif: eth0 Oifs: pimreg
9383 packets, 300256 bytes
```

### 2.1.9 ip tunnel

| command | abbreviation | Meaning        |
| ------- | ------------ | -------------- |
| tunnel  | tunl         | 通道配置       |
| add     | a            | 添加新的通道   |
| change  | chg          | 修改现有的通道 |
| delete  | del、d       | 删除一个通道   |

#### add

建立一个点对点通道，最大TTL是32
```
# ip tunnel add Cisco mode sit remote 192.31.7.104 local 192.203.80.1 ttl 32
```
#### show

`ip tunnel show` -- 列出现有的通道

```
# ip -s tunl ls Cisco
```

### 2.1.10 ip monitor和rtmon

ip monitor 和 rtmon -- 状态监视

ip 命令可以用于连续地监视设备、地址和路由的状态。这个命令选项的格式有点不同，命令选项的名字叫做 monitor，接着是操作对象：
```
ip monitor [ file FILE ] [ all | OBJECT-LIST ]
```
示例1:
```
# rtmon file /var/log/rtmon.log
```
示例2: 
```
# ip monitor file /var/log/rtmon.log r
```


## 2.2 ss

ss 是 Socket Statistics 的缩写。顾名思义，ss 命令可以用来获取 socket 统计信息，可以显示和 netstat 类似的内容。ss 的优势在于它能够显示更多更详细的有关 TCP 和连接状态的信息，而且比 netstat 更快速更高效。

当服务器的 socket 连接数量变得非常大时，无论是使用 netstat 命令还是直接 cat /proc/net/tcp，执行速度都会很慢。

ss 快的秘诀在于，它利用到了 TCP 协议栈中 tcp_diag。tcp_diag 是一个用于分析统计的模块，可以获得 Linux 内核中第一手的信息，这就确保了 ss 的快捷高效。

> [Linux ss 命令详解](https://www.cnblogs.com/ftl1012/p/ss.html)

```
Usage: ss [ OPTIONS ]
       ss [ OPTIONS ] [ FILTER ]
   -h, --help           this message
   -V, --version        output version information
   -n, --numeric        don't resolve service names
   -r, --resolve        resolve host names
   -a, --all            display all sockets
   -l, --listening      display listening socket
   -o, --options        show timer information
   -e, --extended       show detailed socket information
   -m, --memory         show socket memory usage
   -p, --processes      show process using socket
   -i, --info           show internal TCP information
   -s, --summary        show socket usage summary
 
   -4, --ipv4           display only IP version 4 sockets
   -6, --ipv6           display only IP version 6 sockets
   -0, --packet display PACKET sockets
   -t, --tcp            display only TCP sockets
   -u, --udp            display only UDP sockets
   -d, --dccp           display only DCCP sockets
   -w, --raw            display only RAW sockets
   -x, --unix           display only Unix domain sockets
   -f, --family=FAMILY display sockets of type FAMILY
 
   -A, --query=QUERY, --socket=QUERY
       QUERY := {all|inet|tcp|udp|raw|unix|packet|netlink}[,QUERY]
 
   -D, --diag=FILE      Dump raw information about TCP sockets to FILE
   -F, --filter=FILE   read filter information from FILE
       FILTER := [ state TCP-STATE ] [ EXPRESSION ]
```

**常用命令**

```
-t：tcp
-a: all
-l: listening      【ss -l列出所有打开的网络连接端口】
-s: summary        【显示 Sockets 摘要】
-p: progress
-n: numeric        【不解析服务名称】
-r: resolve        【解析服务名称】
-m: memory         【显示内存情况】
```

查看进程使用的 socket

```
ss -pl
```

# 参考资料
- [linux 路由表设置 之 route 指令详解](https://blog.csdn.net/vevenlcf/article/details/48026965)
- [ubuntu16.04网卡信息配置](https://www.cnblogs.com/wucaiyun1/p/11115182.html)
- [linux命令总结之ip命令](https://www.cnblogs.com/ginvip/p/6367803.html)
