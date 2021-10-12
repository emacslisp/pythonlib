from collections import Counter
from collections import defaultdict
from collections import namedtuple


mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3,3]

print(Counter(mylist))

print(Counter('aaaaaaaaaaaabbbbbbbbbcccccccccc'))

d = {'a': 10}
d = defaultdict(lambda: 0)
print(d['adsf'])


Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='sam')
type(sammy)

print(sammy)