"""
Published on Friday, 2nd November 2001, 06:00 pm; Solved by 589915; Difficulty rating: 5%

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

# prime: a number is classified as prime when is an integer that only can be divided by itself and 1
# factor: a number that divides another without decimals

Q = 600_851_475_143
# Q = 13_195

known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def next_prime(primes: list[int]):
    candidate = primes[-1] + 1
    while True:
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            return candidate
        candidate += 1

def largest_prime_factor(n: int):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

def main():
    print(largest_prime_factor(Q))

if __name__ == '__main__':
    main()