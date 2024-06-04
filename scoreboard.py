from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.color("white")
        self.score = 0
        self.high_score = 0
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.score_card()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!(press R to restart)", align=ALIGNMENT, font=FONT)

    def score_card(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.clear()
        self.goto(x=0,y=280)
        self.write(arg=f"Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=260)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.score_card()
