---
layout: post
title: "Linux 日志级别"
subtitle: "linux log level"
7date: 2021-03-18 14:00:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Linux
---

Linux 系统 syslog 日志为 8 个等级，从 0 到 7；系统日志保存在在 `/var/log/` 下面，修改日志级别方法如下：

syslog 的日志等级有 8 个，默认是 info，这时候用 syslog 为 debug(最低日志级别) 来写日志，syslog 服务是不会写如日志的。

比如：
```sh
[root@umail180 etc]# cat /etc/syslog.conf
*.info;mail.none;authpriv.none;cron.none

/var/log/messages
```
这时候用 - p 选项来修改日志级别的优先级

```sh
[root@umail180 etc]# logger -p debug "hello this is a test"

#-p选项来指定优先级，logger的默认优先为是info，指定info或更高的优先级都可以被syslog所接收。
```

优先级（priority），优先级越低情况越严重：  

```
emerg      0     系统不可用
alert      1     必须马上采取行动的事件
crit       2     关键的事件
err        3     错误事件
warning    4     警告事件
notice     5     普通但重要的事件
info       6     有用的信息
debug      7     调试信息
```