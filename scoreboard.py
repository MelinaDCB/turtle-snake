from turtle import Turtle

FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.score = 0
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align="center", font=("Arial", 14, "normal"))
