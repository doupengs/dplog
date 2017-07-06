# coding: utf-8

from dplog import logger


# ----参数含义参看 README.md----
logger.LOG_LEVEL         = 10
# ----参数:输出到控制台(不建议修改)----
logger.IS_CONSOLE        = (True, True)
logger.COLOR_ERROR       = ('red', None, 'bold')
logger.COLOR_WARNING     = ('yellow', None, 'bold')
logger.COLOR_INFO        = ('cyan', None, 'bold')
logger.COLOR_DEBUG       = ('green', None, 'bold')
# ----参数:日志写入部分----
logger.FILE_ERROR        = None
logger.FILE_WARNING      = None
logger.FILE_INFO         = None
logger.FILE_DEBUG        = None
logger.FILE_LOG          = None
logger.FILE_MAX_BYTES    = 128*1024*1024
logger.FILE_BACKUP_COUNT = 10
# ----参数:日志格式(不建议修改)----
logger.LOG_FORMAT        = '[%(levelname)s] %(asctime)s %(message)s'
logger.TIME_FORMAT       = "%Y-%m-%d %H:%M:%S"
logger.FULL_FILE_PATH    = False


if __name__ == '__main__':
    logger.error("123456789")
    logger.warning("123456789")
    logger.debug("123456789")
    logger.info("123456789")

