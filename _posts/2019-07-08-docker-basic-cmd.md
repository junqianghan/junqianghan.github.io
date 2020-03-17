---
layout:       post
title:        "Docker 基本命令"
subtitle: "docker basic cmd"
date:         2019-07-08 23:15:00
author:       "Randle"
catalog:      true
comments: true
tags:
    - Docker
---


# 运行

```shell
randle@H:~$ docker run ubuntu:15.10 /bin/echo "Hello world"
Hello world
```

- docker: Docker 的二进制执行文件。
- run:与前面的 docker 组合来运行一个容器。
- ubuntu:15.10指定要运行的镜像，Docker首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
- /bin/echo "Hello world": 在启动的容器里执行的命令

以上命令完整的意思可以解释为：Docker 以 ubuntu15.10 镜像创建一个新容器，然后在容器里执行 bin/echo "Hello world"，然后输出结果。

# 交互

```shell
randle@H:~$ docker run -i -t ubuntu:15.10 /bin/bash
root@dc0050c79503:/#
```
* -t:在新容器内指定一个伪终端或终端。
* -i:允许你对容器内的标准输入 (STDIN) 进行交互。

我们可以通过运行exit命令或者使用CTRL+D来退出容器。

# 后台模式

```shell
randle@H:~$ docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
2b1b7a428627c51ab8810d541d759f072b4fc75487eed05812646b8534a2fe63
```

在输出中，我们没有看到期望的"hello world"，而是一串长字符

2b1b7a428627c51ab8810d541d759f072b4fc75487eed05812646b8534a2fe63

这个长字符串叫做容器ID，对每个容器来说都是唯一的，我们可以通过容器ID来查看对应的容器发生了什么。

首先，我们需要确认容器有在运行，可以通过 docker ps 来查看:

# 运行状态

```shell
randle@H:~$ docker ps
```

返回结果中：
- CONTAINER ID:容器ID
- NAMES:自动分配的容器名称

# 日志

在容器内使用docker logs命令，查看容器内的标准输出：
```shell
randle@H:~$ docker logs 2b1b7a428627
```

- docker logs CONTAINER_ID;
- docker logs CONTAINER_NAME;

这两种方式效果相同。

```shell
randle@H:~$ docker logs -f bf08b7f2cd89
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
192.168.239.1 - - [09/May/2016 16:30:37] "GET / HTTP/1.1" 200 -
192.168.239.1 - - [09/May/2016 16:30:37] "GET /favicon.ico HTTP/1.1" 404 -
```
* -f: 让 docker logs 像使用 tail -f 一样来输出容器内部的标准输出。

# 停止

- docker stop CONTAINER_ID;
- docker stop CONTAINER_NAME;

与前面日志类似，这两条命令，作用相同。

# 重启

已经停止的容器，可以使用命令 docker start 来启动。

docker ps -l 查询最后一次创建的容器：

```shell
#  docker ps -l 
CONTAINER ID        IMAGE                             PORTS                     NAMES
bf08b7f2cd89        training/webapp     ...        0.0.0.0:5000->5000/tcp    wizardly_chandrasekhar
```

正在运行的容器，可以使用 docker restart 命令来重启.

# 移除

使用 docker rm 命令来删除不需要的容器。

删除容器时，容器必须是停止状态，否则会报如下错误：

```shell
randle@H:~$ docker rm wizardly_chandrasekhar
Error response from daemon: You cannot remove a running container bf08b7f2cd897b5964943134aa6d373e355c286db9b9885b1f60b6e8f82b2b85. Stop the container before attempting removal or force remove
```

# 退出

通过 bash 进入一个容器后，调试之后，让容器继续运行，可以使用 Ctrl+P+Q。注意 P 和 Q 需要大写。
