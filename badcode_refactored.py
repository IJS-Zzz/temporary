import collections


def is_funny_function(data):
    """
    Sorted array check function.

    Params:
        data: list[int]
    Return: bool

    Return True in the following situations:
        - all items is equals
        - items is growing or decreasing by 1

    Raised ValueError if the data is empty.
    """
    if not data:
        raise ValueError("data is None")

    if len(data) == 1:
        return True

    # check that all items is equal
    counter = {}
    for v in data:
        counter[v] = counter.get(v, 0) + 1
        if len(counter) > 1:
            break
    else:
        return True

    # check that the array is growing or decreasing by 1
    to_up = True
    to_low = True
    for i in range(1, len(data)):
        pre = int(data[i-1])
        now = int(data[i])

        # validate growing
        if to_up and now != pre + 1:
            to_up = False

        # validate decreasing
        if to_low and now != pre - 1:
            to_low = False

        if not to_up and not to_low:
            return False

    return True

