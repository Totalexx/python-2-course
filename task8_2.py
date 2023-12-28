# Возьмем массив интов. Найти подмассив с максимальной суммой, вернуть её.

import sys

arr = list(map(int, input().split(" ")))

max_sum = -sys.maxsize - 1
start = 0
end = 0

arr_max = max(arr)
if arr_max < 0:
    print(arr_max)
    exit()

for i in range(len(arr)):
    sub_sum = sum(arr[start:i+1])

    if sub_sum > max_sum:
        max_sum = sub_sum
        end = i + 1

    if sub_sum < 0:
        start = i + 1

print(arr[start:end])
print(max_sum)