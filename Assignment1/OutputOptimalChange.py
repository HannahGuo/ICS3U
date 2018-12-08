# Hannah Guo
# February 23rd 2018
# ICS3UR
# This program calculates the most optimal amount of change for an amount below a dollar (this amount is an input from
# the user) in quarters, dimes, nickels and pennies.

print("This program outputs the optimal amount of change.")  # brief program description printed out for the user
num = int(input("Please input an amount (in cents, 99 or less) to calculate its optimal change: "))  # user inputs the
                                                                                                     # amount to
                                                                                                     # calculate change
                                                                                                     # for

# First, the pennies value is determined by finding the remainder of the inputted amount when divided by 5. This is done
# first so that the rest of the possible coin values, which are all multiples of 5, can be counted without the remainder
# of pennies.
pennies = int(num % 5)

# This variable tracks how much change still needs to be sortezd into coins. It's a bit redundant since the math can
# be done directly in the variable initialization, but it makes the logic easier to understand. remainingChange
# is first set to the difference between the original inputted number and the pennies because the values of pennies has
# already been calculated.
remainingChange = num - pennies

# The number of quarters is calculated by finding the remainder of the number when it is divided by 25 (how many cents
# a quarter is worth, then subtracting this value from remainingChange. This ensures that the expression
# (remainingChange - (remainingChange % 25)) will be a value divisible by 25. From there, divide this value by 25 to
# find the number of quarters. To get rid of the decimal at the end, the variable is cast to an integer.
quarters = int((remainingChange - (remainingChange % 25)) / 25)

# Since quarters have now been calculated, we can subtract that value from remainingChange as well. The variable
# quarters is multiplied by 25 because the variable quarters stores the number of quarters and not the value of the
# quarters. For example, if there were two quarters in the change, the variable quarters would be 2 but the value of
# both these quarters would be 50 (2 * 25) cents.
remainingChange -= (quarters * 25)

# The number of dimes is calculated by using the variable remainingChange, which is currently the value of change that
# still needs to be split into dimes and nickels. The remainder of remainingChange when divided by 10 is subtracted from
# remainingChange, which ensures that the expression (remainingChange - (remainingChange % 10)) will result in a value
# that is divisible by 10. From there, divide this value by 10 to find the number of dimes. To get rid of the decimal at
# the end, the variable is cast to an integer.
dimes = int((remainingChange - (remainingChange % 10)) / 10)

# Since dimes have now been calculated, we can subtract that value from remainingChange as well. Dimes is
# multiplied by 10 because the variable dimes stores the number of dimes and not the value of the dimes. For
# example, if there were two dimes in the change, the variable dimes would be 2 but the value of both these
# quarters would be 20 (2 * 10) cents. This is also the last time that remainingChange needs to be calculated, since
# nickels is the last possible coin value.
remainingChange -= (dimes * 10)

# After removing the values of pennies, quarters and dimes from remainingChange, remainingChange must be a multiple of
# 5. Therefore, the number of nickels can be calculated by dividing remainingChange by 5. Its cast to an integer to
# remove decimals.
nickels = int(remainingChange / 5)

# This prints out the most optimal change for the user's inputted change amount
print("The most optimal change for this amount is " + str(quarters) + " quarter(s), " + str(dimes) + " dime(s), "
      + str(nickels) + " nickel(s), and " + str(pennies) + " penny/pennies.")
