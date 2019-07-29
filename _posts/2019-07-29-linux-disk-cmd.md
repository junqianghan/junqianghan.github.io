---
layout:       post
title:        "linux 磁盘相关命令"
subtitle: "linux disk commands"
date:         2019-07-29 17:33:00
author:       "Randle"
catalog:	true
mathjax:	false
comments:	true
tags:
    - Linux
---

# fdisk

`Linux fdisk`是一个创建和维护分区表的程序，它兼容`DOS`类型的分区表、`BSD`或者`SUN`类型的磁盘列表。

```shell
fdisk -l  #列出所有分区表
```

# lsblk

`lsblk`命令可以列出所有可用块设备的信息，比如我们说的逻辑磁盘，而`df -h`查看的是文件系统级别的信息。`lsblk`命令包含在`util-linux`包中，`yum`安装`util-linux`包即可，`util-linux`包含多个命令工具。

# blkid

查看块设备的文件系统类型、LABEL、UUID等信息。

# df

显示已挂载的文件系统，磁盘使用状况。常用命令：

```shell
df -h 		#显示存储空间大小
df -ah 		#人性化显示各存储空间大小
df -aT 		#显示所有存储系统空间使用情况,同时显示存储系统的文件系统类型
df -ahlT 	#查看本地文件，不显示网络磁盘
```

# du

`Linux du`命令用于显示目录或文件的大小。`du`会显示指定的目录或文件所占用的磁盘空间。常用命令：

```shell
du -sh				#显示当前文件夹的空间使用情况	
du -h --max-depth=1 /home	#查看home文件夹的空间使用情况
du -ch				#看当前文件及文件中包含的子文件夹大小
du -h test1.txt			#查看某个文件容量大小
du -h test1.txt test2.txt	#查看多个文件容量大小
```

# 参考资料

- [Linux fdisk命令](https://www.runoob.com/linux/linux-comm-fdisk.html)
- [openstack-creating-and-attaching-a-volume-into-an-instance](https://www.darwinbiler.com/openstack-creating-and-attaching-a-volume-into-an-instance/)
- [blkid](https://ipcmen.com/blkid)
- [centos Linux 查看硬盘常用命令](https://www.cnblogs.com/acck/p/9540693.html)
- [Linux df命令](https://www.runoob.com/linux/linux-comm-df.html)
- [Linux du命令](https://www.runoob.com/linux/linux-comm-du.html)