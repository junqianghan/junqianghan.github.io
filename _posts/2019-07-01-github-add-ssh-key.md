---
layout:       post
title:        "Github 添加 ssh 公钥"
subtitle: "Github add ssh key"
date:         2019-07-01 20:23:00
author:       "Randle"
catalog:      true
comments: true
tags:
    - Github
    - SSH-Key
---

`Github`上配置个人电脑公钥是个常规操作，今天配置的时候出了一些问题，记录在此。

# 本机生成公钥操作

```shell
ssh-keygen -t rsa -C "mail_user_name@mail_server.com"
```
后面出现的提示，可以默认回车，在 ~/.ssh/目录下，出现下面的文件：

```shell
id_rsa			#私钥
id_rsa.pub		#公钥
```
到这里，公钥和私钥就创建完成了，下一步将公钥放到`Github`上面。

# Github 添加公钥

1. 登陆`Github`账号；
2. 复制前面生成的`id_rsa.pub` 的内容到` Github/Setting/SSH and GPG keys` 中，在`SSH`下面创建新的条目；

至此，添加完成。

# 私钥权限问题

按照上面的两步配置之后遇到了一个问题，shell 返回如下：
```shell
Warning: Permanently added 'github.com,13.229.188.59' (RSA) to the list of known
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0670 for '~/.ssh/id_rsa' are too open.
It is recommended that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "~/.ssh/id_rsa": bad permissions
Permission denied (publickey).
fatal: Could not read from remote repository.
```
这个错误表达的是，`.ssh`目录下的私钥的权限，可以被本机的其他用户访问，所以在SSH鉴权的时候被忽略了，无法与远端的公钥配对。

解决办法就是，去掉 `id_rsa` 私钥文件其他用户的访问权限；

```shell
chmod 600 ~/.ssh/id_rsa
```

# 验证

通过下面的方法可以验证公钥配置成功：

```shell
ssh -T git@github.com 
```

返回下面的结果时候，验证成功：

```shell
Hi $USER_NAME$! You've successfully authenticated, but GitHub does not provide shell access.
```

其中的 `USER_NAME` 是 `Github` 用户名。