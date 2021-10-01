from random import randint

def guess():
    target = randint(0,100)
    while True:
        num = int(input('guess a number between 0 100:\n'))
        if num == target:
            print('you guess right number {}'.format(target))
            return
        elif num < target:
            print(f'{num} is smaller than target\n')
        elif num > target:
            print(f'{num} is larger than target\n')
        else:
            continue


guess()