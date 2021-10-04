x = 50

def func():
    global x
    print(f'X is {x}');

    x = 'NEW VALUE'
    print(f'X has new value {x}')

func()
print(x)
