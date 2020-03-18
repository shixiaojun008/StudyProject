# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var, end=" ")
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

print("\n")

# 可写函数说明
# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    # "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

print("\n")

# 如果单独出现星号 * 后的参数必须用关键字传入
def f(a, b, *, c):
    return a + b + c
# f(1, 2, 3)  错误的调用方式

print(f(1, 2, c=3))
