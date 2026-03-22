from turtle import Turtle
import random
from data import colors

class Food(Turtle): #Turtle es la super class, Food es una subclase
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len = 0.5 , stretch_wid = 0.5) #20 pixeles a la mitad, osea 10
    self.speed("fastest")
    self.refresh()

  def refresh(self):
    self.color(random.choice(colors))
    random_x = random.randrange(-320, 320, 20)
    random_y = random.randrange(-320, 320, 20)
    self.goto(x = random_x, y = random_y)