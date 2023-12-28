# Возьмем массив интов и какое-то число k.
# Можем ли мы разбить этот массив на k подмножеств (не пустых) с равными суммами.

def findNext(array, div, sub_sum):
    diff = div - sub_sum
    filtered = list(filter(lambda n: n <= diff, array))

    if len(filtered) == 0:
        return None

    return max(filtered)


arr = list(map(int, input().split(" ")))
k = int(input())

arr.sort()
arr_sum = sum(arr)
div = arr_sum / k

arr_max = arr[len(arr) - 1]

if div != int(div) or arr_max > div:
    print("не можем")
    exit()

subset = list()
for i in range(k):
    subset.append(0)


while len(arr) != 0:
    for i in range(3):
        if subset[i] == div:
            continue

        next_num = findNext(arr, div, subset[i])

        if next_num == None:
            print("Не можем")
            exit()

        subset[i] += next_num
        arr.remove(next_num)

print("Можем")