import turtle


t = turtle.Turtle()
t.speed(2) 

t.color("red")


t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

t.hideturtle()
turtle.done()
