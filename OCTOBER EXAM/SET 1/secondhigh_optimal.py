def second_highest(arr):
    highest = None
    second = None

    for i in range(len(arr)):
        if highest == None or arr[i] > highest:
            second = highest
            highest = arr[i]

        elif arr[i] != highest:
            if second == None or arr[i] > second:
                second = arr[i]

    return second


arr = [31, 28, 35, 35, 29, -4, 35, 28, 30]

print(second_highest(arr))