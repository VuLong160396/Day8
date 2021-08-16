import turtle
t = turtle.Pen()
d = 0 
for x in range(100) :
    t.forward(d)
    t.left(20)
    d += 1
turtle.done()