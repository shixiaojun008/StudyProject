import turtle

t = turtle.Pen()
t.pensize(3)
t.pencolor("green")
t.speed(0)

width = 600
step = 40

points = [(-width/2,width/2), (-width/2,-width/2),(width/2,-width/2),(width/2,width/2)]
print(points[0])
t.penup()

for i in range(len(points)):
    t.goto(points[i])
    t.pendown()
t.goto(points[0])

for x in range(int(width/step)):
    t.penup()
    t.goto(-width/2+step*x, width/2)
    t.pendown()
    t.goto(-width/2+step*x, -width/2)

for y in range(int(width/step)):
    t.penup()
    t.goto(-width/2, width/2-step*y)
    t.pendown()
    t.goto(width/2, width/2-step*y)


turtle.done()

