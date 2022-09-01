def doubler(number):
    """Doubles the number passed to it"""
    return number * 2

def info(func):
    def wrapper(*args):
        print(f'Function name: {func.__name__}')
        print(f'Function docstring: {str(func.__doc__)}')
        return func(*args)

    return wrapper 

my_decorator = info(doubler)
print(my_decorator(2))
