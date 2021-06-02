'''
    1、使用组合实现代码的复用

'''

class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "重写 __str__ 方法，返回新的描述，类的名字是：Student"

    def getInfo(self):
        # 子类自己的方法
        print("姓名：{0}，年龄：{1}，成绩：{2}".format(self.name, self.age, self.score))  # 父类的私有属性用法


class Teacher:

    def __init__(self, student, salary):
        self.student = student
        self.salary = salary

    def getInfo(self):
        print("姓名：{0}，年龄：{1}，工资：{2}".format(self.student.name, self.student.age, self.salary))


stu = Student("史沐晨", 10, 100)

tch = Teacher(stu, 3000)

tch.student.getInfo()
tch.getInfo()
