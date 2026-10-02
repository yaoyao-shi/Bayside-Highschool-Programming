import turtle

bob = turtle.Turtle()

turtle.screensize(canvwidth=200, canvheight=200, bg=None)

bob.color("yellow")
for i in range(3):
    bob.forward(50)
    bob.left(120)

bob.color("red")
for i in range(4):
    bob.forward(75)
    bob.left(90)

bob.color("green")
for i in range(5):
    bob.forward(100)
    bob.left(72)
