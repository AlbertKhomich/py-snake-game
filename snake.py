from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.make_start_snake()

    def make_start_snake(self):
        for x in range(0, -41, -20):
            self.add_a_segment((x, 0))

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.make_start_snake()

    def add_a_segment(self, position):
        tim = Turtle("square", visible=False)
        tim.penup()
        tim.color("white")
        tim.goto(position)
        tim.showturtle()
        self.segments.append(tim)

    def snake_gross(self):
        self.add_a_segment(self.segments[-1].pos())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].pos())

        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
