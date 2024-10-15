# misc functions

def make_same_size(list1, list2, pad_with=0):
    """while maintaining the length of list1, ensure that list2 is the same size as list1. if list2
    is shorter it pads the list with padder, if longer then it's truncated

    Args:
        list1 (list): list of length n
        list2 (list): list of length m

    Returns:
        list of the first n elements of list2 (padded if necessary)
    """

    if (len(list1) < len(list2)):
        list2 = list2[:len(list1)]
    elif (len(list1) > len(list2)):
        list2 += [pad_with]*(len(list1)-len(list2))

    return list2
