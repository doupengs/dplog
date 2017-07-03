```
     _       _             
  __| |_ __ | | ___   __ _ 
 / _` | '_ \| |/ _ \ / _` |
| (_| | |_) | | (_) | (_| |
 \__,_| .__/|_|\___/ \__, |
      |_|   V-0.0.1  |___/    我有...最美好的初衷
```

## 用少量的代码输出漂亮的日志

#### 简单的例子

```python
# coding: utf-8

from dplog.dplog import Logger

Logger.error("123456789")
Logger.warning("123456789")
Logger.debug("123456789")
Logger.info("123456789")
```

#### 输出结果

![](/image/1.jpg)

## 参数介绍

```
! 参数的设置只有在初始化之前生效，即在没有调用过Logger.debug|info|warning|error中的一个函数之前

日志的默认的基本格式(但不建议修改)
    Logger.LOG_FORMAT = '[%(levelname)s] %(asctime)s %(message)s'
      * 总的格式, 其中 %(message)s 包含了 filePath functionName lineNumber: message
    Logger.TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
      * 时间的格式
    Logger.FULL_FILE_PATH = False
      * 是否使用绝对路径
  
 日志的默认输出级别
    Logger.LOG_LEVEL = 10
      * 10 logging.DEBUG
      * 20 logging.INFO
      * 30 logging.WARNING|WARN
      * 40 logging.ERROR
      * 50 logging.CRITICAL|FATAL

输出到控制台颜色的控制
    Logger.IS_CONSOLE = (True, True)
      * 第一个表示是否输出到控制台
      * 第二个表示是否带有颜色,只对Linux起作用,对Windows无效,默认以下颜色，且不改变
    Logger.COLOR_ERROR   = ('red', None, 'bold')
    Logger.COLOR_WARNING = ('yellow', None, 'bold')
    Logger.COLOR_INFO    = ('cyan', None, 'bold')
    Logger.COLOR_DEBUG   = ('green', None, 'bold')
      * 第一个表示字体颜色 red yellow green blue cyan purple black white
      * 第二个表示背景颜色 red yellow green blue cyan purple black white
      * 第三个表示文字效果 bold underline
      * 只对Linux起作用,对Windows无效,默认以上颜色，且不改变
    
写入文件
    Logger.FILE_ERROR   = None
    Logger.FILE_WARNING = None
    Logger.FILE_INFO    = None
    Logger.FILE_DEBUG   = None
    Logger.FILE_LOG     = None
      * 只要以上五个参数不为None, 就表示日志写入文件
      * 前四个是单独写入，例如把 [ERROR] 的日志写入 FILE_ERROR 中
      * FILE_LOG 则是全部记录
    Logger.FILE_MAX_BYTES    = 128*1024*1024
      * 每个日志文件最大的值, 默认128M
    Logger.FILE_BACKUP_COUNT = 10
      * 最多存储多少个日志文件
      * error.log  error.log.1  error.log.2  error.log.3  ...
```

参看[示例](https://github.com/doupengs/dplog/blob/master/test.py)

## 其他修改颜色效果

![](/image/2.jpg)

![](/image/4.jpg)

## 保存的日志

![](/image/3.jpg)

## 安装

```
pip install dist/dplog-x.x.x.tar.gz
或者
python setup.py install
```

## 更新日志

```
v-0.0.1
  只支持Linux下带有颜色输出
v-0.0.2
  加入dpcolor.py
  支持 Linux 和 Windows 下均带有颜色输出
  但 Linux 下支持通过参数关闭颜色输出，以及默认的颜色
     Windows 下不支持
```

#### dpcolor.py winAddColor-装饰器的介绍

```python
# coding: utf-8
# v-0.0.2

from dplog.dpcolor import winAddColor

@winAddColor('red', 'yellow', 'bold')
def print_text(obj):
    print obj

print_text('123456789')

# 由于 Windows 中的一些IDE或者自带的IDLE, logging 打印都是默认的红色, 所以在CMD窗口下有效
```

#### windows 下的效果

![](/image/5.jpg)
