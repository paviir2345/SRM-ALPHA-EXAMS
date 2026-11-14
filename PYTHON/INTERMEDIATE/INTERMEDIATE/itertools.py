from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))



from itertools import permutations

perm = permutations([1, 2, 3])
print(list(perm))


perm = permutations([1, 2, 3], 2)
print(list(perm))



from itertools import groupby

def smaller_than_3(x):
    return x < 3

group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)

for key, group in group_obj:
    print(key, list(group))


group_obj = groupby(
    ["hi", "nice", "hello", "cool"],
    key=lambda x: "i" in x
)

for key, group in group_obj:
    print(key, list(group))


persons = [
    {'name': 'Tim', 'age': 25},
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27},
    {'name': 'Claire', 'age': 28}
]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))