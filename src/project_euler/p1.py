"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import timeit


def sum_multiples_looping(end):
    r = 0
    for n in range(end):
        if n % 3 == 0 or n % 5 == 0:
            r += n
    return r


def sum_multiples_creating_list(end):
    return sum({*range(0, end, 5), *range(0, end, 3)})


def main():

    def listing():
        return sum_multiples_creating_list(1000)

    def looping():
        return sum_multiples_looping(1000)

    t1 = timeit.timeit(listing, number=10000)
    t2 = timeit.timeit(looping, number=10000)

    print(f"listing: {t1:.6f} seconds")
    print(f"looping: {t2:.6f} seconds")


if __name__ == '__main__':
    main()
