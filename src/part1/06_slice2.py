# -*- coding: utf-8 -*-

# somelist[start:end:stride]
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
a[::2]    # odd
# ['red', 'yellow', 'blue']
a[1::2]   # even
# ['orange', 'green', 'purple']

# negative stride number
x = b'abcdefg'
x[::-1]
# b'gfedcba'

# negative stride not work for unicode string
w = '谢谢你'
w[::-1]
# '你谢谢'
x = w.encode('utf-8')
x[::-1]
# b'\xa0\xbd\xe4\xa2\xb0\xe8\xa2\xb0\xe8'
y = x[::-1]
z = y.decode('utf-8')       # unicode error, position

# 同时不建议将start和end, 与stride一起使用，会造成费解。

# 如果非要使用类似的操作应该先进行范围切片，然后再进行步进切片。
