def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

int_mx = toint(max)

print(int_mx(True, 2, "3"))