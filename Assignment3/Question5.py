# Hannah Guo
# April 18th 2018
# ICS3UR
# This program prints out all the prime numbers between 2 and 100 (inclusive) using nested loops and a boolean flag.

print("This program generates all the prime numbers between 2 and 100 (inclusive).")

for i in range(2, 101):    # this loops through all the numbers between 2 and 100. The ending range is 101 because range
                           # is exclusive, so to include 100, 101 must be the ending range.
    isPrime = True         # this sets the isPrime flag to True, and is reset to True every time the first for loop runs
    for j in range(2, i):  # this loops through all the numbers between 2 and the current iteration of i in the first
                           # for loop (exclusive). These are the caps because prime numbers can only be divided by 1 and
                           # themselves, meaning we want to check if the number i is divisible by numbers other than
                           # those.
        if i % j == 0:     # this checks if the number i is divisible by the current iteration of j. This checks every
                           # time that the j for loop runs. There is no else statement to this because there are only
                           # two values of isPrime (True and False). Since isPrime is already set to True every time the
                           # loop runs, no else statement is needed (since all it would do is set isPrime to True which
                           # is already done, so it's redundant).
            isPrime = False  # the isPrime flag sets to false if the current number i is in fact divisible by the
                             # current value for j. This means that the number is not a prime number because it is
                             # divisible by a number that isn't one or itself.
    if isPrime:   # once the j loop has finished checking, isPrime now correctly specifies if the current value of i is
                  # prime or not. If the number is prime, we want to print it out. No else is needed because we don't
                  # want to print out numbers that aren't prime. All an else would do is print nothing, which is
                  # useless.
        print(str(i) + " is prime")  # prints out i (cast to a string for string concatenation), which is a confirmed
                                     # prime number.
