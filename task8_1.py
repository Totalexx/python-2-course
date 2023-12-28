# Возьмем массив интов. Найти подмассив с максимальной суммой, вернуть её.
import sys

arr = list(map(int, input().split(" ")))

max_sum = -sys.maxsize - 1
start = 0
end = 0

for i in range(len(arr)):
    for j in range(len(arr) - i):
        sub = arr[j:j+i]
        sub_sum = sum(sub)

        if sub_sum > max_sum:
            max_sum = sub_sum
            start = j
            end = j + i

print(arr[start:end])
print(max_sum)