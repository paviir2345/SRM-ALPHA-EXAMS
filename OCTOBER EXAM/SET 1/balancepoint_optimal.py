def balance_point(arr):
    total = 0

    for i in range(len(arr)):
        total = total + arr[i]

    left_sum = 0

    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum = left_sum + arr[i]

    return -1


arr = [3, -2, 5, 4, 1, 5]

print(balance_point(arr))