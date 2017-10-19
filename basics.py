#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    # comments
    # ~~~~~~~~
    # comments start with '#'
    # but! first two comments have special meaning

    # variables
    # ~~~~~~~~~
    # ==> left: name; right: value
    # number: int,float
    i = 1       # int: name=i, value=0
    f = 3.1415  # float: name=f, value=3.1415 (approx. pi)
    # string: sequence of characters
    # NOTE: double-quotes ("") are EXACTLY THE SAME as single-quotes ('')
    # NOTE: escape double-quotes inside double quotes and escape single-quotes
    #       inside single-quotes, otherwise you will run into trouble; to escape
    #       a quote, put a backslash before it.
    #       (eg, "\"an unexamined life is not worth living\" - Socrates")
    #       You do NOT have to esacpe a " inside '' .. nor do you have to escape
    #       a ' inside ""
    s = "hello world" # string: name=s, value="hello world"

    # stdout: print strings to "standard output" or stdout
    print("\nVARIABLES\n~~~~~~~~~")
    # prints variable(s) to stdout (useful for debugging and sometimes user input)
    print(s)
    print(i, f)

    print("\nSTRING CONCATENATION\n~~~~~~~~~~~~~~~~~~~~")
    # string concatenation
    # ~~~~~~~~~~~~~~~~~~~~
    # cocatenation: + ==> adds strings together
    print(s + "; good bye world")
    # In order to concatenate something that is not a string, use str(..)
    # NOTE: str(..) converts, or casts, the result (which is a float, or
    #       floting point number) into a string. In order to concatenate
    #       something with a string, it, too, must be a string
    print("i + f yields " + str(i + f))

    print("\nTYPES\n~~~~~")
    # type(..); show what the type of the variable is
    # it's useful to know what a type is; also, note the use of .format(); this
    # NOTE: "{}".format(..) is a better way to concatenate something to a string
    print("type of i is {}\nalso, type of f is".format(type(i)))

    # more types
    # ~~~~~~~~~~
    # list: indexable array of items (can be mixed)
    l = ["this", "is", 1, "example", "of", "a", "list", s, i, f]
    # tuple: immutable list
    t = ("this", "is", "a", "tuple", s, i, f)
    # none: nothing
    n = None
    # bool: True,False
    b = True

    print("l is {} ({})".format(l, type(l)))
    print("t is {} ({})".format(t, type(t)))
    print("n is {} ({})".format(n, type(n)))
    print("b is {} ({})".format(b, type(b)))

    input("\n--PRESS ENTER TO CONTINUE--")

    # appending
    # ~~~~~~~~~
    l.append("appended item")
    print("l is now: {}".format(l))
    try:
        t.append("another appended item")
    except AttributeError:
        # because the above line throws an AttributeError, this will quietly
        # handle the error if it occurs
        # "it's better to ask for forgiveness than ask for permission"
        print("error trying to append to tuple...")

    # using lists and tuples
    # ~~~~~~~~~~~~~~~~~~~~~~
    # indexing: [#] is notation for getting object at index "#" where # is number
    # NOTE: 0 is always the first index
    print("list l ==> first item: {} .. last item: {}".format(l[0], l[-1]))
    print("tuple t ==> first item: {} .. last item: {}".format(t[0], t[-1]))
    # index: list.index(object) will get the index of first object that is
    #        equal to the object passed
    print("in list l, \"example\" is at index {}".format(l.index("example")))
    # join: converts entire list into one string where each item is delimited
    #       by the delimiter. If nothing is passed, then each item butts up
    #       against another with no delimiting string
    print("\nfunny way to show a list: {}".format("{ " + " - ".join(str(o) for o in l) + " } "))

    input("\n--PRESS ENTER TO CONTINUE--")
    print()

    # input
    # ~~~~~
    # get user input from stdin until user enters "yes" or "no"
    inp = None
    while not isinstance(inp, str) or inp.lower() not in ("yes", "no"):
        inp = input("How about we calculate pi for real? (yes,no) ")

    # conditional
    # ~~~~~~~~~~~
    # if statement checks for comparison
    if inp == "yes":
        # 'if' block is entered ONLY IF THE 'IF' EXPRESSION EVALUATES TO TRUE
        # NOTE: no other 'elif' or 'else' blocks will be entered if this
        #       block is entered because the above expression is True
        print("I'm so glad to hear! Let's get started")
    elif inp == "no":
        # 'elif' block is entered ONLY IF THE PRECEDING 'IF' (AND MAYBE OTHER
        # 'elif's) ARE FALSE AND THIS elif IS TRUE
        # NOTE: no other 'elif' or 'else' blocks will be entered if this
        #       block is entered because the above expression is True
        # NOTE: you need an 'if' before an 'elif'
        print("Fine then!")
        exit(1)
    else:
        # 'else' block is entered ONLY IF THE PRECEDING
        print("This is impossible! 'inp' can only be \"yes\" or \"no\"!")

    print()
    print("Calculating pi! Press CTRL+C to see pi approximation")
    print("(The longer you wait, the better the approximation will be.)")
    piApprox = getPi() # this will block until pi is returned (when user presses ctrl+c)
    print()
    print("pi is approx: {}".format(piApprox))

    realPiApprox = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384"
    piApprox = str(piApprox)
    for ch,count in zip(piApprox, range(len(piApprox))):
        if ch != realPiApprox[count]:
            break
    print()
    print("pi approximation is accurate to {} digits after the decimal".format(count - 2))


def getPi():
    from decimal import Decimal, getcontext

    getcontext().prec = 100

    two = Decimal("2.0")
    p = two # product
    n = two # numerator
    d = Decimal("3.0") # denominator
    b = True
    try:
        while True:
            p *= n / d

            if b:
                n += two
                b = False
            else:
                d += two
                b = True
    except KeyboardInterrupt:
        # upon receiving KeyboardInterrupt, return pi approximation
        return p * 2


if __name__ == '__main__':
    # this checks to see if this file is being run as the main program
    # if it is, then it will call the main function we have defined
    # NOTE: put this at the end so that all of the functions are loaded
    main()
