import matplotlib.pyplot as plt
import numpy as np

# 准备数据,将(x,y)坐标点进行输入
x = np.arange(80, 92, 2)  # x = 80,82,84,86,88,90
y = np.array([90, 84, 83, 80, 75, 68])
# 编写polyfit二次拟合函数

# 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
z1 = np.polyfit(x, y, 2)
# 使用poly1d方法获得多项式系数,按照阶数由高到低排列
p1 = np.poly1d(z1)
# 在屏幕上打印拟合多项式
print(p1)
# 求对应x的各项拟合函数值
fx = p1(x)
# 绘制坐标系散点数据及拟合曲线图
plot1 = plt.plot(x, y, '*', label='origin data')
plot2 = plt.plot(x, fx, 'r', label='polyfit data')
plt.xlabel('x-price')
plt.ylabel('y-amount')
plt.legend(loc=4)  # 指定legend的位置,类似象限的位置
plt.title('polyfit')
plt.show()


