from collections import *
import json

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)


# defaultdict: 与 dict 相比，不需要检查 key 是否存在
favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)


tree = lambda: defaultdict(tree)   # 嵌套结构
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
print(json.dumps(some_dict))


# counter: 计数容器
favs = Counter(name for name, colour in colours)

'''
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)
'''


# deque: 双向列表
d = deque([1, 2, 3, 4, 5])
d.extendleft([0])
d.extend([6, 7, 8])
d.popleft()
d.pop()


# namedtuple: 可以像字典一样访问，但是不可变