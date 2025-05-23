"""
Published on Friday, 19th October 2001, 06:00 pm; Solved by 818833;

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

limit = 4_000_000

def main():
    result = 0
    prev = 1
    current = 2
    while current <= limit:
        if current % 2 == 0:
            result += current
        prev, current = current, prev + current
    print(result)

if __name__ == '__main__':
    main()