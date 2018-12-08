# Hannah Guo
# March 29th 2018
# ICS3UR
# This program prints out if an inputted number is even or odd, as well as if it is positive, negative, or zero by using
# nested if statements and conditions. Note that zero is considered an even number.

# brief program description, printed for the user
print("This program outputs if a number is even or odd, as well as if it is positive, negative or zero.")

# receive a number input from the user, cast to an integer so that comparison operators can be properly used later
num = int(input("Please enter a number: "))

# The following if/else logic determines if the number is even or odd, and positive, negative or zero.
# The first if statement checks if the number is less than zero.
#
# If a number is less than zero, it must be negative.
# Nested inside this first if is logic that determines if the number is even or not by checking if its remainder is 0
# when divided by 2. If the remainder is 0, then number is even and the program will print out that the inputted number
# is negative and even. Otherwise (else), the number must be odd, so the program will print that the number is negative
# and odd.
#
# If the number is not less zero, the program will then check if (elif) its greater than zero. If this condition is
# true, the number must be positive. Nested inside this elif statement is another even/odd number condition checker,
# identical to the one in the first if. The only difference is that the print outs this time say that the number is
# positive (compared to negative), followed by if it's even or odd.
#
# Finally, if a number is neither positive nor negative, it must be zero. In this case, since zero is an even number,
# the program doesn't have a nested if statement for even/odd number checking, and instead prints out that the inputted
# number was 0, and is even.

if num < 0:
    if num % 2 == 0:
        print("The inputted number is negative and even.")
    else:
        print("The inputted number is negative and odd.")
elif num > 0:
    if num % 2 == 0:
        print("The inputted number is positive and even.")
    else:
        print("The inputted number is positive and odd.")
else:
    print("The inputted number is 0, which is an even number.")