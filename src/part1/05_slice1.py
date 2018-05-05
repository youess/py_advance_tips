# -*- coding: utf-8 -*-

# somelist[start:end]
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:4]     # ['a', 'b', 'c', 'd']
a[-4:]    # last four, ['e', 'f', 'g', 'h']
a[3:-3]   # middle two, ['d', 'e'], last index will never reach
# start and end over limit will work OK, but index got wrong
a[-10:3]
a[:20]
a[10]   # raise list index error
# slice will copy original list
b = a[:]
assert b == a and b is not a
b[0] = 'aa'
b
a
