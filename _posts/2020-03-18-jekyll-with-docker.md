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
docker run -d --name=blog-server -p 4000:4000 \
    -v $HOST_BLOG_DIR:/srv/jekyll jekyll/jekyll jekyll server --watch
```

因为 jekyll 镜像的工作目录是 `/srv/jekyll`，容器启动后，会自动修改此目录的权限，并执行传入的命令，所以，将博客目录映射到该目录下，并且启动 jekyll 服务即可。以上结论的依据来源于：

```shell
$ docker inspect blog-server
"Env": [
        "JEKYLL_DATA_DIR=/srv/jekyll",
]
...
"Path": "/usr/jekyll/bin/entrypoint",
"Args": [
         "jekyll",
         "server",
         "--watch"
]

$ docker exec blog-server cat /usr/jekyll/bin/entrypoint
#!/bin/bash
[ "$DEBUG" = "true" ] && set -x
set -e

# --
: ${JEKYLL_UID:=$(id -u jekyll)}
: ${JEKYLL_GID:=$(id -g jekyll)}

# --
export JEKYLL_UID
export JEKYLL_GID

# --
# Users can customize our UID's to fit their own so that
#   we don't have to chown constantly.  Well it's not like
#   we do so much of it (anymore) it's slow, but we do
#   change permissions which can result in some bad
#   behavior on OS X.
# --
if [ "$JEKYLL_UID" != "0" ] && [ "$JEKYLL_UID" != "$(id -u jekyll)" ]; then
  usermod  -u $JEKYLL_UID jekyll
  groupmod -g $JEKYLL_GID jekyll
  chown_args=""

  [ "$FULL_CHOWN" ] && chown_args="-R"
  for d in "$JEKYLL_DATA_DIR" "$JEKYLL_VAR_DIR"; do
    chown $chown_args jekyll:jekyll "$d"
  done
fi

# --
exec "$@"
```

上面几个参数表明了容器的启动方式，不详述。若想重启服务，重启容器即可，`docker restart`。

这样宿主机上添加或者修改的内容，会直接应用到博客中，访问方式如下：

```
http://ADDRESS:4000
```

其中`ADDRESS`为 docker 容器所在的服务器地址，4000 端口也可以在启动 jekyll 的时候指定其他的，4000 是默认值 。

```shell
jekyll serve --host 0.0.0.0 --port 4000 --wait
```

