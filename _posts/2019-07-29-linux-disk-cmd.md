---
layout:       post
title:        "Linux 磁盘相关命令"
subtitle: "Linux disk commands"
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

```
# lsblk -f
NAME   FSTYPE LABEL    UUID	MOUNTPOINT
sda                                                         
├─sda1 ntfs            6E221EC8221E9565                     
├─sda2 ntfs            AC0AAC410AAC0B02                     
├─sda3                                                      
├─sda5 ext4            79ab7eb1-3620-4417-9016-591cc075ff55 /
└─sda6 swap            58f62d90-bb43-48bd-a227-0dfd6d9c89f8 [SWAP]
sdb                                                         
├─sdb1                                                      
├─sdb5 ntfs   Software 000CA322000F0B89                     
└─sdb6 ntfs   Document 0003BBC8000F1539
```
`lsblk -f`操作可以列出系统内所有设备并且显示其`UUID`和`LABEL`信息。


# blkid

查看块设备的文件系统类型、LABEL、UUID等信息。

```
# blkid -t LABEL="config-2" -odevice
```
上述命令可以查看，label为config-2的设备，其设备名，挂载操作的时候使用。

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

# fatab

`/etc/fstab`是用来存放文件系统的静态信息的文件，   当系统启动的时候，系统会自动地从这个文件读取信息，并且会自动将此文件中指定的文件系统挂载到指定的目录。

## 文档示例
/etc/fstab
```
# <file system>        <dir>         <type>    <options>             <dump> <pass>
tmpfs                  /tmp          tmpfs     nodev,nosuid          0      0
/dev/sda1              /             ext4      defaults,noatime      0      1
/dev/sda2              none          swap      defaults              0      0
/dev/sda3              /home         ext4      defaults,noatime      0      2
```
## 字段定义

`/etc/fstab` 文件包含了如下字段，通过空格或 Tab 分隔。

```
<file system>	<dir>	<type>	<options>	<dump>	<pass>
```

- <file systems> - 要挂载的分区或存储设备.
- <dir> - <file systems>的挂载位置。
- <type> - 要挂载设备或是分区的文件系统类型，支持许多种不同的文件系统：ext2, ext3, ext4, reiserfs, xfs, jfs, smbfs, iso9660, vfat, ntfs, swap 及 auto。 设置成auto类型，mount 命令会猜测使用的文件系统类型，对 CDROM 和 DVD 等移动设备是非常有用的。
- <options> - 挂载时使用的参数，注意有些mount 参数是特定文件系统才有的。一些比较常用的参数有：
	- auto - 在启动时或键入了 mount -a 命令时自动挂载。
	- noauto - 只在你的命令下被挂载。
	- exec - 允许执行此分区的二进制文件。
	- noexec - 不允许执行此文件系统上的二进制文件。
	- ro - 以只读模式挂载文件系统。
	- rw - 以读写模式挂载文件系统。
	- user - 允许任意用户挂载此文件系统，若无显示定义，隐含启用 noexec, nosuid, nodev 参数。
	- users - 允许所有 users 组中的用户挂载文件系统.
	- nouser - 只能被 root 挂载。
	- owner - 允许设备所有者挂载.
	- sync - I/O 同步进行。
	- async - I/O 异步进行。
	- dev - 解析文件系统上的块特殊设备。
	- nodev - 不解析文件系统上的块特殊设备。
	- suid - 允许 suid 操作和设定 sgid 位。这一参数通常用于一些特殊任务，使一般用户运行程序时临时提升权限。
	- nosuid - 禁止 suid 操作和设定 sgid 位。
	- noatime - 不更新文件系统上 inode 访问记录，可以提升性能(参见 atime 参数)。
	- nodiratime - 不更新文件系统上的目录 inode 访问记录，可以提升性能(参见 atime 参数)。
	- relatime - 实时更新 inode access 记录。只有在记录中的访问时间早于当前访问才会被更新。（与 noatime 相似，但不会打断如 mutt 或其它程序探测文件在上次访问后是否被修改的进程。），可以提升性能(参见 atime 参数)。
	- flush - vfat 的选项，更频繁的刷新数据，复制对话框或进度条在全部数据都写入后才消失。
	- defaults - 使用文件系统的默认挂载参数，例如 ext4 的默认参数为:rw, suid, dev, exec, auto, nouser, async.
- <dump> dump 工具通过它决定何时作备份. dump 会检查其内容，并用数字来决定是否对这个文件系统进行备份。 允许的数字是 0 和 1 。0 表示忽略， 1 则进行备份。大部分的用户是没有安装 dump 的 ，对他们而言 <dump> 应设为 0。
- <pass> fsck 读取 <pass> 的数值来决定需要检查的文件系统的检查顺序。允许的数字是0, 1, 和2。 根目录应当获得最高的优先权 1, 其它所有需要被检查的设备设置为 2. 0 表示设备不会被 fsck 所检查。


## 文件系统标示

在` /etc/fstab`配置文件中你可以以三种不同的方法表示文件系统：内核名称、`UUID` 或者 `LABEL`。使用 `UUID` 或是 `LABEL` 的好处在于它们与磁盘顺序无关。如果你在 `BIOS` 中改变了你的存储设备顺序，或是重新拔插了存储设备，或是因为一些 `BIOS` 可能会随机地改变存储设备的顺序，那么用 `UUID` 或是 `LABEL` 来表示将更有效。参见 持久化块设备名称 。

要显示分区的基本信息请运行`lablk -f`。

### 内核名称

你可以使用 `fdisk -l` 来获得内核名称，前缀是 `dev`。

### UUID
所有分区和设备都有唯一的`UUID`。它们由文件系统生成工具 (mkfs.*) 在创建文件系统时生成。

`lsblk -f` 命令将显示所有设备的 `UUID` 值。`/etc/fstab` 中使用 `UUID=` 前缀:

`/etc/fstab`
```
# <file system>                           <dir>         <type>    <options>             <dump> <pass>
tmpfs                                     /tmp          tmpfs     nodev,nosuid          0      0
UUID=24f28fc6-717e-4bcd-a5f7-32b959024e26 /     ext4              defaults,noatime      0      1
UUID=03ec5dd3-45c0-4f95-a363-61ff321a09ff /home ext4              defaults,noatime      0      2
UUID=4209c845-f495-4c43-8a03-5363dd433153 none  swap              defaults              0      0
```

### LABEL

注意: 使用这一方法，每一个标签必须是唯一的.
要显示所有设备的标签，可以使用` lsblk -f` 命令。在 `/etc/fstab` 中使用 `LABEL=` 作为设备名的开头 :

`/etc/fstab`

```
# <file system>        <dir>         <type>    <options>             <dump> <pass>
tmpfs                  /tmp          tmpfs     nodev,nosuid   0      0
LABEL=Arch_Linux       /             ext4      defaults,noatime      0      1
LABEL=Arch_Swap        none          swap      defaults              0      0
```




# 参考资料

- [Linux fdisk命令](https://www.runoob.com/linux/linux-comm-fdisk.html)
- [openstack-creating-and-attaching-a-volume-into-an-instance](https://www.darwinbiler.com/openstack-creating-and-attaching-a-volume-into-an-instance/)
- [blkid](https://ipcmen.com/blkid)
- [centos Linux 查看硬盘常用命令](https://www.cnblogs.com/acck/p/9540693.html)
- [Linux df命令](https://www.runoob.com/linux/linux-comm-df.html)
- [Linux du命令](https://www.runoob.com/linux/linux-comm-du.html)
- [linux之fstab文件详解](https://blog.csdn.net/richerg85/article/details/17917129)