mylist = ["apple","banana","cherry"]
print(mylist)


for i in mylist:
    print(i)

mylist.append("lemon")       
print(mylist)

mylist.insert(1,"blueberry")
print(mylist)

item = mylist.pop()
print(mylist)

item = mylist.remove("cherry")
print(mylist)

item =mylist.clear()
print(mylist)

list_1 = [2,4,5,6,7]
list_2 = [3,6,2,1,4]
print(list_1 + list_2)

list_1 = [1,2,3,4,5,6,7,8,9]
a = list_1[1::2]
print(a)

list_org = ["banana" , "cherry" "apple"]
list_cpy = list_org

print(list_cpy)