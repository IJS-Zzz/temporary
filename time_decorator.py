import functools
import time


def timeit(func):
    """
    Decorator that counts the execution time of a decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = ["{}={}".format(k, repr(v)) for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        # func work
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = round((time.time() - start_time) * 1000, 6)

        print("run {func_name}({func_params}) took {time} ms.".format(
            func_name=func.__name__,
            func_params=signature,
            time=total_time
        ))
        return result
    return wrapper

