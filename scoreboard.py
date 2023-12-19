import turtle


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = 0
        self.high_score = 0
        self.show()

    def reset_round(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file_score:
                file_score.write(str(self.score))
        self.score = 0
        self.clear()
        self.show()

    def calculate(self):
        self.score += 1
        self.clear()
        self.show()

    def show(self):
        self.sety(270)
        with open("data.txt", "r") as file_score:
            self.high_score = int(file_score.read())
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=('Courier', 18, 'bold'))
