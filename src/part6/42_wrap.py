# -*- coding: utf-8 -*-


import functools

'''
装饰器能够帮助已有的函数在进行开始和结束之前添加额外的附加代码功能。
'''


def trace(func):

    @functools.wraps(func)      # 帮助修正返回函数的，能够保持原来的函数名
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args}, {kwargs}) -> {result}')
        return result
    return wrapper


@trace
def fibonacci(n):

    if n in (0, 1):
        return n
    return fibonacci(n-2) + fibonacci(n-1)


fibonacci(3)


print(fibonacci)
