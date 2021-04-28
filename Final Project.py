# import libraries for required for project
import turtle
import random
import time

# creating game display
console = turtle.Screen()
console.title('KILLER CENTIPEDE')
console.setup(width=700, height=700)
console.tracer(0)
turtle.bgcolor('green')

# setting the size dimensions
turtle.speed(5)
turtle.pensize(4)
turtle.penup()  # explain what this all means
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()

# Create centipede and bugs
centipede = turtle.Turtle()
centipede.speed(0.5)
centipede.shape('circle')  # just explain centi, speed, shape, color
centipede.color("brown")
centipede.penup()
centipede.goto(0, 0)
centipede.direction = 'stop'

bug = turtle.Turtle()
bug.speed(0)
bug.shape('circle')
bug.color('beige')
bug.penup()
bug.goto(20, 40)

# stores eaten bug in empty array
eaten_bugs = []

# player score display
scores = turtle.Turtle()
scores.speed(0)
scores.color("black")
scores.penup()
scores.hideturtle()
scores.goto(0, 300)
scores.write("Bugs Eaten :", align="center", font=("Courier", 24, "bold"))


# binding the game to the keyboard
def centipede_crawl_up():
    if centipede.direction != "down":
        centipede.direction = "up"


def centipede_crawl_down():
    if centipede.direction != "up":
        centipede.direction = "down"


def centipede_crawl_right():
    if centipede.direction != "left":
        centipede.direction = "right"


def centipede_crawl_left():
    if centipede.direction != "right":
        centipede.direction = "left"


def centipede_crawl():
    if centipede.direction == "up":
        y = centipede.ycor()
        centipede.sety(y + 20)

    if centipede.direction == "down":
        y = centipede.ycor()
        centipede.sety(y - 20)

    if centipede.direction == "right":
        x = centipede.xcor()
        centipede.setx(x + 20)

    if centipede.direction == "left":
        x = centipede.xcor()
        centipede.setx(x - 20)


# setting the bound keyboards to the console
console.listen()
console.onkeypress(centipede_crawl_up, "Up")
console.onkeypress(centipede_crawl_down, "Down")
console.onkeypress(centipede_crawl_right, "Right")
console.onkeypress(centipede_crawl_left, "Left")

# when the centipede eats the bug
if centipede.distance(bug) < 20:
    x = random.randint(-290, 270)
    y = random.randint(-240, 240)
    bug.goto(x, y)
    scores.clear()
    score += 1
    scores.write("Bugs Eaten:{}".format(score), align="center", font=("Courier", 24, "bold"))
    delay -= 0.001

    new_bug = turtle.Turtle()
    new_bug.speed(0)
    new_bug.shape('circle')
    new_bug.color('beige')
    new_bug.penup()
    eaten_bugs.append(new_bug)

for index in range(len(eaten_bugs) - 1, 0, -1):
    a = eaten_bugs[index - 1].xcor()
    b = eaten_bugs[index - 1].ycor()
    eaten_bugs[index].goto(a, b)

if len(eaten_bugs) > 0:
    a = centipede.xcor()
    b = centipede.ycor()
    eaten_bugs[0].goto(a, b)
centipede_crawl()

# collision physics

# when the centipede hits itself
for prey in eaten_bugs:
    if prey.distance(centipede) < 20:
        time.sleep(1)
        console.clear()
        console.bgcolor('green')
        scores.goto(0, 0)
        scores.write("    GAME OVER \n You Have Eaten {}".format(score), align="center", font=("Courier", 30, "bold"))

# when the centipede hits the wall
if centipede.xcor() > 280 or centipede.xcor() < -300 or centipede.ycor() > 240 or centipede.ycor() < -240:
    time.sleep(1)
    console.clear()
    console.bgcolor('green')
    scores.goto(0, 0)
    scores.write("   GAME OVER \n You Have Eaten {}".format(score), align="center", font=("Courier", 30, "bold"))
