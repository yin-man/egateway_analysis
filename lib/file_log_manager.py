# log_manager module wrapper modules of logging
# to support data_collect personalized log write.

from os.path import dirname, abspath, sep
PWD = dirname(abspath(__file__))
log_dir = dirname(dirname(PWD)) + sep + 'log'

import logging
import traceback
from logging.handlers import RotatingFileHandler

import jsonpickle


class FileLogManager(object):
    """LogManager instances are used to write module log & process rotate.

    LogManager fulfill following parts:
    1.    shelter logging module details from business modules;
    2.    can rotate different modules in different ways;

    Attributes:
        _logger: logger instance

    """

    def __init__(self, module, debug=False, log_dir=log_dir, maxBytes=1073741824, backupCount=10):
        """init a LogManager instance

        Args:
            module: A String module name, different module write info different file
            maxBytes: An Integer, rotate when log size arrive at maxBytes
            backupCount: An Integer, keep backupCount log files while rotate

        """
        self._logger = logging.getLogger(module)
        if len(self._logger.handlers) >= 2:
            # 如果不添加此逻辑，如果在同一个程序冲，多次初始化一个module的日志对象，会导致日志重复记录
            return
        log_file = log_dir + sep + module + '.log'
        rhandler = RotatingFileHandler(log_file, 'a', maxBytes, backupCount)
        formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s -  %(message)s')
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(rhandler)

        rhandler.setFormatter(formatter)
        if debug is False:
            rhandler.setLevel(logging.INFO)
        else:
            rhandler.setLevel(logging.DEBUG)

    def write_log(self, msg, log_level='info'):
        """proxy logger's log record methods

        Args:
            log_level: A String log level
            msg: A String  message for record

        Returns:
            ret: An Boolean used to indicate whether write log success/fail

        """

        try:
            if not isinstance(msg, str):
                msg = jsonpickle.encode(msg)
            getattr(self._logger, log_level)(msg)
        except AttributeError as e:
            self._logger.debug(e)
        except Exception as e:
            msg += " - (%s) " % traceback.format_exc()
            self._logger.error(msg)
        else:
            return True

        return False

    def error(self, msg):
        return self.write_log(msg, 'error')

    def info(self, msg):
        return self.write_log(msg, 'info')

    def warn(self, msg):
        return self.write_log(msg, 'warn')

    def debug(self, msg):
        return self.write_log(msg, 'debug')

    def critical(self, msg):
        return self.write_log(msg, 'critical')


if __name__ == '__main__':
    lm = FileLogManager('sync_dev_group', debug=True)
    lm.write_log('record msg with uuid')
    lm.write_log('record msg without uuid', 'debug')
    lm2 = FileLogManager('sync_dev_group', debug=True)
    lm2.write_log('record msg with uuid2')
    lm2.write_log('record msg without uuid2', 'debug')

    lm = FileLogManager('sync_dev_group2', debug=True)
    lm.write_log('record msg with uuid')
    lm.write_log('record msg without uuid', 'debug')
    lm2 = FileLogManager('sync_dev_group2', debug=True)
    lm2.write_log('record msg with uuid2')
    lm2.write_log('record msg without uuid2', 'debug')
