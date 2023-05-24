import  numpy as np
import matplotlib.pyplot as plt
import random

# 随机生成一个常微分方程组
def generate_equation(n):
    # 初始化系数矩阵
    A = np.zeros((n, n))
    # 初始化常数项
    b = np.zeros(n)
    # 遍历所有的行
    for i in range(n):
        # 遍历所有的列
        for j in range(n):
            # 生成一个随机的系数
            A[i][j] = random.randint(-10, 10)
        # 生成一个随机的常数项
        b[i] = random.randint(-10, 10)
    return A, b

# 构造求数值解的方法
def solve_equation(A, b, x0, h, epoches):
    # 初始化解
    x = np.zeros((len(A), epoches))
    x[:, 0] = x0
    # 遍历所有的列
    for i in range(1, epoches):
        # 计算下一个解
        x[:, i] = x[:, i - 1] + h * np.dot(A, x[:, i - 1]) + h * b
    # 返回解
    return x

# 打印方程组
def print_equation(A, b):
    # 遍历所有的行
    for i in range(len(A)):
        # 遍历所有的列
        for j in range(len(A)):
            # 打印系数
            print(A[i][j], end=' ')
        # 打印等号
        print('= ', end='')
        # 打印常数项
        print(b[i])

# 打印解
def print_solution(x):
    # 遍历所有的解
    for i in range(len(x)):
        # 打印解
        print('x' + str(i + 1) + ' = ', x[i])

# 生成一个随机的常微分方程组
A, b = generate_equation(5)
# 打印方程组
print_equation(A, b)
# 求解方程组
x = solve_equation(A, b, np.array([1, 1, 1, 1, 1]), 0.01, 1000)
# 打印解
print_solution(x[:, -1])
