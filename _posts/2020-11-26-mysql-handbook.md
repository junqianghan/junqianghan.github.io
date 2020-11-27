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

关键词：`REGEXP`

```mysql
#基本字符匹配
select c from $table where c1 regexp '1000' order by c1;
```

MySql中的正则表达式，默认不区分大小写，如果要区分的话，可以加`BINARY`参数。

```mysql
select prod_name from table where prod_name regexp binary 'JetPack .000';
```

OR 匹配。

```mysql
where prod_name regexp '1000|2000';
```

[]，几个字符之一。

```mysql
where prod_name regexp '[123] ton';
```

字符集和否定

```mysql
#匹配非这些字符
[^123]
```

字符集合

```mysql
[123456]
[1-6]
[a-z]
```

特殊字符，需要转义。

`.`表示匹配任何单个字符，`\\.`表示匹配单个字符`.`。

| 特殊字符 | 说明                     |
| -------- | ------------------------ |
| `.`      | 任何单个字符             |
| `[]`     | 匹配字符集中的任意字符   |
| `[^]`    | 匹配非字符集中的任意字符 |
| `|`      | 或                       |

空白元字符：

| 元字符 | 说明     |
| ------ | -------- |
| `\\f`  | 换页     |
| `\\n`  | 换行     |
| `\\r`  | 回车     |
| `\\t`  | 制表     |
| `\\v`  | 纵向制表 |

为了匹配反斜杠`\`本身，也需要两个反斜杠，就变成三个反斜杠`\\\`。

> 多数正则表达式实现使用单个反斜杠转义特殊字符，以便能使用这些字符本身，但MySQL要求两个反斜杠（MySQL子机解释一个，正则表达式库解释一个）。

字符类

| 类           | 说明                                              |
| ------------ | ------------------------------------------------- |
| `[:alnum:]`  | 任意字母和数字（同[a-zA-Z0-9]）                   |
| `[:alpha:]`  | 任意字母（同[a-zA-Z]）                            |
| `[:blank:]`  | 空格和制表（`\\t`）                               |
| `[:cncrl:]`  | ASCII控制字符，（ASCII 0到31和127）               |
| `[:digit:]`  | 任意数字（同[0-9]）                               |
| `[:print:]`  | 任意可打印字符                                    |
| `[:graph:]`  | 与[:print:]相同，但不包括空格                     |
| `[:lower:]`  | 任意小写字母（[a-z]）                             |
| `[:upper:]`  | 任意大写字母([A-Z])                               |
| `[:punct:]`  | 既不在[:alnum:]又不在[:cncrl:]中的任意字符        |
| `[:space:]`  | 包括空格在内的任意空白字符（[`\\f\\n\\r\\t\\v`]） |
| `[:xdigit:]` | 任意十六进制数字（[a-fA-F0-9]）                   |

匹配多个实例：

| 元字符  | 说明                         |
| ------- | ---------------------------- |
| `*`     | 0个或多个                    |
| `+`     | 1个或多个（等于{1,})         |
| `?`     | 0个或1个（等于{0,1}）        |
| `{n}`   | 指定数目的匹配               |
| `{n,}`  | 不少于指定数目的匹配         |
| `{n,m}` | 匹配数目的范围（m不超过255） |

定位符：

| 元字符    | 说明       |
| --------- | ---------- |
| `^`       | 文本的开始 |
| `$`       | 文本的结尾 |
| `[[:<:]]` | 词的开始   |
| `[[:>:]]` | 词的结尾   |



## 计算字段



## 数据处理函数



## 汇总数据



## 分组数据



## 子查询



## 联结表



## 组合查询



## 全文本搜索



## 插入数据

插入完整行

```mysql
insert into $table values(c1_value,c2_value,c3_value,c4_value...)；

#更安全的方法
insert into $table(c1,c2,c3) values(c1_value,c2_value,c3_value);

#插入多行
insert into $table(c1,c2,c3) values(c1_value,c2_value,c3_value),(c1_value2,c2_value2,c3_value2);
```

插入检索出的数据

```mysql
insert into $table(c1,c2) select b1,b2 from $table2;
```

## 更新删除

更新表项

```mysql
update $table set c1='' where c2=2;
update $table set c1='1',c2='2' where c3='3';
```

删除

```mysql
delete from $table where id=1;
```

delete 不需要列名或通配符。delete删除整行而不是删除列。为了删除指定的列，请使用update。delete 删除表的内容，但是不删除表本身。

从表中删除所有行，有一个更快的替代命令

```mysql
truncate table $table
```

TRUNCATE TABLE 在功能上与不带 WHERE 子句的 DELETE 语句相同：二者均删除表中的全部行。但 TRUNCATE TABLE 比 DELETE 速度快，且使用的系统和事务日志资源少。


DELETE 语句每次删除一行，并在事务日志中为所删除的每行记录一项。TRUNCATE TABLE 通过释放存储表数据所用的数据页来删除数据，并且只在事务日志中记录页的释放。


TRUNCATE TABLE 删除表中的所有行，但表结构及其列、约束、索引等保持不变。新行标识所用的计数值重置为该列的种子。如果想保留标识计数值，请改用 DELETE。如果要**删除表定义及其数据**，请使用 **DROP TABLE** 语句。

对于由 FOREIGN KEY 约束引用的表，不能使用 TRUNCATE TABLE，而应使用不带 WHERE 子句的 DELETE 语句。由于 TRUNCATE TABLE 不记录在日志中，所以它不能激活触发器。

TRUNCATE TABLE 不能用于参与了索引视图的表。

对用TRUNCATE TABLE删除数据的表上增加数据时，要使用UPDATE STATISTICS来维护索引信息。




## 创建操纵表



