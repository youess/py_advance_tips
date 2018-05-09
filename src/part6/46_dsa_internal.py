# -*- coding: utf-8 -*-
# @Author: denis
# @Date:   2018-05-08 19:27:16
# @Last Modified by:   denis
# @Last Modified time: 2018-05-09 10:15:39


import collections as ct
import heapq as hq
import bisect
import itertools as it


#################################################
# 双向队列 deque
# 头尾插入或删除，常数时间, FIFO
# 比较list, list从头部插入或移除元素，消耗线性时间
#################################################


fifo = ct.deque()
fifo.append(1)       # Producer
x = fifo.popleft()   # Consumer


def test_deque(n=10000, left=True):
	fifo = ct.deque()
	n = int(n)
	if left:
		for _ in range(n):
			fifo.appendleft(30)
			fifo.popleft()
	else:
		for _ in range(n):
			fifo.append(30)
			fifo.pop()


def test_list(n=1000, left=True):
	a = []
	n = int(n)
	if left:
		for _ in range(n):
			a.insert(0, 1)
			a.remove(1)
	else:
		for _ in range(n):
			a.append(1)
			a.pop()


''' run in ipython
# 116 ms ± 17.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit -n 1 test_deque(1000000, True)
# 103 ms ± 1.66 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit -n 1 test_deque(1000000, False)
# 191 ms ± 1.31 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit -n 1 test_list(1000000, True)
# 359 ms ± 41.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit -n 1 test_list(1000000, False)
'''

#################################################
# 有序字典
# python默认的字典是无序的，可能刚开始是看起来是有顺序的
# 但是由于是fast hash table可能会发生碰撞，顺序会发生改变。
# OrderedDict类能够按照插入的顺序保留键值在字典的次序
#################################################


a = ct.OrderedDict()
a['foo'] = 1
a['bar'] = 2
b = ct.OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for av, bv in zip(a.values(), b.values()):
	print(av, bv)

'''
1 red
2 blue
'''

#################################################
# 带默认值的字典
#################################################

# 默认的字典
stats = {}
key = 'my_counter'
if key not in stats:
	stats[key] = 0
stats[key] += 1

# 默认值为0
stats = ct.defaultdict(int)
stats['my_counter'] += 1

# 默认值为[]
ct.defaultdict(list)

# 默认为定制返回函数，这个函数负责返回一个默认值对象
ct.defaultdict(lambda : ct.deque())


#################################################
# 堆队列
# 能够在list对象当中创建堆结构
# 要维持一个排序的序列，这个方法是很好，heapq的操作与
# list长度的对数成正比。
#################################################


a = []
hq.heappush(a, 5)
hq.heappush(a, 3)
hq.heappush(a, 7)
hq.heappush(a, 4)

a[0]         # 3, 返回的是最小值

for _ in range(4):
	print(hq.heappop(a), end=' ')
print()  # 3 4 5 7


#################################################
# 二分查找
#################################################


# 直接索引
x = list(range(10**8))

bisect.bisect_left(x, 991234)

'''
# 18.9 ms ± 2.06 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit -n 1 x.index(991234)
# The slowest run took 10.50 times longer than the fastest. This could mean that an intermediate result is being cached.
# 1.71 µs ± 2.33 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit -n 1 bisect.bisect_left(x, 991234)
'''

#################################################
# 迭代器相关的工具
#################################################


# 迭代器连接函数

## 多个迭代器按照顺序连成一个迭代器
list(it.chain([1, 2, 3], [4, 5], [6], (3, 5, 60)))   # [1, 2, 3, 4, 5, 6, 3, 5, 60]

## 无限循环某个迭代器中的元素
break_idx = 0
for e in it.cycle([1, 2, 3]):
	print(e, end=' ')
	if break_idx > 50:
		break
	break_idx += 1
print()

## 复制迭代器
dd = it.tee([1, 2, 3], 2)
# (<itertools._tee object, <itertools._tee object)
print(dd)
a, b = dd
# [1, 2, 3] [1, 2, 3]
print(list(a), list(b))

## 应对不同长度的迭代器, zip
for a, b in zip([1, 2, 3, 4], [1, 2, 3]):
	print(a, b)
'''
1 1
2 2
3 3
'''
for a, b in it.zip_longest([1, 2, 3, 4], [1, 2, 3]):
	print(a, b)
'''
1 1
2 2
3 3
4 None
'''

# 从迭代器当中过滤元素

## 切割
a = range(4)
b = it.islice(a, 1, 3)    # 不进行复制的情况下，根据索引值获取
print(list(a), list(b))   # [0, 1, 2, 3] [1, 2]

## filter
a = range(10)
b = it.takewhile(lambda x: x < 5, a)
print(list(b))      # [0, 1, 2, 3, 4]


a = [1, 4, 6, 3, 8, 9]
c = it.dropwhile(lambda x: x < 5, a)   # 从判断函数初次判定为False的地方，逐个返回
print(list(c))      # [6, 3, 8, 9]

d = it.filterfalse(lambda x: x < 5, a)  # 去除任何不满足条件的元素
print(list(d))      # [6, 8, 9]


# 能够把迭代器中的元素组合起来

## 笛卡儿积组合
a = it.product([1, 2], ['a', 'b'], ['-', '+'])
print(list(a)) 
'''
[(1, 'a', '-'), (1, 'a', '+'), (1, 'b', '-'), (1, 'b', '+'), (2, 'a', '-'), (2, 'a', '+'), (2, 'b', '-'), (2, 'b', '+')]
'''

## 有序组合，包含了相同元素，不同位置的组合
a = it.permutations([1, 2, 3, 4], 2)
print(list(a))
'''
[(1, 2),
 (1, 3),
 (1, 4),
 (2, 1),
 (2, 3),
 (2, 4),
 (3, 1),
 (3, 2),
 (3, 4),
 (4, 1),
 (4, 2),
 (4, 3)]
'''

## 无序组合
a = it.combinations([1, 2, 3, 4], 2)
print(list(a))
'''
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
'''

