"""
Published on Friday, 16th November 2001, 06:00 pm; Solved by 521199; Difficulty rating: 5%

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

r = list(reversed(range(100, 1000)))


def is_palindromic(n: int):
    return f'{n}' == f'{n}'[::-1]


def main():
    found = 0
    for i, a in enumerate(r):
        for b in r[i:]:
            product = a * b
            if is_palindromic(product) and product > found:
                print(f'{product} = {a} * {b}')
                found = product
    print(found)


if __name__ == '__main__':
    main()
