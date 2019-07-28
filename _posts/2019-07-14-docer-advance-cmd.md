---
layout:       post
title:        "Docker 进阶命令"
subtitle: "docker advanced cmd"
date:         2019-07-14 23:58:00
author:       "Randle"
catalog:      true
comments: true
tags:
    - Docker
---

docker 客户端非常简单 ,可以直接输入 docker 命令来查看到 Docker 客户端的所有命令选项。

```shell
randle@H:~# docker
```

可以通过命令 docker command --help 更深入的了解指定的 Docker 命令使用方法。

例如我们要查看 docker stats 指令的具体使用方法：

```shell
randle@H:~# docker stats --help
```
# 命名

--name

# 端口

```shell
randle@H:~# docker run -d -P training/webapp python app.py
```
参数含义：
* -d:让容器在后台运行。
* -P:将容器内部使用的网络端口映射到我们使用的主机上。

可以使用 docker port 命令查看容器的端口映射情况：

- docker port CONTAINER_ID;
- docker port CONTAINER_NAME;

两种方式效果相同.

设定容器端口和宿主机的端口映射：
* -p: 指定端口映射，格式为：主机(宿主)端口:容器端口

# 卷映射

```shell
docker run -v HOST_DIR:DOCKER_DIR
```

* -v
* --volume

效果相同。

# 连接

```shell
docker run --link DOCKER_NAME:ALIAS_NAME
```
其中，
- DOCKER_NAME:被连接的容器名。
- ALIAS_NAME:新建的容器内被连接容器的别名。


# 容器内进程

可以使用 docker top 来查看容器内部运行的进程:
```shell
randle@H:~$ docker top wizardly_chandrasekhar
UID     PID         PPID          ...       TIME                CMD
root    23245       23228         ...       00:00:00            python app.py
```

# 底层信息

使用 docker inspect 来查看 Docker 的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

```shell
randle@H:~$ docker inspect wizardly_chandrasekhar
[
    {
        "Id": "bf08b7f2cd897b5964943134aa6d373e355c286db9b9885b1f60b6e8f82b2b85",
        "Created": "2018-09-17T01:41:26.174228707Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 23245,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2018-09-17T01:41:26.494185806Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
......
```

# docker cp/exec

```shell
docker cp   #用于容器与主机之间的数据拷贝
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
docker cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH

docker exec [options] container command [arg...]
docker exec -it -w /root $CONTAINER pwd
docker exec -it $CONTAINER bash
docker exec -u root -it $CONTAINER bash         # 以root用户执行bash
```


# 更多命令

[Docker 命令大全](https://www.runoob.com/docker/docker-command-manual.html)
