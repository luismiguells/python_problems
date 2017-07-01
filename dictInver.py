import bisect
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    result = {}

    for k, v in d.items():
        bisect.insort(result.setdefault(v, []), k)

    return result
