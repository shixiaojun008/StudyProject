class Person:
    __age = 18

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getInfo(self):
        print("姓名：{0}，年龄：{1}".format(self.name, self.__age))


'''
   
    1、继承的用法， 继承后的初始化，私有属性的用法
    

'''


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    def __str__(self):
        return "重写 __str__ 方法，返回新的描述，类的名字是：Student"

    def getInfo(self):
        # 测试supper()，代表父类的定义，而不是父类的对象
        super().getInfo()

        # 子类自己的方法
        print("姓名：{0}，年龄：{1}，成绩：{2}".format(self.name, self._Person__age, self.score))  # 父类的私有属性用法


class Teacher(Person):

    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def getInfo(self):
        print("姓名：{0}，年龄：{1}，工资：{2}".format(self.name, self._Person__age, self.salary))  # 父类的私有属性用法


stu01 = Student("史沐晨", 10, 100)
stu01.getInfo()

# 测试 __str__ 重写
print(stu01)

print("**" * 50)

tch01 = Teacher("史小军", 30, 2000)
tch01.getInfo()


print("**" * 50)


'''
# 通过 mro()方法查看类的结构
print(Student.mro())

# 通过 dir()方法查看类的所有属性
print(dir(stu01))

# __dict__ 查看属性
print(tch01.__dict__)

# __class__ 查看所属类
print(tch01.__class__)

# __bases__ 查看父类
print(Teacher.__bases__)

# __subclasses__ 查看子类列表
print(Person.__subclasses__())

'''




