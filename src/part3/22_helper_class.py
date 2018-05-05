# -*- coding: utf-8 -*-


import collections


# 定义成绩元祖，简单的而又不可变的数据类, 后续可以重写成类
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        """记录科目分数以及权重"""
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        """计算科目的平均分数"""
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):

    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        """返回学生的科目信息"""
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):

    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

    # add more function to extend the statistic info


# apply
book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('math')
math.report_grade(80, 0.10)
math.report_grade(90, 0.20)
math.report_grade(95, 0.30)
math.report_grade(93, 0.30)
print(albert.average_grade())
