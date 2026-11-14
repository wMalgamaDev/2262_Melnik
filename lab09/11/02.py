def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

def div(x, y):
    return x/y

int_div = toint(div)

print(int_div(True, "2"))