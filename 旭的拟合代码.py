import numpy as np
import matplotlib.pyplot as plt

class polyfit():
    def __init__(self, n):
        self.n = n + 1
        self.weight = np.random.randn(n + 1)

    def fit(self, X, y, epoches=1000, lr=0.001):
        for epoch in range(epoches):
            grads = np.zeros(self.n)
            for i in range(len(X)):
                x = np.array([X[i] ** k for k in range(self.n)])
                grads += 2 * x * (np.dot(self.weight, x) - y[i])
            grads /= len(X)
            self.weight -= lr * grads
        print('权重为：', self.weight)
        plt.figure(figsize=(7.5, 7.5))
        plt.scatter(X, y, label='data', s=100, c='orange')
        new_x = np.arange(np.min(X) - 1, np.max(X) + 1, 0.1)
        new_y = np.zeros_like(new_x)
        for i in range(self.n):
            new_y += self.weight[i] * (new_x ** i)
        plt.plot(new_x, new_y, label='func')
        plt.legend()
        plt.show()

X = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 5, 10, 17])
A = polyfit(2)
A.fit(X, y)