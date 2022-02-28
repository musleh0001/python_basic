from functools import wraps

# def decorator_function(msg):
#     def wrapper_function():
#         print(msg)

#     return wrapper_function


# hi_func = decorator_function("Hi")
# bye_func = decorator_function("Bye")

# hi_func()
# bye_func()

# Example
def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename="{}.log".format(orig_func.__name__), level=logging.INFO
    )

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = orig_func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{orig_func.__name__} ran in: {end - start:.4f} sec")

    return wrapper


# lession
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_function
def display():
    print("display function ran")


@my_logger
@my_timer
def display_info(name, age):
    print(f"display_info run with arguments ({name}, {age})")


# display = decorator_function(display)
# display()
display_info("Khan", 23)
