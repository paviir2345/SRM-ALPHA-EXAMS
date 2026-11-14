from threading import Thread
import os

def squarnumber(num):
    for i in num:
        print("Square of", i, "is", i * i)
threads = []
num_threads = 10
for i in range(num_threads):
    t = Thread(target=squarnumber, args=([i],))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()    

print("end of main thread")
