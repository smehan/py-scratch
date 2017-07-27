from functools import wraps


def cache(func):
    """
    Will cache previous computes in a pure function. Use as a decorator on such a pure function.
    :param func:
    :return:
    """
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc
