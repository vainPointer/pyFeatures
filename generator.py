# 类似于 SICP 中流的概念
# yield next
L = [x*x for x in range(10)]
G = (x*x for x in range(10))


def fib():
    a, b = 0, 1
    while 1:
        yield(b)
        a, b = b, a + b

f = fib()
for i in range(10):
    print(f.__next__())

my_string = "cnstrong"
my_string = iter(my_string)
while True:
    i = next(my_string)
    if i:
        print(i)
    else:
        break
