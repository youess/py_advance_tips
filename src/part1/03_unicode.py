# -*- coding: utf-8 -*-


"""
py3: str -> 包含unicode字符的序列，bytes是包含8位值的序列。
py2: str -> 包含8位值的序列，unicode是包含unicode字符的序列。

Unicode字符   ----> encode -----> 二进制数据
二进制数据    ----> decode -----> Unicode字符

"""


# in py3
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value
