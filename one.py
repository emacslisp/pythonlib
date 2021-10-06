def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print('ONE.py is being run directly!')
else:
    print('ONE.py has been imported!')