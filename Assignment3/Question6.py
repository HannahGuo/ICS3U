# Hannah Guo
# April 18th 2018
# ICS3UR
# This program prints out the height of a tennis ball as it bounces towards the ground. It receives an the starting
# height of the ball via an input from the user. From its initial height, the ball's height halves every time it
# bounces. Due to this algorithm alone resulting in an infinite loop (since the ball's height will never reach 0), the
# program stops running when the ball's height is 0.0000000000000001.

# brief program description printed for the user.
print("This program prints out the heights of a tennis ball dropped from an inputted height. Note that the program "
      "assumes that a ball height below 0.0000000000000001 metres means that the ball has reached the ground")

startingHeight = float(input("Input the starting height of the tennis ball (metres): "))  # receives the starting height
                                                                                          # of the tennis ball in
                                                                                          # metres, cast to a float for
                                                                                          # math operators later. Note
                                                                                          # that later on in the
                                                                                          # program, startingHeight is
                                                                                          # manipulated (its value
                                                                                          # changes)

numBounce = 0  # this counter keeps track of how many times the ball has bounced since it was dropped

while startingHeight > 0.0000000000000001:  # this while loop will run as long as startingHeight is greater than
                                            # 0.0000000000000001
    print("The ball is currently at " + str(startingHeight) + " metres.")  # print out startingHeight's current value
    startingHeight /= 2  # halves startingHeight every time the while loop runs
    numBounce += 1  # every time this while loop runs, the ball bounces another time. Increment the ball's bounce
                    # counter by one to keep track of how many times it has bounced.

print("The ball has reached the ground after " + str(numBounce) + " bounces.")  # prints out that the ball has reached
                                                                                # the ground, and says how many times it
                                                                                # bounced to do so. (numBounce is cast
                                                                                # to a string for string concatenation)