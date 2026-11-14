import os
from multiprocessing import Process


def squarnumber(num):
    for i in num:
        print("Square of", i, "is", i * i)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count() or 1
    print("Number of processes:", num_processes)

    for i in range(num_processes):
        p = Process(target=squarnumber, args=([i],))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("end of main process")