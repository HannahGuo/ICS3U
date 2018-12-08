# Hannah Guo
# February 22nd 2018
# ICS3UR
# This program calculates the circumference of a circle by using the user inputs of its radius (in centimetres).
# It implements Python's math library for the value of pi. The program calculates the product of two, the user's radius
# and pi (which is the formula for the circumference of a circle, 2(pi)(r)), then prints it out.

import math  # imports Python's math library so that the value for pi can be used

print("This program calculates the circumference of a circle.")  # brief program description, printed for the user

r = float(input("Please input the radius of the circle (in centimetres): "))   # user inputs the radius of the circle
                                                                               # (as a float)

C = float(2 * math.pi * r)  # calculates the circle's circumference by finding the product of two, pi
                            # (from the imported math library), and the circle's radius, then assigns it to variable C

print("The circumference of this circle is: " + str(C) + "cm.")  # prints out the circumference of the circle
                                                                 # in centimetres