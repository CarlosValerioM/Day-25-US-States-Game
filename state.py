from turtle import Turtle

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, us_state_input, x, y):
        self.goto(x, y)
        self.write(us_state_input, font=("Arial", 5, "bold"))
