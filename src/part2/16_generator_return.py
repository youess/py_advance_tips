# -*- coding: utf-8 -*-
# @Author: denis
# @Date:   2018-05-08 14:48:53
# @Last Modified by:   denis
# @Last Modified time: 2018-05-08 14:54:52


'''
使用列表可能的问题有2：

1. 代码拥挤，需要使用list的接口
2. 数据量大的时候容易内存爆炸

'''


def index_words(text):

	'''
	查找text中单词长度，以空格作为分割
	'''
	ret = []

	if text:
		ret.append(0)
	for idx, letter in enumerate(text):
		if letter == ' ':
			ret.append(idx + 1)

	return ret


def index_words_gen(text):

	if text:
		yield 0

	for idx, letter in enumerate(text):
		if letter == ' ':
			yield idx + 1



if __name__ == '__main__':
	
	address = 'Four score and seven years ago...'

	ret = index_words(address)
	print(ret)               # [0, 5, 11, 15, 21, 27]

	ret = index_words_gen(address)
	print(ret, list(ret))    # <generator object ...> [0, 5, 11, 15, 21, 27]
