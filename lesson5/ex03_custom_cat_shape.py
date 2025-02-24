import turtle
from pathlib import Path

screen = turtle.Screen()
t = turtle.Turtle()

image_name = "cat_cry.gif"
print(Path(__file__))
image_path = str(Path(__file__).parent.joinpath(image_name)) 

screen.addshape(image_path)
t.shape(image_path)
t.forward(100)

turtle.done()
