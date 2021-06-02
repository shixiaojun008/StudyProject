# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a+b
#
# print('\n')
#
# j, k = 0, 1
# while k < 1000:
#     print(k, end=',')
#     n = k
#     m = j + k
#     j = n
#     k = m


def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


# 获取用户输入
# nterms = int(input("您要输出几项? "))

nterms = 10

# 检查输入的数字是否正确
if nterms <= 0:
    print("输入正数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(recur_fibo(i), end="\t")


print("\n")


# ******** 计算 n 的阶乘 **********

number = 5
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(number)
print("{0}的阶乘结果是:{1}".format(number, result))

