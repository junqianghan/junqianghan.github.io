---
layout: post
title: "CAP 理论"
subtitle: "CAP Theory"
date: 2020-07-23 00:00:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - CAP
---

# 什么是CAP理论

CAP即：

- Consistency（一致性）
- Availability（可用性）
- Partition tolerance（分区容忍性）

这三个性质对应了分布式系统的三个指标：
而CAP理论说的就是：一个分布式系统，不可能同时做到这三点。如下图：

![](/img/20200723-CAP-theory/CAP-theory.jpg)

接下来将详细介绍C A P 三个指标的含义，以及三者如何权衡。

# CAP的含义

借用一下维基百科[CAP理论](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/CAP_theorem)一文中关于C、A、P三者的定义。

> *Consistency* : Every read receives the most recent write or an error  
> *Availability* : Every request receives a (non-error) response – without the guarantee that it contains the most recent write  
> *Partition tolerance* : The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes

翻译一下就是：
①**一致性：**对于客户端的每次读操作，要么读到的是最新的数据，要么读取失败。换句话说，一致性是站在分布式系统的角度，对访问本系统的客户端的一种承诺：要么我给您返回一个错误，要么我给你返回绝对一致的最新数据，不难看出，其强调的是数据正确。

②**可用性：**任何客户端的请求都能得到响应数据，不会出现响应错误。换句话说，可用性是站在分布式系统的角度，对访问本系统的客户的另一种承诺：我一定会给您返回数据，不会给你返回错误，但不保证数据最新，强调的是不出错。

③**分区容忍性：**由于分布式系统通过网络进行通信，网络是不可靠的。当任意数量的消息丢失或延迟到达时，系统仍会继续提供服务，不会挂掉。换句话说，分区容忍性是站在分布式系统的角度，对访问本系统的客户端的再一种承诺：我会一直运行，不管我的内部出现何种数据同步问题，强调的是不挂掉。



# 权衡 C、A

之前提到，CAP理论说一个分布式系统不可能同时满足C、A、P这三个特性。那么我们就来分析C、A、P的权衡吧。

> **note：**其实这里有个关于CAP理论理解的误区。不要以为在所有时候都只能选择两个特性。在不存在网络失败的情况下（分布式系统正常运行时），C和A能够同时保证。只有当网络发生分区或失败时，才会在C和A之间做出选择。

对于一个分布式系统而言，P是前提，必须保证，因为只要有网络交互就一定会有延迟和数据丢失，这种状况我们必须接受，必须保证系统不能挂掉。所以只剩下C、A可以选择。要么保证数据一致性（保证数据绝对正确），要么保证可用性（保证系统不出错）。

当选择了C（一致性）时，如果由于网络分区而无法保证特定信息是最新的，则系统将返回错误或超时。

当选择了A（可用性）时，系统将始终处理客户端的查询并尝试返回最新的可用的信息版本，即使由于网络分区而无法保证其是最新的。

# C、A、P三者之间的冲突

本部分主要参考[分布式CAP定理，为什么不能同时满足三个特性？](https://link.zhihu.com/?target=https%3A//blog.csdn.net/yeyazhishang/article/details/80758354)

假设有两台服务器，一台放着应用A和数据库V，一台放着应用B和数据库V，他们之间的网络可以互通，也就相当于分布式系统的两个部分。

在满足一致性的时候，两台服务器(假设为N1,N2)的数据是一样的，DB0=DB0。在满足可用性的时候，用户不管是请求N1或者N2，都会得到立即响应。在满足分区容错性的情况下，N1和N2有任何一方宕机，或者网络不通的时候，都不会影响N1和N2彼此之间的正常运作。

![](/img/20200723-CAP-theory/cap-conflict-1.jpg)
![](/img/20200723-CAP-theory/cap-conflict-2.png)


图1中，用户通过N1中的A应用请求数据更新到服务器DB0，这时N1中的服务器DB0变为DB1，通过分布式系统的数据同步更新操作，N2服务器中的数据库V0也更新为了DB1（图2），这时，用户通过B向数据库发起请求得到的数据就是即时更新后的数据DB1。

上面是正常运作的情况，但分布式系统中，最大的问题就是网络，现在假设一种极端情况，N1和N2之间的网络断开了，但我们仍要支持这种网络异常，也就是满足分区容错性，那么这样能不能同时满足一致性和可用性呢？

![](/img/20200723-CAP-theory/cap-conflict-3.png)

假设N1和N2之间通信的时候网络突然出现故障，有用户向N1发送数据更新请求，那N1中的数据DB0将被更新为DB1，由于网络是断开的，N2中的数据库仍旧是DB0；

如果这个时候，有用户向N2发送数据读取请求，由于数据还没有进行同步，应用程序没办法立即给用户返回最新的数据DB1，怎么办呢？有二种选择，第一，牺牲数据一致性，响应旧的数据DB0给用户；第二，牺牲可用性，阻塞等待，直到网络连接恢复，数据更新操作完成之后，再给用户响应最新的数据DB1。

> 参考资料：
> [CAP 定理的含义](https://link.zhihu.com/?target=http%3A//www.ruanyifeng.com/blog/2018/07/cap.html)
