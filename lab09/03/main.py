lst = list(range(6000, 7000))
ans = max(lst, key=lambda n: bin(n).count("1"))
print(ans)
