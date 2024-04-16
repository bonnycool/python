import turtle

t=turtle.Turtle()

t.speed(2)
t.fillcolor("red")

t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
   
t.end_fill()

turtle.Mainloop()

