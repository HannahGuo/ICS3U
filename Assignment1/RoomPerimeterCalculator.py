# Hannah Guo
# February 21st 2018
# ICS3UR
# This program calculates the perimeter of a rectangular room given the user inputs of the room's length and width
# (in feet) It multiplies the sum of the length and width by two (because a rectangle has two pairs of equal side
# lengths) and outputs the perimeter (in feet).

print("This program calculates the perimeter of a rectangular room.")  # brief program description, printed for the user
w = float(input("Please input the room's width (in feet): "))          # user inputs width of the room (as a float)
l = float(input("Please input the room's length (in feet): "))         # user inputs length of the room (as a float)
p = float(2 * (w + l))  # calculates perimeter of the room by adding the room's width and length, multiplies this sum
                        # by two, then assigns it to variable p as a float.

print("The perimeter of this room is: " + str(p) + "ft.")  # prints out the perimeter of this rectangular room in feet