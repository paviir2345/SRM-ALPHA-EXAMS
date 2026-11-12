def second_highest(arr):
    highest = arr[0]

    for i in range(len(arr)):
        if arr[i] > highest:
            highest = arr[i]

    second = None

    for i in range(len(arr)):
        if arr[i] != highest:
            if second == None or arr[i] > second:
                second = arr[i]

    return second


arr = [31, 28, 35, 35, 29, -4, 35, 28, 30]

print(second_highest(arr))