---
layout: post
title: "Docker 数据卷"
subtitle: "Docker Volume"
date: 2020-05-12 15:00:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Docker
---

# 1 数据卷

## 1.1 Docker 联合文件系统
`Docker镜像`是由多层`只读文件`叠加而成，当运行起一个容器的时候，Docker会在只读层上创建一个`读写层`。如果运行中的容器需要修改文件，那么并不会修改只读层的文件，只会把该文件复制到`读写层`然后进行修改，只读层的文件就被隐藏了。当删除了该容器之后，或者重启容器之后，之前对文件的更改会丢失，镜像的只读层以及容器运行时的“读写层”被称为`联合文件系统（Union File System）`。

为了实现容器与主机之间、容器与容器之间`共享文件`，容器中`数据的持久化`，将容器中的数据`备份`、`迁移`、`恢复`等，Docker加入了数据卷(volumes)机制。简单的讲，就是做了一个文件夹的实时共享，有点像局域网的文件共享。

## 1.2 数据卷的特点

1. 数据卷存在于宿主机的文件系统中，独立于容器，和容器的生命周期是分离的。
2. 数据卷可以是目录也可以是文件，容器可以利用数据卷与宿主机进行数据共享，实现了容器间的数据共享和交换。
3. 容器启动初始化时，如果容器使用的镜像包含了数据，这些数据会拷贝到数据卷中。
4. 容器对数据卷的修改是实时进行的。
5. 数据卷的变化不会影响镜像的更新。数据卷是独立于联合文件系统，镜像是基于联合文件系统。镜像与数据卷之间不会相互影响。

# 2 Docker挂载容器数据卷

[`查看更多`](https://docs.docker.com/storage/#choose-the-right-type-of-mount)

`bind mounts`、`Volumes`、和`tepfs mounts`三种方式，还有就是共享其他容器的数据卷，其中`tmpfs`是一种基于内存的临时文件系统。`tepfs mounts`数据不会存储在磁盘上，在次笔记中暂不做笔记。

## 2.1 bind mounts

![](img/docker-volume/bind-mounts.png)

使用bind mounts挂载数据卷时，宿主机上的文件或者目录将载入到容器中。文件或目录由其在主机上的绝对路径或相对路径引用。如果将数据卷绑定到容器上的非空目录中，则绑定装置会**隐藏**目录的现有内容。

bind mounts方式挂载数据卷有两种方式，利用docker run/create的参数为容器挂载数据卷。

### 2.1.1 -v --volume

```
-v HOST_DIR_OR_PATH:CONTAINER_DIR_OR_PATH:option
```

option 可选项如 ro，consistent，delegated，cached，z，和Z，可以参考文档。

### 2.1.2 --mount

其参数由多个键值对组成，以逗号分隔。

- `type`选项，其可以是`bind`，`volume`，或`tmpfs`。本主题讨论绑定装入，因此类型始终是`bind`。
- `source`选项。对于绑定装入，这是Docker守护程序主机上的文件或目录的路径。可以指定为`source`/`src`。
- 将`destination`文件或目录安装在容器中的路径作为其值。可以指定为`destination`，`dst`或`target`。
- `readonly`选项（如果存在）导致绑定装入以[只读](https://docs.docker.com/storage/bind-mounts/#use-a-read-only-bind-mount)方式[装入容器中](https://docs.docker.com/storage/bind-mounts/#use-a-read-only-bind-mount)。
- `bind-propagation`选项（如果存在）会更改 [绑定传播](https://docs.docker.com/storage/bind-mounts/#configure-bind-propagation)。可以是一个`rprivate`，`private`，`rshared`，`shared`，`rslave`，`slave`。
- [`consistency`](https://docs.docker.com/storage/bind-mounts/#configure-mount-consistency-for-macos)选项，如果存在，可以是一种`consistent`，`delegated`或`cached`。此设置仅适用于Docker for Mac，并在所有其他平台上被忽略。
- `--mount`标志不支持`z`或`Z`修改selinux标签的选项。

### 2.1.3 -v 与 --mount区别

使用`-v`绑定宿主机上不存在的文件或者目录时，会自动生成相应的文件或者目录，`--mount`则会抛出异常，所以用`--mount`指定文件和路径时需要提前创建以保证其存在。

## 2.2 volumes

![](img/docker-volume/bind-mounts.png)

Volumes 是保存 Docker 容器生成和使用数据的首选机制，利用 docker run/create 的参数为容器挂载数据卷。

### 2.2.1 -v --volume

```
-v volume_name:CONTAINER_DIR_OR_PATH:option
```

其中 `volume_name`是数据卷的名称，在宿主机上是唯一的，可以省略该字段，会自动创建。

### 2.2.2 --mount

其参数由多个键值对组成，以逗号分隔。

- `type`选项，其可以是[`bind`](https://docs.docker.com/storage/bind-mounts/)，`volume`，或 [`tmpfs`](https://docs.docker.com/storage/tmpfs/)。本主题讨论卷，因此类型始终是 `volume`。
- `source`选项。对于命名卷，这是卷的名称。对于匿名卷，省略此字段。可以指定为`source` /`src`。
- 将`destination`文件或目录安装在容器中的路径作为其值。可以指定为`destination`，`dst`/`target`。
- `readonly`选项（如果存在）导致绑定装入以[只读](https://docs.docker.com/storage/volumes/#use-a-read-only-volume)方式[装入容器中](https://docs.docker.com/storage/volumes/#use-a-read-only-volume)。
- `volume-opt`选项可以多次指定，它采用由选项名称及其值组成的键值对。

用`volumes`方式挂载的数据卷，实际上是创建了数据卷对象，可以用以下命令进行管理：

```
docker volume create     创建数据卷对象
docker volume inspect    查看数据卷的详细信息
docker volume ls         查看已创建的数据卷对象
docker volume prune      删除所有未被使用的数据卷对象
docker volume rm         删除一个或多个数据卷对象
```

## 2.3 容器 volume

使用`dockers run/create`的`--volumes-from`参数指定数据卷容器`docker run/create --volume-form CONTAINER`。

# 3. 注意

Docker 的数据卷更多会是使用 volumes 方式来进行使用，但值得注意的是：

- 如果挂载一个`空的数据卷`到容器中的一个`非空目录`中，那么这个目录下的文件会被`复制`到数据卷中。(我的测试：使用 -v 参数并没有这个效果，需要使--mount参数，如果不符请指正)
- 如果挂载一个`非空的数据卷`到容器中的`一个目录`中，那么容器中的目录中会`显示数据卷中的数据`。如果原来容器中目录`非空`，那么这些原始数据会被`隐藏掉`。

# 4 参考资料

- [Docker笔记之数据卷](https://www.jianshu.com/p/19f12c616d0c)
- [docker document](https://docs.docker.com/storage/#choose-the-right-type-of-mount)