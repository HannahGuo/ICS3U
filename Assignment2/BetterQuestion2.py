# Hannah Guo
# March 29th 2018
# ICS3UR
# This program determines if the inputted year is a leap year (has 366 days compared to the 365 days of a regular year)
# by using a provided algorithm.

#  brief program description, printed for the user
print("This program outputs if the inputted year is a leap year.")

# receive a year input from the user
year = int(input("Please enter a year: "))

# The following bit of logic was deduced from the given steps:
# 1. If the year is divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).
# After following the paths, the only ways one will end up on step 4 (that it is a leap year)
# a) If the year is divisible by 4 (step 1 is true) and not divisible by 100 (step 2 is false)
# b) If the year is divisible by 4 (step 1 is true), is divisible by 100 (step 3 is true) and is divisible by 400 (step
# 3 is true)
# These two conditions were put into the first if statement. The modulus (%) operator returns the remainder of the
# quotient of the year and the next number, and if that remainder is zero, the year is divisible by that number. The and
# keyword ensure that all conditions of a) or b) are met. The or keyword defines that as long as either option a is true
# or option b is true, then it is a leap year.

if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        print("This is a leap year.")  # prints out that the inputted year is a leap year
else:
    print("This is not a leap year.")  # prints out that the inputted year is not a leap year