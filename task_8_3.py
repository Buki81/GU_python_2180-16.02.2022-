from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        return callback.__name__,(*args, type(callback(*args, **kwargs)))
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(*a)
