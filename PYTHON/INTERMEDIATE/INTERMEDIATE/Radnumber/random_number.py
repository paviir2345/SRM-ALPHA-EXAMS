import random
random.seed(1)
print(random.random())
a=random.random()
print(a)

b=random.uniform(1,10)
print(b)

c=random.randint(1,100)
print(c)
d=random.normalvariate(0,1)
print(d)

mylist=list("QWERTYUIOPASDFGHJKLZXCVBNM")
e=random.choice(mylist)
print(e)

f=random.sample(mylist,5)
print(f)

g=random.choices(mylist,k=3)
print(g)

h=random.shuffle(mylist)
print(mylist)
print(random.getstate())
print(random.random())