def missing_numbers(arr):
    n = len(arr)
    missing = []

    for i in range(1, n + 1):
        found = False

        for j in range(n):
            if arr[j] == i:
                found = True
                break

        if found == False:
            missing.append(i)

    return missing


arr = [4, 3, 2, 7, 8, 2, 3, 1]

answer = missing_numbers(arr)

if len(answer) == 0:
    print("None")
else:
    for i in range(len(answer)):
        print(answer[i], end=" ")