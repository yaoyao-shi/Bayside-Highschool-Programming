import turtle

a = turtle.Turtle()

w = 50
s = 5
l = 360 / s

a.pensize(5)

for times in range(s):
    a.forward(w)
    a.left(l)

s += 1
l = 360 / s

a.penup()
a.goto(150, 0)
a.pendown()

a.color("red")
for times in range(s):
    a.forward(w)
    a.left(l)

s = 8
l = 135

a.penup()
a.goto(-150, 0)
a.pendown()

a.color("yellow")
for times in range(s):
    a.forward(w)
    a.left(l)

a.penup()
a.goto(0, -150)
a.pendown()
a.right(180)

a.color("green")
a.circle(100)
