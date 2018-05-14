# -*- coding: utf-8 -*-
# @Author: denis
# @Date:   2018-05-14 15:24:46
# @Last Modified by:   denis
# @Last Modified time: 2018-05-14 15:33:35


'''
python不是一个严格的限制private属性的
'''


class MyParentObject(object):
	def __init__(self):
		self.__private_field = 71


class MyChildObject(MyParentObject):

	def get_private_field(self):
		return self.__private_field           # raise error


a = MyChildObject()
a.get_private_field()           # raise error-- AttributeError: 'MyChildObject' object has no attribute '_MyChildObject__private_field'

'''
其实python访问私有方法是从类名进行变化访问的
但是这种直接访问的方法也不能一直用，因为如果发生超类(爷爷和孙子辈的类，是不容易知道这个方法的)，
对后面开发者是不友好的。 
同时只有一类情况是私有属性对超类好的，就是避免与子类发生属性重命名相冲突的问题。
'''
a._MyParentObject__private_field      # ok, 71


class MyClass(object):

	def __init__(self, value):

		# 用注释说明保护属性，应该是不变的，遵循大家都是成年人了，知道该如何使用
		# API文档中需要好好的注明。
		self._value = value


