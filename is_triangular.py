def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    "To tell whether it's a triangular number"
    aux = 0
    count = 1
    while aux < k:
        aux = aux + count
        count += 1
        if aux == k:
            return True
        elif aux > k:
            return False
