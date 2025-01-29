import turtle

# Set up the turtle system
turtle.penup()
turtle.setposition(0, 400)
turtle.pendown()
turtle.speed(0)
turtle.tracer(2)  # Speed up the drawing process
turtle.pensize(3)
turtle.hideturtle()

# Function to generate the axiom
def axi(itr):
    axiom = "F-+"  # Initial axiom
    for _ in range(itr):  # Iteration loop
        tempax = ""
        for char in axiom:  # Iterate through each character in axiom
            if char == "+":
                tempax += "+"
            elif char == "-":
                tempax += "-"
            elif char == "F":
                # Replace "F" with the recursive pattern
                tempax += "F+F-F+F"
        axiom = tempax  # Update axiom in each iteration
        print(axiom)  # Print the axiom at each iteration
    return axiom

# Function to draw based on the axiom
def draw(axiom, dist):
    turtle.colormode(1.0)  # Switch to RGB color mode
    for char in axiom:  # Loop through the axiom to draw
        if char == "+":
            turtle.right(45)  # Turn right by 45 degrees
        elif char == "-":
            turtle.left(45)  # Turn left by 45 degrees
        elif char == "F":
	#you can type there is any color or write on RGB
            turtle.pencolor("lime")
            turtle.forward(dist)  # Move forward by the specified distance
    turtle.update()  # Update the screen after drawing
    turtle.mainloop()  # Keep the window open

# Main code
itr = 10  # Number of iterations
dist = 1.6  # Distance to move forward
axiom = axi(itr)  # Generate the axiom
draw(axiom, dist)  # Draw the fractal based on the axiom
