#!usr/bin/python3
def isWinner(x, nums):
    maria = 0
    ben = 0

    for i in nums:
        arr = list(range(2, i + 1))
        count = 0
        if arr == []:
            ben += 1
            continue
        if arr == [2]:
            maria += 1
            continue

        for j in range(len(arr)):
            if arr[j] == 2:
                count += 1
                continue
            for el in arr[0:j + 1]:
                if arr[j] == el:
                    count += 1
                    break
                if arr[j] % el == 0:
                    break

        if count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    else:
        return "Maria"
