from turtle import Turtle, Screen
from random import randint


window = Screen()
window.setup(width=800, height=400)
window.title("Turtle Race")

SCREEN_HEIGHT = 400
FINISH_X = 380


def state(win):
    writer = Turtle("turtle")
    writer.hideturtle()
    if win:
        window.bgcolor("light green")
        writer.write("Congratulations🎉. You Won🏆", font=(
            "arial", 28, "bold"), align="center")
    else:
        window.bgcolor("pink")
        writer.write("You Lose!", font=("arial", 28, "bold"), align="center")


while True:
    user_choice = window.textinput(title="Make your bet",
                                   prompt="Guess the winner\nType a color: Red, Blue or Green ?")
    if user_choice in ["red", "green", "blue"]:
        break

# Draw finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(FINISH_X, SCREEN_HEIGHT//2 - 50)  # Top of screen
finish_line.setheading(270)  # Face down
finish_line.pendown()
finish_line.pensize(3)
finish_line.forward(SCREEN_HEIGHT - 100)  # Draw vertical line

# Display user's bet
bet_display = Turtle()
bet_display.hideturtle()
bet_display.penup()
bet_display.goto(0, SCREEN_HEIGHT//2 - 100)
bet_display.write(f"You bet on {user_choice.upper()}!",
                  align="center", font=("Arial", 16, "bold"))

turtles = []
colors = ("red", "blue", "green")
positions = ((-380, 40), (-380, 0), (-380, -40))

for i in range(3):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(positions[i])
    print(new_turtle.xcor())
    turtles.append(new_turtle)


game_on = True

while game_on:
    for turtle in turtles:
        turtle.forward(randint(1, 5))
        if turtle.xcor() >= 380:
            win = user_choice.strip().lower() == turtle.color()[0]
            state(win)
            game_on = False

window.exitonclick()
