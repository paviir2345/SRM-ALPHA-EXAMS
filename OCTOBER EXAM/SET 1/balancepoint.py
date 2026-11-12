def balance_point(arr):
    n = len(arr)

    for i in range(n):
        left_sum = 0
        right_sum = 0

        for j in range(i):
            left_sum = left_sum + arr[j]

        for j in range(i + 1, n):
            right_sum = right_sum + arr[j]

        if left_sum == right_sum:
            return i

    return -1


arr = [3, -2, 5, 4, 1, 5]

print(balance_point(arr))