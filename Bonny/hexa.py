import turtle

t=turtle.Turtle()

t.speed(2)
t.fillcolor("red")

t.begin_fill()
for i in range(6):
    t.forward(100)
    t.left(60)
    t.forward(10)
    t.left(120)
    t.forward(100)
    t.left(120)

t.end_fill()

