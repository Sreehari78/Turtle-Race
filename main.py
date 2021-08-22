from turtle import Turtle, Screen
from random import randint


def expand_color(character):
    color_dict = {
        'r': "red",
        'o': "orange",
        'y': "yellow",
        'g': "green",
        'b': "blue",
        'i': "indigo",
        'v': "violet",
    }
    return color_dict[character]


screen = Screen()
racer_turtles = []
is_game_on = False
winning_color = None
winning_turtle = None

screen.colormode(255)
screen.setup(width=500, height=400)

user_bet = None
while (user_bet not in ['v', 'i', 'b', 'g', 'y', 'o', 'r']) and \
        (user_bet not in ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]):
    user_bet = screen.textinput(title="Make your bet!",
                                prompt="Which turtle will win the race? Enter the color: ").lower()

if user_bet in "vibgyor":
    user_bet = expand_color(user_bet)

print(f"You have chosen to be {user_bet}!")
colors = {
    0: ["red", (255, 0, 0)],
    1: ["orange", (255, 165, 0)],
    2: ["yellow", (255, 255, 0)],
    3: ["green", (0, 255, 0)],
    4: ["blue", (0, 0, 255)],
    5: ["indigo", (143, 0, 255)],
    6: ["violet", (75, 0, 130)]
}

for prepare_turtle in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[prepare_turtle][1])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-150 + prepare_turtle * 50)
    racer_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in racer_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_game_on = False
        speed = randint(0, 10)
        turtle.forward(speed)

for turtle_color in range(0, 7):
    if winning_color == colors[turtle_color][1]:
        winning_turtle = colors[turtle_color][0]

if winning_turtle == user_bet:
    print(f"You have won!! The {winning_turtle} is the winner!!")
else:
    print(f"You have lost!! The {winning_turtle} is the winner!!")

screen.exitonclick()
