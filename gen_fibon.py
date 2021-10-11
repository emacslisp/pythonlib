def gen_fibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a+b

def simple_gen():
    for x in range(3):
        yield x

for number in gen_fibon(10):
    print(number)

print("## simple gen")

print(next(simple_gen()))
print(next(simple_gen()))
print(next(simple_gen()))


print("## string iter")

s = "Hello"
s_iter = iter(s)

print(next(s_iter))