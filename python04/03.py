from string import ascii_lowercase
al = ascii_lowercase

word = input()
cnt = 0
lit = ''

lal = len(al)
itr = 0
ali = ''

for i in range(lal):
    ali = al[i]
    itr = word.count(ali)
    if itr > cnt:
        cnt = itr
        lit = ali

print(word.replace(lit, ''))