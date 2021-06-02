class Student:
    company = "Co.LT"  # 类属性
    count = 0  # 类属性

    __score = 97

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def say_score(self):
        print("{0}的分数是：{1},到校次数是{2}".format(self.name, self.__score, self.count))

    @classmethod
    def print_company(cls):
        print("公司是{0}".format(cls.company))

    @property                   #Python 装饰器
    def score(self):
        print("Get score ...{0}".format(self.__score))
        return self.__score

    @score.setter      #Python 装饰器
    def score(self, score):
        self.__score = score

    @staticmethod
    def print_sum(n1, n2):
        print("到校次数是:{}".format(n1 + n2))

    def __call__(self):
        print("计算结果出来啦。。。。。，年薪为：{0}".format(30000))

    def __PrintScore(self):
        print("私有方法，打印私有属性值__score：{0}".format(self.__score))

    def __del__(self):
        print("销毁对象：{0}".format(self))


class Man:
    sum1 = 100
    sum2 = 200

    def __call__(self):
        print("计算结果出来啦。。。。。，年薪为：{0}".format(self.sum1 + self.sum2))
        return self.sum1 + self.sum2

    def work(self):
        print("努力上班!")

def n_work(m):
        print("努力上班!赚钱娶媳妇！")

s1 = Student("史沐晨", 98)
s1.count = 20
s1.say_score()
s1.print_company()
s1.print_sum(1, 2)
s1()

print("*****************************************************************")

s1.score          # 像调用属性一样调用方法   @property
#s1.salary = 30000  # 报错， 只能访问，不能赋值

s1.score = 50000
s1.score

print("*****************************************************************")

Student.print_company()

print("私有属性值：{0}".format(s1._Student__score))      #  类的私有属性的访问
s1._Student__PrintScore()

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

sMan = Man()
sMan()

Man.work = n_work    # Man 类中的 work 方法被外部新的 n_work 方法动态替换为新的对象
sMan.work()

print("*****************************************************************")

del s1
# del s2   销毁s1的同时 对应的s2也被销毁，调用销毁方法
