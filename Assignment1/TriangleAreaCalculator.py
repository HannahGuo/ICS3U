# Hannah Guo
# February 22nd 2018
# ICS3UR
# This program calculates the rounded area of a triangle by using the user inputs of its base and height in centimetres.
# It multiplies these values, then divides by two to get the area of the triangle, rounds the result, and prints out
# the rounded area in centimetres squared.

print("This program calculates the rounded area of a triangle.")  # brief program description, printed for the user
b = float(input("Please input the triangle's base (in centimetres): "))    # user inputs triangle's base (as a float)
h = float(input("Please input the triangle's height (in centimetres): "))  # user inputs triangle's height (as a float)
A = round(float((b * h) / 2))  # calculates the triangle's area by multiplying the base and height and dividing this
                               # product by two, then rounds the result and assigns it to variable A

print("The area of this triangle is: " + str(A) + "cm^2.")  # prints out the rounded area of the triangle in
                                                            # centimetres squared