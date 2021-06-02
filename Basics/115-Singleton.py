'''

    1、确保一个类只有一个对象
    2、提供一个访问该实例的全局访问点

'''


class MySingleton:
    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return  cls.__obj

    def __init__(self, name):
        if MySingleton.__init_flag == True:
            print("Init........")
            self.name = name
            MySingleton.__init_flag = False

sg01 = MySingleton("SG01")
sg02 = MySingleton("SG02")

print(sg01)
print(sg02)

sg03 = MySingleton("SG03")
print(sg03)