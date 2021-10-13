
# 1、导包：loguru
from loguru import logger

# 2、调用不同的日志方法

# 日志级别：
'''
调试日志：debug()  默认值10
一般日志：info()   默认值20
警告日志：warning()   默认值40
成功日志：success()   默认值30
错误日志：error()     默认值50
'''

# 输出到文件 add()方法
logger.add('test.log',format='{time} {level} {message}',level='INFO')

logger.debug('这是一条debug日志')
logger.info('这是一个info日志')
logger.warning('这是一个warning日志')
logger.success('这是一个success日志')
logger.error('这是一个error日志')

logger.info('小明今年{}岁',12)


