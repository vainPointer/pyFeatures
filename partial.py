from functools import partial
# 偏函数：用于改变函数默认的参数值


# int2 = partial(int, base=2)
def int2(x, base=2):
    return int(x, base)


max2 = partial(max, 10)
