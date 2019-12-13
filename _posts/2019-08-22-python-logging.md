---
layout: post
title: "python logging"
subtitle: "python logging"
date: 2019-08-22 00:05:00
author: "Randle"
catalog: true
mathjax: false
comments: true
tags:
    - Python
---

`Logging` 是一个很好用的日志工具箱，是python 标准库中的一个模块，可以很方便的添加到项目中。本篇文章较详细的介绍`logging`的使用方法。

# The Logging Module

Logging 是 Python标准库中的一个模块，初学者和专业团队的需求都能满足。在项目中加入`logging`，只需要`import`操作。

```python
import logging
```

导入 logging 模块后，可以使用 logger记录日志，默认情况下，有5个level表征事件的严重程度。每一个level有一个对应的方法，用来记录对应level的事件。按照时间严重性顺序，默认的levels是：

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Logging模块提供了默认的logger，这样不需要做很多工作就可以完成日志记录工作。

```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

上面程序的输出如下：

```shell
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

上面的输出格式，level，name，message，以冒号分隔，是默认的输出格式，是可配置的，后文介绍。

注意，没有打印`debug()` 和 `info()` 信息。这是因为，默认情况下，logging模块记录严重性高于`WARNING`的日志。这个level是可以配置的，可以理解为一个门槛level。也可以自定义level，但是，自定义level是个很不推荐的做法。


# Basic Configurations

可以使用`basicConfig(**kwargs)`方法配置logging：

