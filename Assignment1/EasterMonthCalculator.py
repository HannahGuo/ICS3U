# Hannah Guo
# February 26th 2018
# ICS3UR
# This program calculates the date (month and day) Easter will fall on for a year inputted by the user. It uses an
# algorithm that was given in pseudocode, so I just translated it into Python. Note that the algorithm used is outdated
# for current years, so not all years will return accurate results.

print("This program calculates when Easter will be for an inputted year.")  # brief program description, printed for the
                                                                            #  user

year = int(input("Please input the year that you would like to find Easter's date for: "))  # prompts user for the year
                                                                                            # to find when Easter is
                                                                                            # during that year, cast as
                                                                                            # an int to be used for math
                                                                                            # in the Easter algorithm
# The following code block makes up the Easter algorithm.
# % means modulus and finds the remainder of when the first number is divided by the second
# / is a division symbol and finds the quotient of the two numbers
# * is a multiplication symbol and finds the product of two numbers
# + is an addition symbol and finds the sum of two numbers
# - is a subtraction symbol and finds the difference of two numbers
# () are brackets so that BEDMAS (brackets, exponents, division/multiplication, addition/subtraction) rules are followed
# = assigns the value on the right to the variable on the left
# year was the user's inputted year
# This algorithm was given.

z = year % 19
y = year / 100
x = year % 100
w = y / 4
v = y % 4
u = ((8 * y) + 13) / 25
t = ((19 * z) + y - w - u + 15) % 30
s = (z + (11 * t)) / 319
r = x / 4
q = x % 4
p = ((2 * v) + (2 * r) - t - s - q + 32) % 7

month = int((t - s + p + 90) / 28)  # the month of Easter calculated using the algorithm, where 3 is March and 4 is
                                    # April, casted to an int to get rid of the floating decimal points
day = int((t - s + p + month + 19) % 32)  # the day of Easter calculated using the algorithm, casted to an int to get
                                          # rid of the floating decimal points
monthName = "March" if month == 3 else "April"  # ternary operator that changes the int value of month to the actual
                                                # name of the month, so 3 is March and 4 is April
print("Easter falls on " + monthName + " " + str(day) + "th.")  # this prints out the date (month and day) of Easter
                                                                # for the year inputted by the user