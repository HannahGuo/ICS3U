# Hannah Guo
# March 29th 2018
# ICS3UR
# This program determines postage costs based on the inputted weight of the package (in grams) by using if/else
# conditions.

# brief program description, printed for the user
print("This program calculates postage costs based on the weight of the package (g).")

# receive an input from the user of their package's weight, cast to a float because of program specifications
packageWeight = float(input("Please enter in your package's weight (in grams): "))
cost = 0.00  # cost variable (a float) that changes based on the package weight (see logic below)

if packageWeight > 0.0:                                 # condition checking if the package weight entered is positive,
    if packageWeight > 100.0:                           # condition checking if the package weight is over 100g
        cost = round(0.90 + ((packageWeight - 100.0) * 0.03), 2)  # assigns cost the base cost of $0.90 of a package of
                                                                  # 100g, and an additional cost of $0.03 for every
                                                                  # additional gram past 100g. It rounds the cost to two
                                                                  # decimals since this is how cost is given (not with
                                                                  # a lot of decimal places for fractions of a cent).
    elif packageWeight > 50.0:                        # condition checking if the package weight is over 50g. Note
                                                      # that this will only run if the package weight is not over 100g
        cost = 0.90                                   # assigns cost to be $0.90
    elif packageWeight > 30.0:                        # condition checking if the package weight is over 30g. Note that
                                                      # this will only run if the package weight is not over 50g.
        cost = 0.70                                   # assigns cost to be $0.70
    else:                                             # for this else to run, the package weight must be below 30g
        cost = 0.48                                   # assigns cost to be $0.48
    print("The cost to ship this package will be $" + str(cost))  # prints out the cost to ship the package. Since the
                                                                  # cost variable is a float, it must be cast to a
                                                                  # string so it can be concatenated
else:                                                 # for this else to run, the package weight entered must have been
                                                      # negative
    print("An invalid package weight was entered (negative), please try again.")  # print out that this was an invalid
                                                                                  # input to the user
