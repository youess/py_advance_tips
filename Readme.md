

记录effective python的建议，并实际码一下代码看看效果。

利用工具ipython, `%history -f save_file.py -o 41-100`  -o表示同时保持输出。


## PART1 用pythonic的方式进行思考

1. [确认python版本](./src/part1/01_py_version.py).
2. [遵循PEP8风格](http://www.python.org/dev/peps/pep-0008)
3. [了解bytes, str和Unicode的区别](./src/part1/03_unicode.py)
4. [辅助函数替代复杂的表达式](./src/part1/04_helper_func.py)

## PART2 函数

14. [尽量用异常表示特殊情况，不要返回None](./src/part2/14_func_special_val.py)
15. [了解如何在闭包里使用外围作用域中的变量](./src/part2/15_clousure_scope.py)
16. [考虑用生成器代替直接返回的列表函数](./src/part2/16_generator_return.py)

## PART3 类与继承

22. [尽量使用辅助类，而不要用字典和元祖进行多重嵌套](./src/part3/22_helper_class.py)
23. [简单的接口应该接受函数而不是类的实例](./src/part3/23_api_func.py)

## PART4 元类与属性

29. [用纯属性取代get, set方法](./src/part4/29_pure_attr.py)

## PART5 并发与并行

36. [用subprocss模块管理子进程](./src/part5/36_subprocess.py)

## PART6 内置模块

42. [用functools.wraps定义函数修饰器](./src/part6/42_wrap.py)

## PART7 协作开发

49. [为每个函数，类和模块编写文档字符串](http://www.python.org/dev/peps/pep-0257)

## PART8 部署

54. [考虑用模块级别的代码配置不同的部署环境](./src/part8/env_deploy.py)
