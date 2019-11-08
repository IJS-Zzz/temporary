import collections

def may_be_palindrome(string):
    """
    Functional check of a string, which may be a palindrome string.
    """
    if not isinstance(string, str):
        raise TypeError("checked value must be a string")

    counter = collections.defaultdict(int)
    for c in string:
        counter[c] += 1

    balance = 0
    for k, v in counter.items():
        balance += v % 2
        if balance > 1:
            return False
    return True

