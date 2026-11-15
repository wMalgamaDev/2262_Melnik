n = int(input())
dress = list(map(int, input().split()))
flag = [0, 0, 0]
cnt = 0
for d in dress:
    if sum(flag) == 3:
        print(cnt)
        break
    if flag[d-1] != 1:
        flag[d-1] =1
    cnt += 1
else:
    print(cnt)