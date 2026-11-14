from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import deque
a="banana"
my_counter=Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

#namedtuple
Point=namedtuple('Point','x,y,z')
p=Point(1,2,3)
print(p)
print(p.x)
print(p.y)
print(p.z)

#orderedDict
ordered_dict=OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

#defaultdict
default_dict=defaultdict(int)
default_dict['a'] += 1
default_dict['b'] += 2
default_dict['c'] += 3
print(default_dict)

#deque
d=deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft(0)
print(d)
d.pop()
print(d)    
d.appendleft(3)
print(d)
d.popleft()
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
d.extend([4,5,6])
print(d)
d.extendleft([-1,-2,-3])
print(d)