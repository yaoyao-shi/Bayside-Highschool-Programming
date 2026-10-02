import turtle

a = turtle.Turtle()

a.width(5)

f = 100
f2 = 20
r = 90

for times in range(7):
    a.forward(f)
    a.left(r)
    a.forward(f2)
    a.left(r)
    a.forward(f)
    a.right(r)
    a.forward(f2)
    a.right(r)
