def every_other(seq):
    i = 0
    for n in seq:
        if i % 2 == 0:
            yield n
        i += 1
print(*every_other([10, 20, 30, 40, 50]))
print(*every_other(range(10)))
print(*every_other(iter(range(10))))
print(sum(every_other(map(int, input().split()))))
