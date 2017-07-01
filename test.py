# coding: utf-8

from dplog.dplog import Logger


# ----参数含义参看 README.md----
Logger.LOG_LEVEL         = 10
# ----参数:输出到控制台(不建议修改)----
Logger.IS_CONSOLE        = (True, True)
Logger.COLOR_ERROR       = ('red', None, 'bold')
Logger.COLOR_WARNING     = ('yellow', None, 'bold')
Logger.COLOR_INFO        = ('cyan', None, 'bold')
Logger.COLOR_DEBUG       = ('green', None, 'bold')
# ----参数:日志写入部分----
Logger.FILE_ERROR        = None
Logger.FILE_WARNING      = None
Logger.FILE_INFO         = None
Logger.FILE_DEBUG        = None
Logger.FILE_LOG          = None
Logger.FILE_MAX_BYTES    = 128*1024*1024
Logger.FILE_BACKUP_COUNT = 10
# ----参数:日志格式(不建议修改)----
Logger.LOG_FORMAT        = '[%(levelname)s] %(asctime)s %(message)s'
Logger.TIME_FORMAT       = "%Y-%m-%d %H:%M:%S"
Logger.FULL_FILE_PATH    = False


if __name__ == '__main__':
    Logger.error("123456789")
    Logger.warning("123456789")
    Logger.debug("123456789")
    Logger.info("123456789")

