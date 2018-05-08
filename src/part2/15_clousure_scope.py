# -*- coding: utf-8 -*-
# @Author: denis
# @Date:   2018-05-08 14:10:06
# @Last Modified by:   denis
# @Last Modified time: 2018-05-08 14:37:09


'''

比如对一些组里面的数字进行优先排序

'''


def sort_priority(numbers, group):

	found = False
	def helper(x):
		if x in group:
			found = True        # try to change
			return (0, x)
		return (1, x)
	numbers.sort(key=helper)
	return found


def sort_priority2(numbers, group):

	found = False           # py2, 利用list是改变的 found = [False]
	def helper(x):
		nonlocal found                  # nonlocal将变量搜查范围往上提高直到找到这个变量，参照sort_priority3
		if x in group:
			found = True        # try to change, found[0] = True
			return (0, x)
		return (1, x)
	numbers.sort(key=helper)
	return found


def sort_priority3(numbers, group):
	found = False

	def helper(x):

		def inner_helper(x):
			nonlocal found
			if x in group:
				found = True
				return (0, x)
			return (1, x)
		return inner_helper(x)

	numbers.sort(key=helper)

	return found


class Sorter(object):
	'''
	当代码很复杂，用nonlocal理解起来就比较麻烦，需要写辅助类帮助代码逻辑清晰。
	'''
	def __init__(self, group):
		self.group = group
		self.found = False

	def __call__(self, x):
		if x in self.group:
			self.found = True
			return (0, x)
		return (1, x)


if __name__ == '__main__':
	
	num_list = [8, 3, 1, 2, 5, 4]
	grp = [1, 3, 5]
	found = sort_priority(num_list, grp)
	# expected True, [1, 3, 5, 2, 4, 8]
	print('Try 1: ', found, num_list)           # False, [1, 3, 5, 2, 4, 8]

	found = sort_priority2(num_list, grp)
	print('Try 2: ', found, num_list)           # True, [1, 3, 5, 2, 4, 8]

	found = sort_priority3(num_list, grp)
	print('Try 3: ', found, num_list)           # True, [1, 3, 5, 2, 4, 8]

	sorter = Sorter(grp)
	num_list.sort(key=sorter)
	assert sorter.found is True