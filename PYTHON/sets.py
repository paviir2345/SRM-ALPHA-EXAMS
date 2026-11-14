my_set = {"apple", "banana", "cherry"}
print(my_set)

my_set = {"apple", "banana", "cherry"}
print(my_set)

# Using list
my_set_2 = set(["one", "two", "three"])

# Using tuple
my_set_2 = set(("one", "two", "three"))
print(my_set_2)


my_set_3 = set("aaabbbcccdddeeeeeffff")
print(my_set_3)


my_set = set()

my_set.add(42)
my_set.add(True)
my_set.add("Hello")

print(my_set)


my_set.add(42)
print(my_set)


my_set = {"apple", "banana", "cherry"}

my_set.remove("apple")
print(my_set)

my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)

my_set.clear()
print(my_set)