import collections
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    newTuple = ()
    newList = []
    if not L1 and not L2:
        newTuple = (None, None, None)
        return newTuple
    elif collections.Counter(L1) == collections.Counter(L2) and len(L1) == len(L2):
        my_dict = {i:L1.count(i) for i in L1}
        for key, value in my_dict.items():
            newList.append(value)
        maxValue = max(newList)
        for key, value in my_dict.items():
            if value == maxValue:
                maxKey = key
        newTuple = (maxKey, maxValue, type(maxKey))
        return newTuple
    else:
        return False
