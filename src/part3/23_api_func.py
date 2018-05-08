# -*- coding: utf-8 -*-
# @Author: denis
# @Date:   2018-05-08 15:02:38
# @Last Modified by:   denis
# @Last Modified time: 2018-05-08 15:20:22


'''

hook函数， 回调api代码

Python函数-->一级对象


'''

from collections import defaultdict


def log_missing():
	"""缺失key就打印log，并返回0作为键值"""
	print("Key added!")
	return 0


current = {'green': 12, 'blue': 3}
increments = [
	('red', 5),
	('blue', 17),
	('orange', 9)
]

# 2次missing报告打印
results = defaultdict(log_missing, current)
print('Before: ', dict(results))

for key, amount in increments:
	results[key] += amount

print("After: ", dict(results))


# 统计缺失个数
# ans1， 闭包
def increment_with_report(current, increments):

	added_count = 0

	def missing():
		nonlocal added_count
		added_count += 1
		return 0

	results = defaultdict(missing, current)
	for key, amount in increments:
		results[key] += amount
	return dict(results), added_count


print("Sreport 1:")
result, cnt = increment_with_report(current, increments)
assert cnt == 2
print(result, cnt)


# ans2, 辅助类
print("Sreport 2:")
class CountMissing(object):

	def __init__(self):
		self.added = 0

	def missing(self):
		self.added += 1
		return 0

counter = CountMissing()
results = defaultdict(counter.missing, current)
for key, amount in increments:
	results[key] += amount
print(dict(results), counter.added)


# ans3, 辅助类2
class BetterCountMissing(object):

	def __init__(self):
		self.added = 0

	def __call__(self):
		"""
		类可以充当带状态的闭包函数
		"""
		self.added += 1
		return 0


print("Sreport 3:")
counter = BetterCountMissing()
results = defaultdict(counter, current)
for key, amount in increments:
	results[key] += amount

print(dict(results), counter.added)
