# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
# 可写函数说明
def printinfo(arg1, *vartuple):
    '''打印任何传入的参数'''
    print("输出: {0}".format(arg1))
    for var in vartuple:
        print(var, end=" ")
    return

# 调用printinfo 函数
help(printinfo.__doc__)
printinfo(10)
printinfo(70, 60, 50)

print("\n")
print ("**********************************************")

# 可写函数说明
# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    '''打印任何传入的参数'''
    print("输出: {0}".format(arg1))
    print(vardict)

# 调用printinfo 函数
printinfo(1, a=2, b=3)

print()
print ("**********************************************")

# 如果单独出现星号 * 后的参数必须用关键字传入
def f(a, b, *, c):
    return a + b + c
# f(1, 2, 3)  错误的调用方式

print("输出函数值：{0}".format(f(1, 2, c=3)))

print ("**********************************************")

''' 传递可变对象 '''
a = [10,20]
print(id(a))
print (a)
print ("**********************************************")
def test01(m):
    print(id(m))
    m.append(30)
    print(id(m))
    print(m)

test01(a)



