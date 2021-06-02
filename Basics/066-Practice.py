import  turtle

t = turtle.Pen()
my_colors = ("red", "green", "yellow","black")
t.pensize(5)
t.speed(10)

for i in range(10):
    t.penup()
    t.goto(0, -i*20)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(20+i*20)

turtle.done()