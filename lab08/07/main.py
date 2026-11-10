nums = list(map(int, input().split()))

for x in nums:
    if x < 0:
        print("найдено отрицательное:", x)
        break
else:
    print("все числа неотрицательные")