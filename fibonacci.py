#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    from sys import argv
    num = None
    if len(argv) >= 2 and (argv[1] == '-n' or argv[1] == '--num'):
        try:
            num = int(argv[2])
        except ValueError:
            pass
    if num == None:
        while True:
            try:
                num = int(input("How many digits in the fibonacci sequence should I get?\n ==> "))
                break
            except ValueError:
                pass
    try:
        print((getFibonacci(num)))
    except RecursionError:
        print("Sorry; I can't find *that* many numbers in the fibonacci sequence")


def getFibonacci(num, seq = [1, 1]):
    if num < 2:
        return [1]
    if num == 2:
        return [1, 1]
    if len(seq) == num:
        return seq
    seq.append(seq[-2] + seq[-1])
    return getFibonacci(num, seq)


if __name__ == '__main__':
    main()
