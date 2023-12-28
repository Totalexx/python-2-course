# 2Л) Самостоятельно реализовать перевод из в строки в int. Без int().
import math

def to_int(num):

    zero_ascii = ord("0")
    nine_ascii = ord("9")

    number = 0
    digit = len(num) - 1

    for i in range(len(num)):
        current_number = ord(num[i]) - zero_ascii
        if current_number < 0 or current_number > nine_ascii:
            return float("nan")
        number = number + current_number * math.pow(10, digit)
        digit -= 1

    return number


print(to_int("123"))
print(to_int("1332"))
print(to_int("123/11"))
