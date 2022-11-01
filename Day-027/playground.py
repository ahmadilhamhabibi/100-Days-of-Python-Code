def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5, 5, 6, 7, 9))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(5, add=5, multiply=3)