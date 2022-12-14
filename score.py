from turtle import Turtle

FONT_FAMILY = "Courier"
FONT_SIZE = 17
FONT_WEIGHT = "normal"


def game_over():
    failed = Turtle()
    failed.penup()
    failed.color('Red')
    failed.goto(-1, -1)
    failed.write('Game Over', font=(FONT_FAMILY, FONT_SIZE, FONT_WEIGHT), align='center')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setheading(90)
        self.goto(0, 270)
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score:{self.score}', font=(FONT_FAMILY, FONT_SIZE, FONT_WEIGHT), align='center')

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
