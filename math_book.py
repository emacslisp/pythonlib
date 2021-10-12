import math

print(math.e)

from math import pi
print(pi)

print(round(4.35))

print(math.log(math.e))

print(math.log(100, 10))

print(math.sin(pi/2))

import random
print(random.randint(0, 100))

print(random.seed(101))
print(random.randint(0, 100))

mylist = list(range(0, 20))
print(random.choice(mylist))
print(random.choice(mylist))
print(random.choices(population=mylist, k=10))
print(random.sample(population=mylist, k=10))

random.shuffle(mylist)
print(mylist)

print(random.uniform(a=0, b=100))

print(random.gauss(mu=0,sigma=1))
