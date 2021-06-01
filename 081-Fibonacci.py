import numpy as np
import numpy.matlib


### *****************方法一 生成数列************************
def fib_matrix(n):
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        print(int(res[0][0]), end="\t")

# 调用
print("*****************方法一 生成数列************************")
fib_matrix(50)


print("\n")

### *****************方法二 生成数列************************
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回是matrix类型
    return np.linalg.matrix_power(Matrix, n)

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list

# 调用
print("*****************方法二 生成数列************************")
print(Fibonacci_Matrix(50))



### pow 速度 比 双**号快, np.linalg.matrix_power也是一种方法