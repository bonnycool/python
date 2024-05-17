import turtle
import  random

t=turtle.Turtle()
t.speed(2)
t.color("blue","orange")
t.begin_fill()

for i in range(36):
    
    if i %2==0:
        t.forward(50)
        t.left(random.randint(1,270))
    else:
        t.forward(50)
        t.left(random.randint(1,270))  
    
t.end_fill() 
   

 

t.end_fill()      