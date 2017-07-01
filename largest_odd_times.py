def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """

    newList = []
    my_dict = {i:L.count(i) for i in L}
    for key, value in my_dict.items():
        if value%2 != 0:
            newList.append(key)
        if not newList:
            return None
    return max(newList)
