from turtle import Turtle

FONT = ('Courier', 20, 'normal')
FONT2 = ('Times New Roman', 100, 'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.ht()
    self.penup()
    self.score = 0
    try:
      with open("../../../../Quilombo/highscore.txt") as file:  
        ##ruta relativa, desde donde estoy parado (seria "Curso Python") vuelve 4 carpetas atras y se ubica
        content = file.read().strip() ## strip le saca los whitespace
        self.highscore = int(content) if content else 0
    except FileNotFoundError:
      self.highscore = 0
      with open("/Users/feder/OneDrive/Escritorio/Quilombo/highscore.txt", "w") as file: ##ruta directa
        file.write("0")
    self.goto(x = 0, y = 310)
    self.color("white")
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"~ Score = {self.score} - Highscore = {self.highscore} ~", False, align="center", font = FONT)
  
  def add_score(self):
    self.score += 1
    self.update_scoreboard()

  def reset(self):
    if self.score > self.highscore:
      self.highscore = self.score
      with open("../../../../Quilombo/highscore.txt", mode = "w") as file:
        file.write(str(self.highscore))
    self.score = 0
    self.update_scoreboard()