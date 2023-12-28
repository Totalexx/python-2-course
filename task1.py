# 1) В мобильное приложение, которое разрабатывает Николай,
# встроен автоматический детектор сбоев. Когда в приложении возникает ошибка

def hasErrorInInterval(errors, interval):
    border = False
    isError = True
    lastErrors = errors[interval[0] - 1]

    for i in range(interval[0], interval[1]):
        nowErrors = errors[i]
        if not border:
            if lastErrors <= nowErrors:
                lastErrors = nowErrors
                continue
            else:
                border = True
                lastErrors = nowErrors
                continue
        else:
            if lastErrors >= nowErrors:
                lastErrors = nowErrors
                continue
            else:
                isError = False
                break


    if isError:
        print("Yes")
    else:
        print("No")


errorListLength = int(input())
errors = []

for i in input().split():
    errors.append(int(i))

periodLength = int(input())

period = []

for i in range(periodLength):
    periodStr = input().split()
    period.append((int(periodStr[0]), int(periodStr[1])))

for i in range(periodLength):
    hasErrorInInterval(errors, period[i])