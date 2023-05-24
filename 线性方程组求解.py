# 随机生成一个五阶以上的线性方程组
# 用高斯消元法求解

import numpy as np
import random
import matplotlib.pyplot as plt

# 生成一个随机的线性方程组
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

# 高斯消元法求解线性方程组
def solve_equation(A, b):
    # 初始化增广矩阵
    A_b = np.zeros((len(A), len(A) + 1))
    # 将系数矩阵和常数项合并
    A_b[:, :-1] = A
    A_b[:, -1] = b
    # 遍历所有的行
    for i in range(len(A_b)):
        # 将第i行的第i个元素变为1
        A_b[i] /= A_b[i][i]
        # 将第i列的其他行的第i个元素变为0
        for j in range(len(A_b)):
            if i != j:
                A_b[j] -= A_b[i] * A_b[j][i]
    # 返回解
    return A_b[:, -1]

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

# 随机生成一个方程并求解
A, b = generate_equation(5)
print_equation(A, b)
x = solve_equation(A, b)
print_solution(x)
