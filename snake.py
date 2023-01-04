from turtle import Turtle

SPACES = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.spaces = SPACES
        self.create()
        self.head = self.snake_segments[0]

    def create(self):
        for turtle in range(3):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape('square')
            new_turtle.goto(y=0, x=self.spaces[turtle])
            new_turtle.color('white')
            self.snake_segments.append(new_turtle)

    def move(self):
        for square_pos in range(len(self.snake_segments) - 1, 0, -1):
            seg_xcor = self.snake_segments[square_pos - 1].xcor()
            seg_ycor = self.snake_segments[square_pos - 1].ycor()
            self.snake_segments[square_pos].goto(x=seg_xcor, y=seg_ycor)
        self.head.forward(MOVE_DISTANCE)

    def add_length(self):
        extra_turtle = Turtle()
        extra_turtle.penup()
        extra_turtle.shape('square')
        # extra_turtle.shapesize(0.5, 0.5)
        extra_turtle.speed('fastest')
        extra_turtle.color('white')
        extra_turtle.goto(self.snake_segments[-1].xcor(), self.snake_segments[-1].ycor())
        self.snake_segments.append(extra_turtle)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
