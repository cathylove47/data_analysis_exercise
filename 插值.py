import numpy as np
import matplotlib.pyplot as plt


# 选取一个函数中离散的点
x = np.linspace(0, 10, 11)
y = np.sin(x)

# 拉格朗日插值自定义的算法
def lagrange(x, y, x_i):
    """
    :param x: 插值点的横坐标
    :param y: 插值点的纵坐标
    :param x_i: 需要插值的点的横坐标
    :return: 返回插值点的纵坐标
    """
    # 初始化插值点的纵坐标
    y_i = 0
    # 遍历所有的插值点
    for i in range(len(x)):
        # 初始化插值基函数的值
        l_i = 1
        # 遍历所有的插值点
        for j in range(len(x)):
            # 排除i=j的情况
            if i != j:
                # 计算插值基函数的值
                l_i *= (x_i - x[j]) / (x[i] - x[j])
        # 计算插值点的纵坐标
        y_i += y[i] * l_i
    return y_i
# 生成插值函数,连续的100个点
x_i = np.linspace(0, 10, 100)
y_i = np.zeros(100)
for i in range(100):
    y_i[i] = lagrange(x, y, x_i[i])
# 绘制图像,插值函数与原函数
# 调用中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('拉格朗日插值')
plt.plot(x_i, y_i, label='插值函数')
plt.plot(x, y, 'o', label='原函数')
plt.legend()
plt.show()
# 误差分析
error = np.abs(y_i - np.sin(x_i))
plt.title('误差分析')
plt.plot(x_i, error)
plt.show()

    
