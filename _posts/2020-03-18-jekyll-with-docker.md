---
layout: post
title: "Docker 容器搭建jekyll环境"
subtitle: "Jekyll with docker"
date: 2020-03-18 16:05:00
author: "Randle"
catalog: false
mathjax: false
comments: true
tags:
    - Jekyll
    - Docker
---

搭建 Jekyll 环境是个烦琐的事，直接利用 docker hub 上的 jekyll 镜像，通过 docker 容器的方式，搭建 jekyll 调试环境，是个很方便的方法。

```shell
docker run -d -it --name=blog-server -p 4000:4000 \
     -v ~/blog_dir:$image_blog_dir jekyll/jekyll bash
```

通过 volume 映射的方式，将宿主机上的博客目录映射到 docker 容器内，这里要注意的是，容器内需要修改此目录的属主为jekyll，可以进入容器修改，也可以通过`docker exec`的方式。

之后运行：

```shell
jekyll server --watch
```

这样宿主机上添加或者修改的内容，会直接应用到博客中，访问方式如下：

```
http://ADDRESS:4000
```

其中`ADDRESS`为 docker 容器所在的服务器地址，4000 端口也可以在启动 jekyll 的时候指定其他的，4000 是默认值 。
