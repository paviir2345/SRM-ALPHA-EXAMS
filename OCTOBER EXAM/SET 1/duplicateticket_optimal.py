def first_duplicate(tickets):
    seen = []

    for i in range(len(tickets)):

        if tickets[i] in seen:
            return tickets[i]

        seen.append(tickets[i])

    return -1


tickets = [4021, 3377, 5120, 3377, 4021, 9001, 5120, 7]

print(first_duplicate(tickets))