import turtle

t=turtle.Turtle()
t.speed(2)
t.penup()
t.goto(-350,0)
t.pendown()
for  i in range(10):
    t.forward(100)
    t.penup()
    t.forward(2)
    t.pendown()

turtle.mainloop()    