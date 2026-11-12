def missing_numbers(arr):
    n = len(arr)

    for i in range(n):
        index = abs(arr[i]) - 1

        if arr[index] > 0:
            arr[index] = -arr[index]

    missing = []

    for i in range(n):
        if arr[i] > 0:
            missing.append(i + 1)

    return missing


arr = [4, 3, 2, 7, 8, 2, 3, 1]

answer = missing_numbers(arr)

if len(answer) == 0:
    print("None")
else:
    for i in range(len(answer)):
        print(answer[i], end=" ")