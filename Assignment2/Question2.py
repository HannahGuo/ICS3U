# Hannah Guo
# March 29th 2018
# ICS3UR
# This program determines if the inputted year is a leap year by using a provided algorithm by using nested if
# statements. This is not the most optimal way to implement the algorithm, but it was required. Here is the algorithm
# used:
# 1. If the year is divisible by 4, go to step 2.  Otherwise, go to step 5.
# 2. If the year is divisible by 100, go to step 3.  Otherwise, go to step 4.
# 3. If the year is divisible by 400, go to step 4.  Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).
# Note that if an invalid (negative) year were to be entered, the program would print that it was an invalid year input
# and that it was not a leap year.

#  brief program description, printed for the user
print("This program outputs if the inputted year is a leap year.")

# receive a year input from the user, cast to an integer so that comparison operators can be properly used later
year = int(input("Please enter a year: "))

if year > 0:                                   # condition checking if the year is positive (greater than 0)
    if year % 4 == 0:                          # condition checking if the year is divisible by 4
        if year % 100 == 0:                    # condition checking if the year is divisible by 100
            if year % 400 == 0:                # condition checking if the year is divisible by 400
                print("This is a leap year.")  # prints out that the inputted year is a leap year
            else:                              # if the year is not divisible by 400, the code in this else runs
                print("This is not a leap year.")  # prints out that the inputted year is not a leap year
        else:                                  # if the year is not divisible by 100, the code in this else runs
            print("This is a leap year.")      # prints out that the inputted year is a leap year
    else:                                      # if the year is not divisible by 4, the code in this else runs
        print("This is not a leap year.")      # prints out that the inputted year is not a leap year
else:                                          # runs if the year entered was invalid (negative)
    print("Invalid year input, please try again. This is not a leap year.")  # prints out that this year was invalid
