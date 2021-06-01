class Student:
    company = "Co.LT"  # 类属性
    count = 0  # 类属性

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是：{1},到校次数是{2}".format(self.name, self.score, self.count))

    @classmethod
    def print_company(cls):
        print("公司是{0}".format(cls.company))

    @staticmethod
    def print_sum(n1, n2):
        print("到校次数是:{}".format(n1 + n2))

    def __del__(self):
        print("销毁对象：{0}".format(self))


class Man:
    pass


s1 = Student("史沐晨", 98)
s1.count = 20
s1.say_score()
s1.print_company()
s1.print_sum(1, 2)

Student.print_company()

print("*****************************************************************")

stu = Student
s2 = stu("张天爱", 96)
s2.count = 30
print(s2)
s2.say_score()

print("*****************************************************************")


# 列出对象所有属性、方法
print(dir(s1))

# 对象的属性字典
print(s1.__dict__)

# pass 空语句

# isinstance(对象，类型)  判断对象是不是指定类型
print(isinstance(s1, Man))

print("*****************************************************************")

del s1
#del s2   销毁s1的同时 对应的s2也被销毁，调用销毁方法
