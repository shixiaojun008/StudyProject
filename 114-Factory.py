#工厂模式
# 工厂模式 & 单列模式整合例子

class CarFactory:

    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return  cls.__obj

    def __init__(self):
        if CarFactory.__init_flag == True:
            print("Init........")
            CarFactory.__init_flag = False


    def createCar(self, brand):
        if brand == "Benz":
            return Benz()
        if brand == "BMW":
            return BMW()
        if brand == "BYD":
            return BYD()


class Benz:
    def CarInfo(self):
        print("We can create Benz")

class BMW:
    def CarInfo(self):
        print("We can create Benz")

class BYD:
    def CarInfo(self):
        print("We can create BYD")

factory01 = CarFactory()
factory01.createCar("BYD").CarInfo()

factory02 = CarFactory()
factory02.createCar("Benz").CarInfo()

print(factory01)
print(factory02)

