# Hannah Guo
# February 22nd 2018
# ICS3UR
# This program converts a temperature given in Fahrenheit to Celsius. It takes in the user input of a temperature in
# Fahrenheit. With this value, it converts it into Celsius using the formula (5/9 (F - 32)) where F is the user input.
# It then prints out the rounded converted temperature.

print("This program converts a temperature in Fahrenheit to Celsius (returns a rounded answer.")  # brief program
                                                                                                  # description printed
                                                                                                  # for the user
F = float(input("Please input a temperature (in Fahrenheit): "))        # user inputs the Fahrenheit temperature
                                                                        # (as a float)

C = round(float((5 / 9) * (F - 32)))  # calculates the Celsius equivalent to the inputted Fahrenheit temperature using
                                      # the formula (5/9 (F - 32)), rounds the result, then assigns it to variable C

print("This temperature in Celsius is: " + str(C) + " degrees Celsius.")  # prints out the rounded temperature in
                                                                          # degrees Celsius