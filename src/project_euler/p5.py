"""
Published on Friday, 30th November 2001, 06:00 pm; Solved by 523771; Difficulty rating: 5%

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible, divisible with no remainder, by all of the numbers from 1 to 20?
"""


def is_divisible_from_to(n, start, end):
    for divisor in range(end, start, -1):
        if n % divisor != 0:
            return False
    return True


def find_smallest_number_divisible(a: int, b: int) -> int:
    found = None
    n = b
    while not found:
        if not is_divisible_from_to(n, a, b):
            n += b
            continue
        found = n
    return found


def main():
    print(find_smallest_number_divisible(1, 19))


if __name__ == '__main__':
    main()
