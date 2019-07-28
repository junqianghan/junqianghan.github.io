---
layout:       post
title:        "ubuntu 安装 typora"
subtitle: "ubuntu install typora"
date:         2019-07-23 16:54:00
author:       "Randle"
catalog:	true
mathjax:	false
comments:	true
tags:
    - Software
---

ubuntu 环境中, typora 软件安装步骤.

```shell
# optional, but recommende# optional, but recommended
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update

# install typora
sudo apt-get install typora
```

---

[Ubuntu16.04安装Typora](https://blog.csdn.net/libing403/article/details/82055422)