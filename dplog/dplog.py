# coding: utf-8

import logging
import logging.handlers
import inspect
from dptool import winAddColor
from dptool import linuxAddColor
from dptool import threadingLock


class Logger(object):
    '''
    LOG_FORMAT = [levelName] ascTime filePath function lineNumber: message
    LOG_LEVEL  = 10 logging.DEBUG
                 20 logging.INFO
                 30 logging.WARNING|WARN
                 40 logging.ERROR
                 50 logging.CRITICAL|FATAL
    '''
    LOG_FORMAT        = '[%(levelname)s] %(asctime)s %(message)s'
    TIME_FORMAT       = "%Y-%m-%d %H:%M:%S"
    FULL_FILE_PATH    = False
    LOG_LEVEL         = 10
    IS_CONSOLE        = (True, True)
    COLOR_ERROR       = ('red', None, 'bold')
    COLOR_WARNING     = ('yellow', None, 'bold')
    COLOR_INFO        = ('cyan', None, 'bold')
    COLOR_DEBUG       = ('green', None, 'bold')
    FILE_ERROR        = None
    FILE_WARNING      = None
    FILE_INFO         = None
    FILE_DEBUG        = None
    FILE_LOG          = None
    FILE_MAX_BYTES    = 128*1024*1024
    FILE_BACKUP_COUNT = 10
    __Ec = None
    __Wc = None
    __Ic = None
    __Dc = None
    __Ef = None
    __Wf = None
    __If = None
    __Df = None
    __C  = None
    __F  = None

    @staticmethod
    def _makeCLogger(logName, colorType):
        textColor, bgColor, style = colorType
        logger = logging.getLogger(logName)
        logger.setLevel(Logger.LOG_LEVEL)
        format = logging.Formatter(
            linuxAddColor(Logger.LOG_FORMAT, textColor, bgColor, style),
            Logger.TIME_FORMAT
        )
        handler = logging.StreamHandler()
        handler.setLevel(Logger.LOG_LEVEL)
        handler.setFormatter(format)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def _makeFLogger(logName, logFile):
        logger = logging.getLogger(logName)
        logger.setLevel(Logger.LOG_LEVEL)
        format = logging.Formatter(
            Logger.LOG_FORMAT,
            Logger.TIME_FORMAT
        )
        handler = logging.handlers.RotatingFileHandler(
            filename=logFile,
            mode='a',
            maxBytes=Logger.FILE_MAX_BYTES,
            backupCount=Logger.FILE_BACKUP_COUNT
        )
        handler.setLevel(Logger.LOG_LEVEL)
        handler.setFormatter(format)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def _initLogger(level):
        cLogger = None
        fLogger = None
        if Logger.IS_CONSOLE[0] is True:
            if Logger.IS_CONSOLE[1] is True:
                if not (Logger.__Ec and Logger.__Wc and Logger.__Ic and Logger.__Dc):
                    Logger.__Ec = Logger._makeCLogger('error_c', Logger.COLOR_ERROR)
                    Logger.__Wc = Logger._makeCLogger('warning_c', Logger.COLOR_WARNING)
                    Logger.__Ic = Logger._makeCLogger('info_c', Logger.COLOR_INFO)
                    Logger.__Dc = Logger._makeCLogger('debug_c', Logger.COLOR_DEBUG)
                if level == 'error':
                    cLogger = Logger.__Ec
                if level == 'warning':
                    cLogger = Logger.__Wc
                if level == 'info':
                    cLogger = Logger.__Ic
                if level == 'debug':
                    cLogger = Logger.__Dc
            elif Logger.IS_CONSOLE[1] is False:
                if not Logger.__C:
                    Logger.__C = Logger._makeCLogger('console', (None, None, None))
                cLogger = Logger.__C
        if Logger.FILE_ERROR is not None:
            if Logger.__Ef is None:
                Logger.__Ef = Logger._makeFLogger('error_f', Logger.FILE_ERROR)
        if Logger.FILE_WARNING is not None:
            if Logger.__Wf is None:
                Logger.__Wf = Logger._makeFLogger('warning_f', Logger.FILE_WARNING)
        if Logger.FILE_INFO is not None:
            if Logger.__If is None:
                Logger.__If = Logger._makeFLogger('info_f', Logger.FILE_INFO)
        if Logger.FILE_DEBUG is not None:
            if Logger.__Df is None:
                Logger.__Df = Logger._makeFLogger('debug_f', Logger.FILE_DEBUG)
        if Logger.FILE_LOG is not None:
            if Logger.__F is None:
                Logger.__F = Logger._makeFLogger('log_file', Logger.FILE_LOG)
        if level == 'error':
            fLogger = Logger.__Ef
        if level == 'warning':
            fLogger = Logger.__Wf
        if level == 'info':
            fLogger = Logger.__If
        if level == 'debug':
            fLogger = Logger.__Df
        return cLogger, fLogger

    @staticmethod
    def _handleMsg(msg):
        stack = inspect.stack()
        filePath = stack[-1][1]
        lineNum = stack[-1][2]
        if not Logger.FULL_FILE_PATH:
            filePath = filePath.split("/")[-1]
        funcName = stack[-2][3]
        return "%s %s [line %d]: %s" % (filePath, funcName, lineNum, msg)

    @staticmethod
    @threadingLock
    @winAddColor(COLOR_ERROR[0], COLOR_ERROR[1], COLOR_ERROR[2])
    def error(msg):
        cLogger, fLogger = Logger._initLogger('error')
        msg = Logger._handleMsg(msg)
        if cLogger is not None:
            cLogger.error(msg)
        if fLogger is not None:
            fLogger.error(msg)
        if Logger.__F is not None:
            Logger.__F.error(msg)

    @staticmethod
    @threadingLock
    @winAddColor(COLOR_WARNING[0], COLOR_WARNING[1], COLOR_WARNING[2])
    def warning(msg):
        cLogger, fLogger = Logger._initLogger('warning')
        msg = Logger._handleMsg(msg)
        if cLogger is not None:
            cLogger.warning(msg)
        if fLogger is not None:
            fLogger.warning(msg)
        if Logger.__F is not None:
            Logger.__F.warning(msg)

    @staticmethod
    @threadingLock
    @winAddColor(COLOR_INFO[0], COLOR_INFO[1], COLOR_INFO[2])
    def info(msg):
        cLogger, fLogger = Logger._initLogger('info')
        msg = Logger._handleMsg(msg)
        if cLogger is not None:
            cLogger.info(msg)
        if fLogger is not None:
            fLogger.info(msg)
        if Logger.__F is not None:
            Logger.__F.info(msg)

    @staticmethod
    @threadingLock
    @winAddColor(COLOR_DEBUG[0], COLOR_DEBUG[1], COLOR_DEBUG[2])
    def debug(msg):
        cLogger, fLogger = Logger._initLogger('debug')
        msg = Logger._handleMsg(msg)
        if cLogger is not None:
            cLogger.debug(msg)
        if fLogger is not None:
            fLogger.debug(msg)
        if Logger.__F is not None:
            Logger.__F.debug(msg)
