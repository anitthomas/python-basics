import turtle
helix=turtle.Screen()
turtle.speed(2)
for i in range(10):
    turtle.circle(5*i)
    turtle.circle(-5*i)
