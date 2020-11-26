---
layout: post
title: "MySQL 速查手册"
subtitle: "mysql handbook"
7date: 2020-11-26 11:00:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - MySQL
    - Database
---



## 数据库使用

```mysql
#登录
mysql -u ben -p -h myserver -P 999

#显示数据库列表
show databases;

#选择数据库
use $DB_NAME

#显示表
show tables;

#显示表列，以下写法相同
show columns from $table_name
describe $table_name
desc $table_name

#SHOW
#显示广泛的服务器状态信息
show status 
show create database $database_name
show create table $table_name
#显示授予用户（所有用户或特定用户）的安全权限
show grants
#显示服务器错误或警告信息
show errors
show warnings
```

## 检索数据

检索不同的列：

```mysql
#单列
select c1 from $table_name;

#多列
select c1,c2 from $table_name;

#所有列
select * from $table_name;

#不同行
select DISTINCT c1 from $table_name;

#完全限定表明
select $table_name.c1 from $db_name.table_name;
```

限制结果

```mysql
#前5行
select c1 from $table_name limit 5;

#从行5开始的5行
select c1 from $table_name limit 5,5;
```

## 排序

```mysql
#单列排序
select c1 from $table_name order by c1;

#多列排序
select c1,c2,c3 from $table_name order by c1,c2;

#排序方向，默认升序（ASC），可指定降序（DESC)
select c1 from $table order by c1 DESC,c2;
```

## 过滤

### where

```mysql
select c1 from $table where c1='';
```

where 字句操作符：

| 操作符  | 说明               |
| ------- | ------------------ |
| =       | 等于               |
| <>      | 不等于             |
| !=      | 不等于             |
| <       | 小于               |
| <=      | 小于等于           |
| >       | 大于               |
| >=      | 大于等于           |
| BETWEEN | 在指定的两个值之间 |

between使用：

```mysql
select c1 from $table where c1 BETWEEN 1 AND 2;
```

### 空值检查

```mysql
select c1 from $table where c1 IS NULL;
```

### 组合where字句

```mysql
#and
select c1 from $table where c1 =1 and c2=2;

#or
select c1 from $table where c1 =1 or c2=2;

#IN
select c1 from $table where c1 in (1,2);

#NOT
select c1 from $table where c1 NOT IN (1,2);

#LIKE 通配符
#%通配符
select c1 from $table where c1 LIKE '%a%';

#_下划线通配符
select c1 from $table where c1 LIKE '_kile';
```

在搜索串中，%表示任何字符出现任何次数。_下划线通配符匹配单个字符。

### 正则表达式





## 计算字段



## 数据处理函数



## 汇总数据



## 分组数据



## 子查询



## 联结表



## 组合查询



## 全文本搜索



## 插入数据



## 更新删除



## 创建操纵表



