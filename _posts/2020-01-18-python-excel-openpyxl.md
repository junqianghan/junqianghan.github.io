---
layout: post
title: "Python 读写 Excel 表格"
subtitle: "openpyxl"
date: 2020-01-18 18:05:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Python
    - Excel
    - Openpyxl
---

> [openpyxl-doc](https://openpyxl.readthedocs.io/en/stable/index.html)

`openpyxl`是`python` 中用来读写 `excel` 的包，操作的是新版 `excel` 文件，即后缀名为 `xlsx`的文件。

每个`excel`文件抽象为一个`Workbook`,每个工作表抽象为一个`sheet`对象，每个单元格抽象为一个`cell`对象，

安装：

```
pip install openpyxl
```

# Workbook

加载Workbook：
```python
>>> from openpyxl import load_workbook
>>> wb2 = load_workbook('test.xlsx')
>>> print wb2.sheetnames
['Sheet2', 'New Title', 'Sheet1']
```

新建Workbook：
```python
>>> from openpyxl import Workbook
>>> wb = Workbook()
```

保存Workbook:
```python
wb = Workbook()
wb.save('balances.xlsx')
```

关闭文件引用:
```python
wb = Workbook()
wb.close()
```

# Sheet

获得活动sheet：
```python
>>> ws = wb.active
```

创建sheet:
```python
# insert at the end (default)
>>> ws1 = wb.create_sheet("Mysheet") 

# insert at first position
>>> ws2 = wb.create_sheet("Mysheet", 0) 

# insert at the penultimate position
>>> ws3 = wb.create_sheet("Mysheet", -1) 
```

表单名:
```python
ws.title = "New Title"
```

访问sheet:
```python
>>> ws3 = wb["New Title"]

>>> print(wb.sheetnames)
['Sheet2', 'New Title', 'Sheet1']

>>> for sheet in wb:
...     print(sheet.title)
```

复制sheet:
```python
source = wb.active
target = wb.copy_worksheet(source)
```

# Cell

## 访问单个单元格

```python
c = ws['A4']
ws['A4'] = 4
d = ws.cell(row=4, column=2, value=10)
```
`cell(row,colum)`访问行和列的方式，行和列从`1`开始。
 
```python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.cell(row, column, value)
```
可以按照这种方式为单元格赋值。  



## 访问范围内单元格

```python
cell_range = ws['A1':'C2']
colC = ws['C']
col_range = ws['C:D']
row10 = ws[10]
row_range = ws[5:10]
```
也可以通过行或列迭代的方式：

```python
>>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
...    for cell in row:
...        print(cell)
<Cell Sheet1.A1>
<Cell Sheet1.B1>
<Cell Sheet1.C1>
<Cell Sheet1.A2>
<Cell Sheet1.B2>
<Cell Sheet1.C2>
```

```python
>>> for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
...     for cell in col:
...         print(cell)
<Cell Sheet1.A1>
<Cell Sheet1.A2>
<Cell Sheet1.B1>
<Cell Sheet1.B2>
<Cell Sheet1.C1>
<Cell Sheet1.C2>
```
或者直接通过`rows`属性，或者`columns`属性。

```python
>>> ws = wb.active
>>> ws['C9'] = 'hello world'
>>> tuple(ws.rows)
((<Cell Sheet.A1>, <Cell Sheet.B1>, <Cell Sheet.C1>),
(<Cell Sheet.A2>, <Cell Sheet.B2>, <Cell Sheet.C2>),
(<Cell Sheet.A3>, <Cell Sheet.B3>, <Cell Sheet.C3>),
(<Cell Sheet.A4>, <Cell Sheet.B4>, <Cell Sheet.C4>),
(<Cell Sheet.A5>, <Cell Sheet.B5>, <Cell Sheet.C5>),
(<Cell Sheet.A6>, <Cell Sheet.B6>, <Cell Sheet.C6>),
(<Cell Sheet.A7>, <Cell Sheet.B7>, <Cell Sheet.C7>),
(<Cell Sheet.A8>, <Cell Sheet.B8>, <Cell Sheet.C8>),
(<Cell Sheet.A9>, <Cell Sheet.B9>, <Cell Sheet.C9>))
```

```python
>>> tuple(ws.columns)
((<Cell Sheet.A1>,
<Cell Sheet.A2>,
<Cell Sheet.A3>,
<Cell Sheet.A4>,
<Cell Sheet.A5>,
<Cell Sheet.A6>,
...
<Cell Sheet.B7>,
<Cell Sheet.B8>,
<Cell Sheet.B9>),
(<Cell Sheet.C1>,
<Cell Sheet.C2>,
<Cell Sheet.C3>,
<Cell Sheet.C4>,
<Cell Sheet.C5>,
<Cell Sheet.C6>,
<Cell Sheet.C7>,
<Cell Sheet.C8>,
<Cell Sheet.C9>))
```
## 只看value
可以使用`Worksheet.values`方法实现只看`sheet`里面的`value`。

```python
for row in ws.values:
   for value in row:
     print(value)
```
`Worksheet.iter_rows()` 和 `Worksheet.iter_cols()` 方法可以使用参数 `values_only` 只返回 `value`。
```python
for row in ws.iter_rows(min_row=1, max_col=3, \
		max_row=2, values_only=True):
    print(row)
---
(None, None, None)
(None, None, None)
```

# 数据存储

获得 Cell 对象以后，可以这样为其赋值：
```python
>>> c.value = 'hello, world'
>>> print(c.value)
'hello, world'

>>> d.value = 3.14
>>> print(d.value)
3.14
```
