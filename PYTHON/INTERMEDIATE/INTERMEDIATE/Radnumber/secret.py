import secrets
import numpy as np
print(secrets.randbelow(10))
print(secrets.randbits(7))
print(secrets.token_bytes(16))
mylist=list("QWERTYUIOPASDFGHJKLZXCVBNM")
print(secrets.choice(mylist))
np.random.seed(1)
print(np.random.randint(3,10,(3,5)))

arr=np.random.randint(1,100,(3,5))
print(arr)
print("After shuffling:")
np.random.shuffle(arr)
print(arr)

print("After resetting the seed:")
np.random.seed(1)
print(np.random.randint(3,10,(3,5)))