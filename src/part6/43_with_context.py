# -*- coding: utf-8 -*-
# @Author: denis
# @Date:   2018-05-09 10:27:25
# @Last Modified by:   denis
# @Last Modified time: 2018-05-09 11:00:21


"""

可以用with改写try/finally代码逻辑

用contextlib.contextmanager修饰器令函数支持with语句，不然要写辅助类实现__enter__和__exit__方法

contextmanager让函数的yield语句向with语句返回一个值

"""

import logging
from contextlib import contextmanager



def my_function():
	logging.debug('Some debug data')
	logging.error('Error log here')
	logging.debug('More debug data')


# 默认级别为warning，只会打印error信息
my_function()

'''
ERROR:root:Error log here
'''

# 定义一个情景管理器，更改原来log级别，最终设置原来级别
@contextmanager
def debug_logging(level):

	logger = logging.getLogger()
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield
	finally:
		logger.setLevel(old_level)


with debug_logging(logging.DEBUG):
	print("Inside:")
	my_function()

print("After: ")
my_function()

'''
Inside:
DEBUG:root:Some debug data
ERROR:root:Error log here
DEBUG:root:More debug data
After:
ERROR:root:Error log here
'''

# 使用带目标的with语句

# 类似文件打开的with语句

# with open('./somefile.txt', 'w') as handle:
# 	 handle.write("Some data saved!")


@contextmanager
def debug_logging2(level, name):

	logger = logging.getLogger(name)
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield logger
	finally:
		logger.setLevel(old_level)


with debug_logging2(logging.DEBUG, 'my-log') as logger:            # 除了能自己手动打印一些东西，然并卵
	logger.debug("This is my message")
	logging.debug("This is not print message")


logger = logging.getLogger('my-log')   # 后续获取这个log，但是这个log也已经设置回原来的级别了
logger.debug('Debug not print')
