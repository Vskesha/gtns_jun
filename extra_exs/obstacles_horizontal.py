import random
import turtle

number_of_obstacles = 40
step = 20
collision_distance = 15  # Distance threshold for collision

screen = turtle.Screen()
half_width = screen.window_width() // 2
half_height = screen.window_height() // 2
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.goto(-half_width, 0)

def write_instructions():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("Blue")
    pen.penup()
    pen.goto(0, half_height - 30)
    pen.write("Використовуй стрілки вверх і вниз, щоб уникнути зіткнення", align="center", font=("Arial", 15, "normal"))

def move_up():
    y = t.ycor()  # Get current y-coordinate
    t.sety(y + step)  # Update y-coordinate

def move_down():
    y = t.ycor()
    t.sety(y - step)

def move_right():
    x = t.xcor()
    t.setx(x + step)

# Function to display "Game Over" message
def display_game_over():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("red")
    pen.write("Game Over", align="center", font=("Arial", 30, "bold"))

def display_you_win():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("green")
    pen.write("You win", align="center", font=("Arial", 30, "bold"))

# Function to disable key controls
def disable_controls():
    screen.onkeyrelease(None, "Up")
    screen.onkeyrelease(None, "Down")

# Function to check collision
def check_collision():
    for obstacle in obstacles:
        if t.distance(obstacle) < collision_distance:
            display_game_over()
            disable_controls()
            return
    move_right()
    if t.xcor() >= half_width:
        display_you_win()
        disable_controls()
        return
    screen.ontimer(check_collision, 100)  # Check again in 100ms

def get_obstacles():
    obstacles = []
    for _ in range(number_of_obstacles):
        obstacle = turtle.Turtle()
        obstacle.shape("circle")
        obstacle.color("black")
        obstacle.speed(0)
        obstacle.penup()
        obstacle.goto(
            random.randint(-half_width, half_width), 
            random.randint(-int(half_height / 1.5), int(half_height / 1.5))
        )
        obstacles.append(obstacle)
    return obstacles

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

write_instructions()
obstacles = get_obstacles()
check_collision()

turtle.done()