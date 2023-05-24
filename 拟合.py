import matplotlib.pyplot as plt
import numpy as np

# 准备数据,将(x,y)坐标点进行输入
x = np.arange(80, 92, 2)  # x = 80,82,84,86,88,90
y = np.array([90, 84, 83, 80, 75, 68])
# 编写最小二乘法二次拟合函数
def least_square(x, y):
    """
    :param x: x坐标点
    :param y: y坐标点
    :return: 返回拟合的系数
    """
    # 初始化矩阵
    A = np.zeros((3, 3))
    B = np.zeros((3, 1))
    # 计算矩阵A
    for i in range(3):
        for j in range(3):
            A[i][j] = np.sum(x ** (i + j))
    # 计算矩阵B
    for i in range(3):
        B[i][0] = np.sum(y * x ** i)
    # 求解矩阵A和B的逆矩阵
    A_inv = np.linalg.inv(A)
    # 求解拟合的系数
    C = np.dot(A_inv, B)
    return C
# 调用最小二乘法二次拟合函数
C = least_square(x, y)
# 生成拟合函数
x_i = np.linspace(80, 90, 100)
y_i = C[0] + C[1] * x_i + C[2] * x_i ** 2
# 打印函数
print('拟合函数为:y = %f + %fx + %fx^2' % (C[0], C[1], C[2]))
# 绘制图像
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('最小二乘法二次拟合')
plt.plot(x_i, y_i, label='拟合函数')
plt.plot(x, y, 'o', label='原函数')
plt.legend()
plt.show()
# 误差分析
error = np.abs(y - (C[0] + C[1] * x + C[2] * x ** 2))
plt.title('误差分析')
plt.plot(x, error)
plt.show()
