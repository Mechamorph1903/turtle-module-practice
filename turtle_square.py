import turtle

# Get the size of the square
square_size = turtle.numinput("Square Size", "How big do you want your square to be?")

# Compute the starting coordinates. We will move the turtle
# position so that the square is drawn in the center of the
# grid.  This is the coordinate of the bottom left corner
# of the square, where we will start drawing it.
start_x = 0 - (square_size // 2)
start_y = start_x

# Raise the pen so that no drawing occurs.
turtle.penup()
# Move the turtle's position to the bottom left corner
# of the square.
turtle.setposition(start_x, start_y)

# Put the pen back down.
turtle.pendown()

# We are going to fill the square with "blue"
turtle.fillcolor('blue')
# Begin filling the square.
turtle.begin_fill()

# Set the direction of the turtle to point right
# starting off.
turtle.setheading(0)
# Move the turtle based off the length of the square side.
turtle.forward(square_size)
# Turn the turtle left by 90 degrees so it is facing up.
turtle.left(90)
# Move the turtle forward again for the length of the square
# side.  Repeat this process for the rest of the square.
turtle.forward(square_size)
turtle.left(90)
turtle.forward(square_size)
turtle.left(90)
turtle.forward(square_size)

# This will apply the blue fill to the square once it has
# been drawn.
turtle.end_fill()

# Needed to keep window open!
turtle.done()