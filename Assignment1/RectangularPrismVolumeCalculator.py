# Hannah Guo
# February 21st 2018
# ICS3UR
# This program calculates the volume of a rectangular prism by using the user inputs of its length, width
# and height in metres. It multiplies these three values to get the volume of the rectangular prism, then prints out
# the rectangular prism's volume in metres cubed.

print("This program calculates the volume of a rectangular prism.")  # brief program description, printed for the user
l = float(input("Please input the prism's length (in metres): "))  # user inputs rectangular prism's length (as a float)
w = float(input("Please input the prism's width (in metres): "))   # user inputs rectangular prism's width (as a float)
h = float(input("Please input the prism's height (in metres): "))  # user inputs rectangular prism's height (as a float)
v = float(w * l * h)  # calculates rectangular prism volume by multiplying the width, length
                      # and height of the rectangular prism (as a float), then assigns it to variable v

print("The volume of this rectangular prism is: " + str(v) + "m^3.")  # prints out the volume of the
                                                                      # rectangular prism in metres cubed