#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    from sys import stdout
    print("press CTRL+C to stop")
    print()
    print("PRIMES")
    print("~~~~~~")

    print("2, 3", end=", ")
    stdout.flush() # flush because no newline
    count = 5 # starting prime number (we already know 2 is prime)
    while True:
        isPrime = True
        for i in range(2, int(count / 2)):
            if count % i == 0:
                isPrime = False
        if isPrime:
            print(count, end=", ")
            stdout.flush() # flush because no newline
        count += 1


if __name__ == '__main__':
    main()

