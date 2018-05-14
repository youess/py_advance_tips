# -*- coding: utf-8 -*-
# @Author: denis
# @Date:   2018-05-14 15:37:49
# @Last Modified by:   denis
# @Last Modified time: 2018-05-14 16:42:48


'''
python编程就是在编不同类的功能

如果定制子类比较简单，可以直接继承python的容器类型如list或dict

要想实现自定义的容器类型，可能需要编写大量的特殊方法，可以从collections.abc模块中
的抽象基类继承，确保编写的子类具备适当的接口和行为

'''

import copy
from collections.abc import Sequence


class FrequencyList(list):

	def __init__(self, members):
		super().__init__(members)

	def frequency(self):
		counts = {}
		for item in self:
			counts.setdefault(item, 0)
			counts[item] += 1
		return counts


foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'a'])
print(f'foo length is {len(foo)}')
foo.pop()
print(f'After pop: {repr(foo)}')
print(f'Frequency: {foo.frequency()}')


class BinaryNode(object):

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


class IndexableNode(BinaryNode):
	def _search(self, count, index):
		
		# 中序遍历

		found = None

		if self.left:
			found, count = self.left._search(count, index)

		if not found and count == index:
			found = self
		else:
			count += 1

		if not found and self.right:
			found, count = self.right._search(count, index)
		
		return found, count

	def __getitem__(self, index):
		found, _ = self._search(0, index)
		if not found:
			raise IndexError("Index out of range")
		return found.value


tree = IndexableNode(
	10,
	left=IndexableNode(
		5,
		left=IndexableNode(2),
		right=IndexableNode(
			6, right=IndexableNode(7))),
	right=IndexableNode(
		15, left=IndexableNode(11)))



print(f'11 in the tree? {11 in tree}')
print(f'17 in the tree? {17 in tree}')
print(f'Index 1 = {tree[1]}')
print(f'Tree is {list(tree)}')


class SequenceNode(IndexableNode):
	def __len__(self):
		_, count = self._search(0, None)
		return count



class BadType(Sequence):
	pass


# foo = BadType()        # 必须先实现__getitem__和__len__方法


class BetterNode(SequenceNode, Sequence):
	pass


tree = BetterNode(
	10,
	left=BetterNode(
		5,
		left=BetterNode(2),
		right=BetterNode(
			6, right=BetterNode(7))),
	right=BetterNode(
		15, left=BetterNode(11)))


# 自动具备Index, count等方法
print(f'Index of 7 is: {tree.index(7)}')
print(f'Count of 10 is: {tree.count(10)}')
