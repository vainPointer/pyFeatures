# iteration: the for keyword in python is more like foreach in other language
array = [1, 2, 3, 4, 5]

for i, e in enumerate(array):
    print("The %i-th element is %i" % (i, e))


# 无限递归
a, b = {}, {}
a['b'] = b
b['a'] = a

a, b = [], []
a.append(b)
b.append(a)
