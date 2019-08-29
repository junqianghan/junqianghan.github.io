---
layout: post
title: "Linux 用户管理"
subtitle: "linux user manage"
date: 2019-08-30 00:05:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Linux
---
# adduser/useradd
`adduser`是增加用户。

`adduser` 与 `useradd` 指令为同一指令（经由符号连结 symbolic link）。
使用权限：系统管理员。

**用法**

```shell
adduser [-c comment] [-d home_dir] [-e expire_date] [-f inactive_time]\ 
[-g initial_group] [-G group[,...]] [-m [-k skeleton_dir] | -M] \
[-p passwd] [-s shell] [-u uid [ -o]] [-n] [-r] loginid
```

**参数**

```shell
-c comment      新的注释（通常在/etc/passwd）
-d home_dir     home目录为 home_dir ，默认值：/home/user_name
-e expire_date  设定此帐号的使用期限（格式为 YYYY-MM-DD），预设值为永久有效
-s shell        shell
-g group        用户组
-G              指定多个用户组
```

# userdel
`userdel`可删除用户帐号与相关的文件。若不加参数，则仅删除用户帐号，而不删除相关文件。

**用法**
```shell
userdel [-r][用户帐号]
```
**参数**
```shell
- -r: 删除用户登入目录以及目录中所有文件。
```
# usermod

修改用户账号。

**用法**

```shell
usermod [-LU][-c <备注>][-d <登入目录>][-e <有效期限>][-f <缓冲天数>]\
[-g <群组>][-G <群组>][-l <帐号名称>][-s <shell>][-u <uid>][用户帐号]
```

```shell
* -c <备注>:       修改用户帐号的备注文字。
* -d <登入目录>:   修改用户登入时的目录。
* -e <有效期限>:   修改帐号的有效期限。
* -f <缓冲天数>:   修改在密码过期后多少天即关闭该帐号。
* -g <群组>:       修改用户所属的群组。
* -G <群组>:       修改用户所属的附加群组。
* -l <帐号名称>:   修改用户帐号名称。
* -L :             锁定用户密码，使密码无效。
* -s <shell>:      修改用户登入后所使用的shell。
* -u <uid>:        修改用户ID。
* -U :             解除密码锁定。
```

**参考资料**
- [Linux usermod命令](https://www.runoob.com/linux/linux-comm-usermod.html)


# 参考资料

- https://www.runoob.com/linux/linux-command-manual.html