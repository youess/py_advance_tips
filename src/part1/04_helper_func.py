# -*- coding: utf-8 -*-


from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
my_values

# 简单解析其中的字符
red = my_values.get('red', [''])[0] or 0
red

red = int(my_values.get('red', [''])[0] or 0)
red

# if/else表达式同时也要比and/or表示更加清晰
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

# 但是多次重复还是比较复杂
green = my_values.get('green', [''])
green = int(green[0]) if green[0] else 0
green


# 写成辅助函数帮助频繁使用问题
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


red = get_first_int(my_values, 'red')
red
