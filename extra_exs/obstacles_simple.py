import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.goto(-380, 0)

number_of_obstacles = 20
step = 50
colision_distance = 50

obstacles = []  # Кожна перешкода - це черепашка, яка збережена у списку
for _ in range(number_of_obstacles):
    obstacle = turtle.Turtle()
    obstacle.shape("circle")
    obstacle.color("black")
    obstacle.shapesize(3, 3, 2)
    obstacle.speed(0)
    obstacle.penup()
    obstacle.goto(random.randint(-400, 400), random.randint(-250, 250))
    obstacles.append(obstacle)

game_over = False
while not game_over and t.xcor() < 400:
    direction = screen.textinput("Direction", "Set direction (up or down or forward): ")
    
    if direction:
        direction = direction.lower().strip()

    if direction == "up":
        t.left(90)
        t.forward(step)
        t.right(90)
    elif direction == "down":
        t.right(90)
        t.forward(step)
        t.left(90)
    t.forward(step)

    # Код для перевірки зіткнення
    for obstacle in obstacles:
        if obstacle.distance(t) < 25:
            pen = turtle.Turtle()
            pen.color("red")
            pen.write("Game Over!", font=("Arial", 30, "bold"), align="center")
            game_over = True
            break

if not game_over:
    pen = turtle.Turtle()
    pen.color("green")
    pen.write("Congratulations! You won!", font=("Arial", 24, "bold"), align="center")

turtle.done()
