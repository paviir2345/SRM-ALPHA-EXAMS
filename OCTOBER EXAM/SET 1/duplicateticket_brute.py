def first_duplicate(tickets):

    for i in range(len(tickets)):

        for j in range(i):

            if tickets[i] == tickets[j]:
                return tickets[i]

    return -1


tickets = [4021, 3377, 5120, 3377, 4021, 9001, 5120, 7]

print(first_duplicate(tickets))