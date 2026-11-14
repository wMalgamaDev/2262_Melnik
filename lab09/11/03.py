def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

def mult(*n):
    r = 1
    for i in n:
        r *= i
    return r

int_mult = toint(mult)
print(int_mult(True, "500", 2))