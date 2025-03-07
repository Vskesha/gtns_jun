import random
import turtle

number_of_obstacles = 20
step = 20
collision_distance = 10  # Distance threshold for collision

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("green")


obstacles = []
for _ in range(number_of_obstacles):
    obstacle = turtle.Turtle()
    obstacle.shape("circle")
    obstacle.color("black")
    obstacle.speed(0)
    obstacle.penup()
    obstacle.goto(random.randint(-250, 250), random.randint(-250, 250))
    obstacles.append(obstacle)

# Define movement functions
def move_up():
    y = t.ycor()  # Get current y-coordinate
    t.sety(y + step)  # Update y-coordinate
    t.setheading(90)

def move_down():
    y = t.ycor()
    t.sety(y - step)
    t.setheading(270)

def move_left():
    x = t.xcor()  # Get current x-coordinate
    t.setx(x - step)  # Update x-coordinate
    t.setheading(180)

def move_right():
    x = t.xcor()
    t.setx(x + step)
    t.setheading(0)

def stop_program():
    screen.bye()  # Close the program

# Function to display "Game Over" message
def display_game_over():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("red")
    pen.write("Game Over", align="center", font=("Arial", 24, "bold"))

# Function to disable key controls
def disable_controls():
    screen.onkey(None, "Up")
    screen.onkey(None, "Down")
    screen.onkey(None, "Left")
    screen.onkey(None, "Right")

# Function to check collision
def check_collision():
    for obstacle in obstacles:
        if t.distance(obstacle) < collision_distance:
            display_game_over()
            disable_controls()
            return
    screen.ontimer(check_collision, 100)  # Check again in 100ms


# Bind keys
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(stop_program, "q")  # Press 'q' to exit

# Start collision detection loop
check_collision()

turtle.done()
