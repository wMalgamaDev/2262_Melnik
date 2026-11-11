def sublist(lst, *nums):
	l = []
	for id in nums:
		l.append(lst[id])

	print(l)
lst = [ 'Anna', 'Barbara', 'Clara', 'Diana', 'Eva', 'Flora']
sublist(lst)
sublist(lst, 0, 2, 5)
sublist(lst, 0, 1, 2, 3, 4, 5)
