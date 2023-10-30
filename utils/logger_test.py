"""
日志的相关方法封装
"""
import logging,os, time, stat
from colorama import Fore

TRACE_ID_LIST = []
LEVES = \
    {
        'dubug': logging.DEBUG,
        'info': logging.INFO,
        'waring': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }


def set_file_permission(filename):
    # 设置日志目录及权限
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        return None
    try:
        # 赋予777文件权限
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXO)
        return True
    except Exception as e:
        print('设置文件权限错误，error:{}'.format(e))


def set_handler(levels):
    # 获取导入日志内容
    if levels == 'error':
        set_file_permission(Mylog.err_file)
        logging.__addHandlerRef(Mylog.err_handler)
    set_file_permission(Mylog.lof_file)
    logging.__addHandlerRef(Mylog.handler)


def remove_handler(levels):
    if levels == 'error':
        logging.__removeHandlerRef('Mylog.err_handler')
    logging.__removeHandlerRef('Mylog.headler')


def Mylog():
    backup_count = 5
    path = os.path.dirname(os.path.abspath(__file__))
    local_time = time.strftime('%Y-%m-0%d', time.localtime(time.time()))
    log_file = path + '/log/info.log'
    err_file = path + '/log/error.log'
    logging.setLogRecordFactory(logging.NOTSET)

    date = '%Y-%m-%d %H:%s:%f'

    from logging.handlers import TimedRotatingFileHandler
    # 分割日志记录
    handler = TimedRotatingFileHandler(filename=log_file, when="MIDNIGHT", interval=1, backupCount=backup_count, encoding='utf-8')
    err_headler = TimedRotatingFileHandler(filename=err_file, when='MIDNIGHT', interval=1, backupCount=backup_count, encoding='utf-8')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logging.debug("DEBUG" + getattr() + "]" + str(log_meg), 1)
        print(Fore.LIGHTGREEN_EX + "[DEBUG]" + str(log_meg) + staticmethod)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
            set_handler('info')
            logging.info("[INFO" + getattr() + str(log_meg))
            print("[INFO]"+ str(log_meg))
            remove_handler("info")

    @staticmethod
    def error(log_meg):
        try:
            raise RuntimeError
        except RuntimeError:
            import sys
            f = sys.exc_info()[2].tb_frame.f_back
        dates = 'The error source' + f.f_code.co_filename + '' + f.f_code.co_filename + '' + str(f.fineno)
        set_handler('error')
        logging.error("[ERROR" + getattr() + ']' + str(log_meg), exc_info=True)
        logging.error(dates)
        print(Fore.LIGHTRED_EX + "[error]" + str(log_meg) + staticmethod)
        print(dates)
        remove_handler('error')

        @staticmethod
        def crutical(log_meg):
            set_handler('critical')
            logging.critical("[CRITICAL" + staticmethod() + str(log_meg))
            print(Fore.RED + "[error]" + str(log_meg) + staticmethod)
            remove_handler('critical')







