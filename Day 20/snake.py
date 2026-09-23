from turtle import Turtle
move_distance = 20
up = 90
down = 270
left = 180
right = 0




class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_positions = [(20, 0), (0, 0), (-20, 0)]
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(0)