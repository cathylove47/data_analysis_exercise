import numpy as np

#定义原函数
def f(x):
    if x == 0:
        f=0
    else:
        f = x
    return  f

#复合梯形求积
def c_t_formula(a,b,n):
    h = (b - a) / n
    sum = 0
    for i in range(n - 1):
        xk = a + h * (i + 1)
        sum = sum + f(xk)
    t = h / 2 * (f(a) + 2 * sum + f(b))
    return t

#复合辛普森求积
def c_s_formula(a,b,n):
    h=(b-a)/n
    sum=0
    for k in range(n-1):
        xk=a+h*(k+1)
        xk_half=xk+h/2
        sum = sum + 4*f(xk_half)+2*f(xk)
    t = h/6*(f(a)+sum+f(b))
    return t

#龙贝格求积
def lomberg_algorithm(a,b,n):
    t=np.zeros((n,n))
    t[0][0]=c_s_formula(a,b,1)
    for i in range(1,n):
        for j in range(i+1):
            #计算T0
            if j == 0:
                t[i][j] = c_s_formula(a,b,2**i)
            #计算Ti[j]
            else:
                t[i][j] = 4**j*t[i][j-1]/(4**j-1)-t[i-1][j-1]/(4**j-1)
                #print(t[i][j])
    return t[n-1][n-1]

if __name__ == '__main__':
    true_value = 0.5
    a = float(input("区间起点:\n"))
    b = float(input("区间终点:\n"))
    n = int(input("计算步数:\n"))
    nl = int(np.log(n)/np.log(2)) + 1 #龙贝格求积时间复杂度为O(2**n)为保证和上面俩复杂度相同（运算步数相同），取对数
    result_1 = c_t_formula(a,b,n)
    result_2 = c_s_formula(a,b,n)
    result_3 = lomberg_algorithm(a,b,nl+1)
    print("result:")
    print("复合梯形:{}".format(result_1))
    print("复合辛普森:{}".format(result_2))
    print("龙贝格:{}".format(result_3))
    print(' ')
    print("误差绝对值")
    print("复合梯形:{}".format(result_1-true_value))
    print("复合辛普森:{}".format(result_2-true_value))
    print("龙贝格:{}".format(result_3-true_value))


