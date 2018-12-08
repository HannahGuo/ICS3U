# Hannah Guo
# February 22nd 2018
# ICS3UR
# This program calculates the hypotenuse of a right angle triangle by using the user inputs of its opposite and adjacent
# sides (length in centimetres) to the hypotenuse. It uses a variation of the Pythagorean Theorem to find the
# hypotenuse, c = sqrt(a^2 + b ^2), where a is the adjacent side to the hypotenuse, b is the opposite side to the
# hypotenuse and c is the hypotenuse, then prints out the hypotenuse length in centimetres.

import math  # imports Python's math library so that the square root function can be used

print("This program calculates the hypotenuse of a right angle triangle.")  # brief program description for the user

a = float(input("Please input the length of the side adjacent to the hypotenuse (in centimetres): "))  # user inputs the
                                                                                                       # side length
                                                                                                       # adjacent to the
                                                                                                       # hypotenuse
                                                                                                       # (as a float)

b = float(input("Please input the length of the side opposite to the hypotenuse (in centimetres): "))  # user inputs the
                                                                                                       # side length
                                                                                                       # opposite to the
                                                                                                       # hypotenuse
                                                                                                       # (as a float)

c = float(math.sqrt((a ** 2) + (b ** 2)))  # calculates the length of the hypotenuse by using a variation of Pythagorean
                                           # Theorem (where they hypotenuse equals the square root (the square root
                                           # function is imported from the math library) of the sum of the
                                           # adjacent side (assigned to variable a) squared and the opposite side
                                           # (assigned to variable b) squared sides of the triangle to find the
                                           # hypotenuse, then assigns this to variable c as a float

print("The length of the hypotenuse for this right angle triangle is: " + str(c) + "cm.")  # prints out the length of
                                                                                           # the hypotenuse in
                                                                                           # centimetres