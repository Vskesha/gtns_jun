import turtle

wn = turtle.Screen()
wn.title("homework")
wn.bgcolor("orange")
wn.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(1)
t.shape("turtle")

t.goto(0, 0)
t.forward(80)
t.up()
t.forward(50)
t.down()
t.forward(80)

t.penup()
t.goto(-100, 0)
height = 70
weight = 100
t.pendown()
t.backward(weight)
t.right(90)
t.forward(height)
t.left(90)
t.forward(weight)
t.right(90)
t.backward(height)
t.penup()
t.goto(0, 0)

wn.mainloop()