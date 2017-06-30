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

from dplog import Logger

Logger.error("123456789")
Logger.warning("123456789")
Logger.debug("123456789")
Logger.info("123456789")
```

#### 输出结果

![](/image/1.jpg)

## 参数介绍

```
日志的默认的基本格式(但不建议修改)
    Logger.LOG_FORMAT = '[%(levelname)s] %(asctime)s %(message)s'
      * 总的格式, 其中 %(message)s 包含了 filePath functionName lineNumber: message
    Logger.TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
      * 时间的格
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
      * 第二个表示是否带有颜色
    Logger.COLOR_ERROR   = ('red', None, 'bold')
    Logger.COLOR_WARNING = ('yellow', None, 'bold')
    Logger.COLOR_INFO    = ('cyan', None, 'bold')
    Logger.COLOR_DEBUG   = ('green', None, 'bold')
      * 第一个表示字体颜色 red yellow green blue cyan purple black white
      * 第二个表示背景颜色 red yellow green blue cyan purple black white
      * 第三个表示文字效果 bold underline
    
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

## 保存的日志

![](/image/3.jpg)

## 安装

```
pip install dist/dplog-x.x.x.tar.gz
或者
python setup.py install
```
