lst = ['hello', 'hell', 'bye', 'world', 'bybye']
lst.sort(key= lambda n: (len(n), n))
print (lst)
