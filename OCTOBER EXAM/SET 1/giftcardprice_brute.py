def giftcardpairing(prices, target):

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):

            if prices[i] + prices[j] == target:
                return i, j


prices = [120, 45, 80, 200, 35, 150]
target = 235

answer = giftcardpairing(prices, target)
print(answer[0], answer[1])