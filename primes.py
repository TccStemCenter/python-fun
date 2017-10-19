#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    from sys import stdout
    print("press CTRL+C to stop")
    print()
    print("PRIMES")
    print("~~~~~~")

    primes = [2]
    print(2, end=", ")
    stdout.flush() # flush because no newline
    count = 3 # starting prime number (we already know 2 is prime)
    while True:
        isPrime = True
        for prime in primes:
            if count % prime == 0:
                isPrime = False
        if isPrime:
            primes.append(count)
            print(count, end=", ")
            stdout.flush() # flush because no newline
        count += 1


if __name__ == '__main__':
    main()
