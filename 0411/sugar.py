N = int(input())

result = 0

five_killo = N // 5
five_extra = N % 5

if five_extra != 0:
    five_killo = five_killo - 1
    five_extra = five_extra + 5
    three_killo = five_extra // 3
    if three_killo != 0:
        result = -1
    else:
        result = five_killo + three_killo
else:
    three_killo = five_extra // 3
    result = five_killo + three_killo

print(result)