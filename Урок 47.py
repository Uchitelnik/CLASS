def frf(num):
    num = list(num)
    min1 = min(num)
    max1 = max(num)

    for num1 in num :
        if num1 ==  min1:
            num.remove(num1)
        elif num1 == max1:
            num.remove(num1)

    num = tuple(num)

    return num
num = (1, 4, 7, 2, 5,3, 62 ,65)

print(frf(num))

