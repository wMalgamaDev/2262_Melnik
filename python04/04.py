con = '1234567890qwertyuiopasdfghjklzxcvbnm'
f1 = False
f2 = False
f3 = False
f4 = False
n = int(input())
l = [input() for _ in range(n)]
for s in l:
    for i in con:
        if i in s:
            if not(f1) and i in con[:10]:
                f1 = True
            elif not(f2) and i in con[10:20]:
                f2 = True
            elif not(f3) and i in con[20:29]:
                f3 = True
            elif not(f4) and i in con[29:36]:
                f4 = True
        if f1 and f2 and f3 and f4:
            print('strong')
            break
    else:
        print('weak')
    f1 = f2 = f3 = f4 = 0

# print(con[:10], con[10:20], con[20:29], con[29:36])
