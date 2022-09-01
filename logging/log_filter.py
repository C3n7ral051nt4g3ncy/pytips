import logging
import sys

class MyFilter(logging.Filter):
    def filter(self, record):
        return record.funcName != 'a'

logger = logging.getLogger('filter_test')
logger.addFilter(MyFilter())

def a():
    """
    Ignore this function's log messages
    """
    logger.debug('Message from function a')

def b():
    logger.debug('Message from B')

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    a()
    b()