---
layout:       post
title:        "ubuntu16.04安装jekyll"
subtitle:     "ubuntu install jekyll"
date:         2018-05-13 00:16:00
author:       "Randle"
catalog:      true
comments: true
tags:
    - Jekyll
    - Ubuntu
    - Linux
---

> 为了使得 github.io 上的博文可以在本地随时检验效果，在本机安装 jekyll 的指导教程。  
> 本次安装的 jekyll 为最新的3.3.1版本。  
> ubuntu 版本为 16.04

###  预备工作
因为 jekyll 需要很多软件的支持，所以准备工作要做足。

* Ruby (including development headers, v1.9.3 or above for Jekyll 2 and v2 or above for Jekyll 3)
* RubyGems
* Linux, Unix, or macOS
* NodeJS, or another JavaScript runtime (Jekyll 2 and earlier, for CoffeeScript support).
* Python 2.7 (for Jekyll 2 and earlier)
* GCC and Make (in case your system doesn’t have them installed, which you can check by running gcc -v and make -v in your system’s command line interface)


#### 安装gcc编译包

```shell
apt-get install build-essential
```

#### 安装ruby

因为 ruby 由于各种原因，原本完整的安装包被分割为多个小包，ruby-full 保证了全部特性安装。

```shell
apt-get install ruby-full
```

#### 安装RubyGems

```shell
apt install rubygems
which gem     //查看gem的安装位置，正常显示“/usr/bin/gem”
gem  update   --system     //升级rubygems到最新版本
```

#### 安装NodeJS

因为nodejs升级太快，造成版本分裂，采用nodesource安装脚本。注意：这里安装的6.x系列。   
  　　
```shell
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### 安装python2.7

```shell
apt-get install python
```

### 开始安装jekyll
预备软件安装好后，安装jekky只是一个命令。

```shell
gem install jekyll
jekyll --version           //查看jekyll的版本。
```

### 使用

在工程主目录下：

```shell
jekyll server --watch		# 启动服务
jekyll clean			# 删除中间文件
```
