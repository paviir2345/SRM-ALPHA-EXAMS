def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')

    return wrapper

def print_name():
    print('Alex')

print_name()

print()

print_name = start_end_decorator(print_name)
print_name()


@start_end_decorator
def print_name():
    print('Alex')

print_name()


def start_end_decorator_2(func):

    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')

    return wrapper

@start_end_decorator_2
def add_5(x):
    return x + 5

result = add_5(10)
print(result)


def start_end_decorator_3(func):

    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result

    return wrapper

@start_end_decorator_3
def add_5(x):
    return x + 5

result = add_5(10)
print(result) #return values 