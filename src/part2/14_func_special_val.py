# -*- coding: utf-8 -*-


# 正确的版本, 抛出异常并在文档当中写明，方便使用者处理
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e


# 使用
# x, y = 5, 2
x, y = 5, 0
try:
    result = divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print("Result is %.1f" % result)


# wrong version
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
