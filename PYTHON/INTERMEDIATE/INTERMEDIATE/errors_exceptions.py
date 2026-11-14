try:
    a = 5 / 1
    b = a + '10'

except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)

except TypeError as e:
    print('A TypeError occured:', e)



try:
    a = 5 / 1

except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)

else:
    print('Everything is ok')