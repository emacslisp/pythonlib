def hello():
    return "xxxxx"

def other(some_def_func):
    print(some_def_func())


def new_decorator(original_func):
    def wrap_func():
        print("some extra code, before")
        original_func()
        print("some extra code, after")
    
    return wrap_func
@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

wrap_func = new_decorator(func_needs_decorator)

wrap_func()
other(hello)


func_needs_decorator()