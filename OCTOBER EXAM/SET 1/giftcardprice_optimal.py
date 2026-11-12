def giftcardpairing(prices, target):

    seen = {}

    for i in range(len(prices)):
        needed = target - prices[i]

        if needed in seen:
            return seen[needed], i

        seen[prices[i]] = i


prices = [120, 45, 80, 200, 35, 150]
target = 235

answer = giftcardpairing(prices, target)
print(answer[0], answer[1])