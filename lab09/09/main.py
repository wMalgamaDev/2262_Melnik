n = 5
tblmul = [[j*i for j in range(1, n+1)] for i in range(1, n+1)]
print(*tblmul,sep='\n')