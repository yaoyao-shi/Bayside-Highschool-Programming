import turtle
bob = turtle.Turtle()

length = 50
num_angle = 4
degree = 360 / num_angle

for a in range(num_angle):
    bob.forward(length)
    bob.left(degree)
