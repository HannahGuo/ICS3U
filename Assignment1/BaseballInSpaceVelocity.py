# Hannah Guo
# February 22nd 2018
# ICS3UR
# This program calculates the velocity of a baseball thrown in space by using the user inputs of its distance thrown
# (in metres) and time in the air (in seconds). It divides the distance by the time to get the velocity, then prints
# our the velocity of the baseball.

print("This program calculates the velocity of a baseball in space.")  # brief program description, printed for the user

d = float(input("Please input the distance the baseball was thrown (in metres): "))   # user inputs distance the
                                                                                      # distance the baseball was thrown
                                                                                      # (as a float)

t = float(input("Please input the time the baseball was in the air (in seconds): "))  # user inputs the time the
                                                                                      # baseball was in the air
                                                                                      # (as a float)

V = float(d / t)  # calculates the baseball's velocity by dividing the distance the baseball traveled by the time it
                  # was in the air for, then assigns it to variable V as a float

print("The velocity of the baseball in space was: " + str(V) + "m/s.")  # prints out the velocity of the baseball
                                                                        # in space in metres per second