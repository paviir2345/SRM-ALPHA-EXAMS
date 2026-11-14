f = lambda x: x + 10

print(f(5))
print(f(100))

f = lambda x, y: x * y

print(f(2, 10))
print(f(7, 5))

#func inside a func
def myfunc(n):
    return lambda x: x * n

doubler = myfunc(2)
print(doubler(6))

tripler = myfunc(3)
print(tripler(6))