> “You will notice that the logging module breaks PEP8 styleguide and uses `camelCase` naming conventions. This is because it was adopted from Log4j, a logging utility in Java. It is a known issue in the package but by the time it was decided to add it to the standard library, it had already been adopted by users and changing it to meet PEP8 requirements would cause backwards compatibility issues.” [(Source)](https://wiki.python.org/moin/LoggingPackage)

`basicConfig()`方法的常用参数如下：

- `level`: The root logger will be set to the specified severity level.
- `filename`: This specifies the file.
- `filemode`: If `filename` is given, the file is opened in this mode. The default is `a`, which means append.
- `format`: This is the format of the log message.

使用 `level`参数配置想要记录的level。同时，此项配置，可以记录验证程度高于此level的日志。

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
```
```shell
DEBUG:root:This will get logged
```
所有严重性为`DEBUG`或高于`DEBUG`的日志会被记录。

相似的，`filename`用来配置输出文件，`filemode`用来配置打开文件的模式。

```python
import logging

logging.basicConfig(filename='app.log', filemode='w', 
                    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
```
```shell
root - ERROR - This will get logged to a file
```
`basicConfig()`的其他配置参数，[这里](https://docs.python.org/3/library/logging.html#logging.basicConfig)

注意，`basicConfig()` 这个函数只能被执行一次。

如果`basicConfig()` 没有被调用过，`debug()`, `info()`, `warning()`, `error()`,和 `critical()`也会调用 `basicConfig()`，调用的时候不加任何参数。也就是说，调用上面几个函数的时候，已经调用了`basicConfig()`，只能调用一次。

`basicConfig()`默认配置为，输出到标准输出，日志格式如下：

```shell
ERROR:root:This is an error message
```

# Formatting the Output

你可以由程序传递任何可以转换为字符串的变量写到log中，有一些基本元素，可以很容易的添加到format中。记录进ID，level，messages，可以这么操作：
```python
import logging
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
```
```shell
18472-WARNING-This is a Warning
```

`format`可以采用 LogRecord 属性的任何顺序组成的字符串。完成的[可用属性列表](https://docs.python.org/3/library/logging.html#logrecord-attributes).

这里是另外一个加了日期和时间信息的例子：

```python
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', 
                    level=logging.INFO)
logging.info('Admin logged in')
```
```shell
2018-07-11 20:12:06,288 - Admin logged in
```

%(asctime)s 增加 LogRecord的创建时间，时间可是可以使用 datefmt 属性配置。

```python
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', 
                    datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')
```

```shell
12-Jul-18 20:53:19 - Admin logged out
```

更过时间格式 [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

## Logging Variable Data

很多情况下，日志信息中会包含动态变量，logging方法的输入参数为字符串，所以，通过变量构造一个字符串是一个很自然的想法，然而，有一个更方便的做法就是，传入格式字符串和变量值，示例如下：

```python
import logging

name = 'John'

logging.error('%s raised an error', name)
```
```shell
ERROR:root:John raised an error
```

Python3.6中引入的 [f-strings](https://realpython.com/python-f-strings/) 也是此问题很好的解决方案。

```python
import logging
name = 'John'
logging.error(f'{name} raised an error')
```
```shell
ERROR:root:John raised an error
```

## Capturing Stack Traces

Logging模块也允许捕捉应用中的全栈跟踪数据。如果`exc_info`置为`True`，可以捕捉异常信息。

```python
import logging
a = 5
b = 0
try:
	c = a / b
except Exception as e:
	logging.error("Exception occurred", exc_info=True)
```
```shell
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
[Finished in 0.2s]
```

如果 `exc_info` 没有置为`True`，上面的程序不会输出异常信息。想像下如果排查问题时发现日志信息是下面这样是不是很崩溃。

```shell
ERROR:root:Exception occurred
```

`logging.exception()`相当于`logging.error(exc_info=True)`。

```python
import logging
a = 5
b = 0
try:
	c = a / b
except Exception as e:
	logging.exception("Exception occurred")
```
```shell
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
[Finished in 0.2s]
```
使用`logging.exception()`记录的日志，level 为`ERROR`，如果想要其他的level，可以使用对应的日志方法（debug，info等）这是参数 `exc_info` 为 `True`.


# Classes and Functions

logging 有一个默认的 `logger` 是 `root`，直接调用`logging.debug()`类似的操作，会使用默认的 logger。也可以自定义 logger 使用 [Logger类](https://realpython.com/python3-object-oriented-programming/)，尤其是程序有多个模块的时候。下面对logging中的类和函数简要介绍。

下面是 logging 中最常用的类：

- **Logger:** Logger 对象实例在程序中直接调用函数。
- **LogRecord:** `Logger` 自动生成 `LogRecord`对象，`LogRecord` 中包含即将记录的日志的所有信息，包括 `function`，`line number`,` message`等。
- **Handler:** `Handler`把 `LogRecord` 发送到需要的输出目标，比如 console或者 file。`Handler` 是  `StreamHandler`, `FileHandler`, `SMTPHandler`, `HTTPHandler`这些类的基类。这些子类把logging输出发送到对应的目标，如`sys.stdout` 或者磁盘文件。
- **Formatter:** Formatter用来指定输出日志的格式。

这些类中，最常用的是 `Logger` 类，通过模块级函数`logging.getLogger(name)`初始化。使用相同的`name`多次调用 `getLogger()`会返回相同`Logger`的引用。下面是一个例子：
```python
import logging

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
```
```shell
This is a warning
```

这个脚本创建了一个logger，名字是 `example_logger`,与root logger不同，自定义logger的名字不是默认的，需要指定。配置一个format显示logger名字，可以得到下面的结果。

```
WARNING:example_logger:This is a warning
```

与 root logger 不同，自定义的 logger 不能使用 `basicConfig()`方法配置，需要使用 Handlers 和 Formatters配置

> “It is recommended that we use module-level loggers by passing `__name__` as the name parameter to `getLogger()` to create a logger object as the name of the logger itself would tell us from where the events are being logged. `__name__` is a special built-in variable in Python which evaluates to the name of the current module.” [(Source)](https://docs.python.org/3/library/logging.html#logger-objects)

# Using Handlers

`handlers`能够实现对自定义`logger`的配置，并且能够将日志发送到不同的地方。`handlers`能够配置将日志发送到标准输出，文件，http，或者通过smtp发送到邮件。

一个`logger`可以有多个`handler`，意味着，可以将日志同时存文件和通过邮件发出。

`handler`中也可以配置危险等级，能够实现，同一个`logger`的不同`handler`，拥有不同的危险等级。下面是一段示例程序：

```python
# logging_example.py

import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
```
```shell
__main__ - WARNING - This is a warning
__main__ - ERROR - This is an error
```
`logger.warning()`创建一个`LogRecord`，其持有此次事件的所有信息，将信息发送给所有的`Handlers`，包括`c_handler`和`f_handler`。

`c_handler`是一个`StreamHandler`，level 为 WARNING ，拿到LogRecord 的信息后，按照指定格式，生成日志信息，并打印到 console 。`f_handler`是一个`FileHandler`，level 为 `ERROR`，将忽略 LogRecord，因为 LogRecord 的level是 WATNING。

当`logger.error()`被调用的时候，`c_handler`的动作与前面相同，`f_handler` 获得 level 为 ERROR 的 LogRecord。所以，像 `c_handler` 那样生成输出，但是它把信息写到指定的文件，而不是打印到标准输出。

```shell
2018-08-03 16:12:21,723 - __main__ - ERROR - This is an error
```

这里的 `__main__`对应着日志格式中的`name`，若上面那段程序在某个模块中，并且模块被导入到其他模块，`name`则会对应显示模块的名字。

```python
# run.py
import logging_example
```

```shell
logging_example - WARNING - This is a warning
logging_example - ERROR - This is an error
```
# Other Configuration Methods

logging的配置，可以像前面那样使用模块和类函数，也可以通过配置文件或者[dictionary](https://realpython.com/python-dicts/) ，通过`fileConfig()`或 `dictConfig()`加载。这些是很有用的，当你想改变正在运行的应用的配置。

下面是一个配置文件的例子：

```shell
#Config File
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=consoleHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[formatter_sampleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```
上面的文件，有两个 logger，一个 handler， 一个 formatter。他们的名字定义好以后，通过在名字前面加 logger ,handler,和formatter，并且通过下划线分割，作为标签，对具体内容进行配置。

加载这个配置文件，可以使用 `fileConfig()`:

```python
import logging
import logging.config

logging.config.fileConfig(fname='file.conf', 
                          disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
```

```shell
2018-07-13 13:57:45,467 - __main__ - DEBUG - This is a debug message
```

配置文件的路径作为参数传递给 `fileConfig()` ， 参数`disable_existing_loggers`用来决定，当加载配置文件函数的时候，是否保留当前存在的loggers，默认值为`True`。

这是一个相同的配置文件，文件格式为 YAML格式，用于 dictionary 方法：

```shell
#YAML
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  sampleLogger:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```
这是一个使用 yaml 配置文件的例子：

```python
import logging
import logging.config
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
```
```shell
2018-07-13 14:05:03,766 - __main__ - DEBUG - This is a debug message
```

# 参考资料
[Logging in Python](https://realpython.com/python-logging/)