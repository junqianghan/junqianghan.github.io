---
layout: post
title: "Tmux"
subtitle: "Linux tmux usage"
date: 2019-11-30 15:30:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Tmux
    - Linux
---
# 1 什么是 Tmux

当我们在`tmux`中工作的时候，即使关掉SecureCRT的连接窗口，再次连接，进入`tmux`的会话我们之前的工作仍然在继续。其实类似`tmux`的工具还有很多。例如gnu `screen`等。

tmux中有3种概念，会话，窗口(window)，窗格(pane)。会话有点像是tmux的服务，在后端运行，我们可以通过tmux命令创建这种服务，并且可以通过tmux命令查看，附加到后端运行的会话中。一个会话可以包含多个窗口，一个窗口可以被分割成多个窗格(pane)。

# 2 安装

```shell
sudo apt-get install tmux
```
# 3 会话

```shell
# 新建会话
tmux new -s [会话名]

# 退出会话
ctrl-b d
```

## 3.1 新建会话
```shell
tmux new -s [会话名]
```
## 3.2 退出会话
```shell
ctrl-b d
```
## 3.3 查看会话列表
```shell
tmux ls
```
如果是在某个会话环境中想查看会话列表，可以用以下指令来获得，然后用键盘选择就可进入
```shell
ctrl+b s
```
## 3.4 进入会话
```shell
tmux a -t [会话名]
```
## 3.5 销毁会话
```shell
tmux kill-session -t [会话名]
```
## 3.6 重命名会话
```shell
tmux rename -t [旧会话名] [新会话名]
```

# 4 窗口操作

一个tmux的会话中可以有多个窗口(`window`)，每个窗口又可以分割成多个`pane`(窗格)。我们工作的最小单位其实是窗格。默认情况下在一个`window`中，只有一个大窗格，占满整个窗口区域。我们在这个区域工作。

## 4.1 新建窗口

```shell
ctrl-b c
```
默认情况下创建出来的窗口由窗口序号+窗口名字组成，窗口名字可以由上面提到的方法修改，可以看到新创建的窗口后面有`*`号，表示是当前窗口。

## 4.2 切换窗口
在同一个会话的多个窗口之间可以通过如下快捷键进行切换：
```shell
ctrl+b p #(previous的首字母) 切换到上一个window。
ctrl+b n #(next的首字母) 切换到下一个window。
ctrl+b 0 #切换到0号window，依次类推，可换成任意窗口序号
ctrl+b w #(windows的首字母) 列出当前session所有window，通过上、下键切换窗口
ctrl+b l #(字母L的小写)相邻的window切换
```

## 4.3 关闭窗口

```shell
ctrl+b &
```

# 5 窗格

tmux的一个窗口可以被分成多个`pane`(窗格)，可以做出分屏的效果。

## 5.1 垂直分屏
```shell
ctrl+b %
```

## 5.2 水平分屏

```shell
ctrl+b “
```
## 5.3 切换窗格
```shell
ctrl+b o 依次切换当前窗口下的各个pane。
ctrl+b Up|Down|Left|Right 根据按箭方向选择切换到某个pane。
ctrl+b Space (空格键) 对当前窗口下的所有pane重新排列布局，每按一次，换一种样式。
ctrl+b z 最大化当前pane。再按一次后恢复。
```
## 5.4 关闭窗格
```shell
ctrl+b x # 关闭当前使用中的pane，操作之后会给出是否关闭的提示，按y确认即关闭。
或
ctrl+d
```

# 参考资料

- [Linux之Tmux使用教程](https://blog.csdn.net/zong596568821xp/article/details/83785387)
