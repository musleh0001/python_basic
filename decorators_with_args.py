from functools import wraps


def prefix_decorator(prefix):
    def decorator_function(original_function):
        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            print(f"{prefix} Executed Before {original_function.__name__}")
            result = original_function(*args, **kwargs)
            print(f"{prefix} Executed After {original_function.__name__} \n")
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator("LOG: ")
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display_info("John", 25)
display_info("Travis", 30)
