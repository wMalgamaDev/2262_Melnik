r = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

trump = input()
n = int(input())

lst = []
for i in range(n):
    r1, s1 = input().split()
    r2, s2 = input().split()
    if (r.index(r1) < r.index(r2) and s1 == s2) or (s2 == trump and s1 != trump):
        lst.append(1)
    else:
        lst.append(0)
print(*lst)