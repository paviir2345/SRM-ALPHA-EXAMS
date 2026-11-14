my_tuple = ("max" , 28,"newyork")
print(my_tuple)

if "max" in my_tuple:
    print("yes")
else:
    print("no")

tuple_4 = tuple([1,2,3,4])
print(tuple_4)

my_tuple = ('a','p','p','l','e')
print(len(my_tuple))

print(my_tuple.index("e"))
print(my_tuple.count("p"))

my_list = ["a", "b", "c", "d"]

list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

a=(1,2,3,4,5,6,7)
b = a[2:5]
print(b)

tuple_1 = ("Max", 28, "New York")

name, age, city = tuple_1

print(name)
print(age)
print(city)

my_tuple = (0,1,2,3,4,5,6)
i1,*i2,i3 = my_tuple
print(i1)
print(i2)
print(i3)