def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper
@start_end_decorator
def print_name():
    print('Alex')

print_name()

import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5


        