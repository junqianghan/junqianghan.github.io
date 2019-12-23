---
layout:       post
title:        "Git 速查手册"
date:         2019-07-22 23:45:00
author:       "Randle"
catalog:      false
permalink: /:title.html
comments: true
tags:
    - Git
---




```shell
# 提交
git add file                # 工作区修改提交到暂存区
git add .                   # 所有修改过的文件提交暂存区
git rm file                 # 从版本库中删除文件
git rm file --cached        # 从版本库中删除文件，但不删除文件

git commit file
git commit .
git commit -a               # git add/rm 和 git commit 结合
git commit -am 'comments'   # 提交到版本库并添加描述
git commit --amend          # 生成一次新提交，与上一次提交并列
git commit --amend --author="userName <userEmail>"  # 修改上一次提交的作者信息
git commit **** --no-edit   # 避免弹出编辑窗

# 标签
git tag v1.0                                    # 打到最近一次 commit
git tag v1.0 commit_id                          # 打到commitid上
git tag -a $TAG_NAME -m '$DESC' $COMMIT_ID      # 添加描述
git tag                                         # 显示标签
git show $TAG_NAME                              # 查看 tag_name 信息
git tag -d v1.0                                 # 删除标签
git push origin v1.0                            # 推送标签到远端
git push origin --tags                          # 推送所有本地标签

# 版本回退
git reset       # 本地撤销，远程无效
git revert      # 撤销某次提交，可提交到远端
git reset --hard HEAD^      # 回到上一个版本
git reset --hard commit_id  # 库回退，清空暂存区，重置工作区
git reset --mixed commit_id # 库回退，清空暂存区，工作区不变
git reset --soft commit_id  # 库回退，暂存区不变，工作区不变

# 分支
git branch -d $BRANCH_NAME          # 删除本地分支
git branch -D $BRANCH_NAME          # 强制删除，未合并分支删除需强制
git branch -r -d $BRANCH_NAME       # 删除远端分支
git branch -f master HEAD~3         # master分支强行指定到HEAD~3
git checkout master~2 makefile      # 操作的是HEAD引用,从一个提交中检出文件
git checkout -- '*.c'               # 丢弃所有 .c 文件的工作区修改
git checkout .                      # 丢弃所有文件的工作区修改
git checkout tag_name               # 在当前分支上，取出tag_name 版本
git branch $BRANCH_NAME             # 新建分支
git checkout $BRANCH_NAME           # 切换分支
git checkout -b $BRANCH_NAME        # 新建并切换分支
git checkout -b $BRANCH_NAME $BRANCH    # 基于BRANCH新建分支并切换

git checkout $COMMIT_ID             # head切换到某次提交，不在任何分支，再次切换自动删除
git checkout $COMMIT_ID -b $BRANCH  # HEAD 切换到某个commit并新建分支

git reset file          # file 从暂存区恢复到工作区
git reset -- .          # 所有文件从暂存区恢复到工作区

# 远端
git push origin <source>:<destination>  # source 分支送到远端的 destination
git fetch origin <source>:<destination> # 远端source下载到本地的dest
git push origin :dest                   # 删除远端的dest分支
git fetch origin :dest                  # 本地创建新分支

git branch -u o/master foo              # 本地 foo 分支跟踪远端 master 分支
git branch --set-upstream-to=o/master foo   # 与上述写法相同，省略foo，当前分支跟踪
# 默认合并方式(fast-forward)
git merge --ff
# 保留源分支信息，创建merge commit
git merge --no-ff
# 额外的commit包含所有源分支内容
git merge --squash

git remote -v                       # 查看地址和名称
git remote show origin              # 查看远端状态
git remote add origin git@***       # 增加远端
git remote set-url origin git@***   # 修改远端地址
git remote rm origin                # 删除远端

# log
git log --graph --pretty=oneline --abbrev-commit    # 分支合并图
git reflog      # 查看历史命令，可实现回到将来分支

# stash
git stash           # 保存现场
git stash pop       # 恢复并删除最近一次 pop 的现场
git stash list      # 查看已经 stash 的列表
git stash apply stash@{0}   # 恢复 stash[0]
git stash drop stash@{0}    # 删除 stash{0}

# diff
git diff file                   # 工作区和暂存区差异
git diff
git diff <$id1>:<$id2>          # 两次提交之间的差异
git diff <branch1>:<branch2>    # 两个分支之间的差异
git diff --staged               # 暂存区和版本库差异
git diff --cached               # 暂存区和版本库差异
git diff stat                   # 仅仅比较统计信息

# patch
git diff > sync.patch           # 生成补丁，sync.patch 文件名
git apply sync.patch            # 打补丁
git apply --check sync.patch    # 测试补丁能够成功

# 配置
git config --list       # 本地配置信息
git config --global user.name 'robot'
git config --global user.email 'example@example.com'
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.lg 'log --graph --pretty=oneline --abbrev-commit'
```

## 参考资料
- [git 教程](https://www.yiibai.com/git)  
- [git 备忘](http://www.imooc.com/article/1111)
- [如何正确使用Git Flow](https://www.cnblogs.com/wish123/p/9785101.html)
- [git merge和git merge --no-ff的区别](https://www.jianshu.com/p/418323ed2b03)