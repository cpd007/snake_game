from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

''' COLORS '''
HEAD = "#FFC355"
TAIL_PRIMARY = "#FFC300"
TAIL_SECONDARY = "#DAF7A6"
MIX_FACTOR_NTH = 5


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.last_heading = self.head.heading()
        self.continue_loop = True

    # def create_snake(self):
    #     for position in STARTING_POSITIONS:
    #         self.add_segment(position)
    #
    # def add_segment(self, position):
    #     snake_segment = Turtle(shape='square')
    #     snake_segment.penup()
    #     snake_segment.color("white")
    #     snake_segment.goto(position)
    #     self.segment.append(snake_segment)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        if len(self.segment) % MIX_FACTOR_NTH == 0:
            new_segment.color(TAIL_SECONDARY)
        else:
            new_segment.color(TAIL_PRIMARY)
        new_segment.penup()
        new_segment.goto(position)
        # new_segment.setheading(STARTING_VECTOR)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for segment_index in range(len(self.segment) - 1, 0, -1):
            x = self.segment[segment_index - 1].xcor()
            y = self.segment[segment_index - 1].ycor()
            self.segment[segment_index].goto(x, y)
        self.head.forward(MOVING_DISTANCE)
        self.last_heading = self.head.heading()

    def up(self):
        if self.last_heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.last_heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.last_heading != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        self.continue_loop = False
        for segment in self.segment:
            segment.goto(1000,1000)

        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.last_heading = self.head.heading()
