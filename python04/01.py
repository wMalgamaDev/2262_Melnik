import math

flag = int(input())
cntr = 0
i = 2

while True:
    for j in range(2, int(math.sqrt(i))+1):
        if(i % j == 0):
            break
    else:
        cntr += 1

    if flag == cntr:
        print(i)
        break
    i += 1

