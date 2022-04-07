from functools import wraps


def val_checker(callback):
    def checker(cube):
        @wraps(cube)
        def wrapper(*args):
            for arg in args:
                if not callback(arg):
                    raise ValueError(f'Неверный аргумент: {arg}')
            return cube(*args)

        return wrapper

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)

a = calc_cube(-5)
print(a)
