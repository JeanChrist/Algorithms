"""
>>> is_prime(2)
True

>>> is_prime(5)
True

>>> is_prime(13)
True

>>> is_prime(15)
False

>>> res = _prime_generator()
>>> [next(res) for i in range(10)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

>>> get_nth_prime(1)
2

>>> get_nth_prime(2)
3

>>> get_nth_prime(10)
29

"""

from math import sqrt


def is_prime(num):
    assert isinstance(num, int), f'{num} is not a integer!'

    if num < 2:  # Need >= 2
        return False
    if num == 2 or num == 3:
        return True

    if num % 6 != 1 and num % 6 != 5:
        return False

    for i in range(5, int(sqrt(num)) + 1, 6):
        if num % i == 0 or num % i+2 == 0:
            return False

    return True


def _prime_generator(start=None):
    if start is not None:
        i = start
    else:
        i = 0

    while True:
        if is_prime(i):
            yield i

        i += 1


def get_nth_prime(n):
    assert n >= 1
    res = _prime_generator()
    for i in range(1, n):

        next(res)
        # print(f'{i}: {next(res)}')
    return next(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # 5209523: 37521133
    # 5209524: 37521137
    # 5209525: 37521139
    # 5209526: 37521161
    # 5209526: 37521163
