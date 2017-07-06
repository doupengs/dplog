# coding: utf-8

import ctypes
import platform
import threading

__SYSTEM = platform.system()
__LOCK = threading.Lock()

def threadingLock(func):
    def inside(*args, **kwargs):
        __LOCK.acquire():
        func(*args, **kwargs)
        __LOCK.release()
    return inside

def winAddColor(textColor=None, bgColor=None, style=None):
    '''
    :param textColor: red yellow green blue cyan purple black white
    :param bgColor: red yellow green blue cyan purple black white
    :param style: bold
    :function: this is a decorator that gives the output with|without a color
    '''
    def decorator(func):
        if (textColor, bgColor, style) == (None, None, None) or __SYSTEM == 'Linux':
            def logger(*args, **kwargs):
                func(*args, **kwargs)
        else:
            def logger(*args, **kwargs):
                textColors = {
                    'black' : 0x0,
                    'blue'  : 0x01,
                    'green' : 0x02,
                    'cyan'  : 0x03,
                    'red'   : 0x04,
                    'purple': 0x05,
                    'yellow': 0x06,
                    'white' : 0x07,
                }
                bgColors = {
                    'black' : 0x0,
                    'blue'  : 0x10,
                    'green' : 0x20,
                    'cyan'  : 0x30,
                    'red'   : 0x40,
                    'purple': 0x50,
                    'yellow': 0x60,
                    'white' : 0x70,
                }
                styles = {
                    'bold_text': 0x08,
                    'bold_bg'  : 0x80,
                }
                t = textColors[textColor] if textColor in textColors else textColors['white']
                b = bgColors[bgColor] if bgColor in bgColors else bgColors['black']
                s = 0x0
                if style == 'bold':
                    s |= styles['bold_text']
                    if b != bgColors['black']:
                        s |= styles['bold_bg']
                stdHandle = ctypes.windll.kernel32.GetStdHandle(-11)
                ctypes.windll.kernel32.SetConsoleTextAttribute(stdHandle, t | b | s)
                func(*args, **kwargs)
                ctypes.windll.kernel32.SetConsoleTextAttribute(stdHandle, textColors['white'])
        return logger
    return decorator


def linuxAddColor(obj, textColor=None, bgColor=None, style=None):
    '''
    :param obj: handle message 
    :param textColor: red yellow green blue cyan purple black white
    :param bgColor: red yellow green blue cyan purple black white
    :param style: bold underline 
    :function: return obj with|without a color
    '''
    if (textColor, bgColor, style) == (None, None, None) or __SYSTEM == 'Windows':
        return obj
    textColors = {
        'black' : '\033[30m',
        'red'   : '\033[31m',
        'green' : '\033[32m',
        'yellow': '\033[33m',
        'blue'  : '\033[34m',
        'purple': '\033[35m',
        'cyan'  : '\033[36m',
        'white' : '\033[37m',
    }
    bgColors = {
        'black' : '\033[40m',
        'red'   : '\033[41m',
        'green' : '\033[42m',
        'yellow': '\033[43m',
        'blue'  : '\033[44m',
        'purple': '\033[45m',
        'cyan'  : '\033[46m',
        'white' : '\033[47m',
    }
    styles = {
        'bold'     : '\033[1m',
        'underline': '\033[4m',
    }
    end = '\033[0m'
    textColor = textColors[textColor] if textColor in textColors else ''
    bgColor = bgColors[bgColor] if bgColor in bgColors else ''
    style = styles[style] if style in styles else ''
    return '%s%s%s%s%s' % (textColor, bgColor, style, obj, end)
