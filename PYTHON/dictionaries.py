mydict = {"name": "max" , "age" : "28" , "city":"new york"}
print(mydict)

value = mydict["name"]
print(value)

mydict["email"] = "xyz@gmail.com"
print(mydict)


del mydict["email"]
print(mydict)

if "name" in mydict:
    print(mydict["name"])

for key in mydict:
    print(key)

for key,value in mydict.items():
    print(key,value)


dict_org = {"name": "Max", "age": 28, "city": "New York"}

dict_copy = dict_org

dict_copy["name"] = "Lisa"

print(dict_copy)
print(dict_org)

my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}

my_dict_2 = dict(name="Lisa", age=27, city="Boston")

my_dict.update(my_dict_2)

print(my_dict)