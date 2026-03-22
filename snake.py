from turtle import Turtle

LARGO_INICIAL = 3
SNAKE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.body = []
    self.crear_vivorita()
    self.head = self.body[0]

  def crear_vivorita(self):
    for i in range(0, LARGO_INICIAL):
      self.add_segment((-20 * i, 0))
  
  def add_segment(self, position):
    seg = Turtle("square")
    seg.penup()
    seg.color("green")
    seg.goto(position)
    self.body.append(seg)
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1): #es como el for de C
      coord_x = self.body[i - 1].xcor()
      coord_y = self.body[i - 1].ycor()
      self.body[i].goto(x = coord_x, y = coord_y)
    self.head.forward(SNAKE_STEP)
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
      self.heading = UP
  
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
      self.heading = DOWN

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
      self.heading = LEFT

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
      self.heading = RIGHT

  def extend(self):
    self.add_segment(self.body[-1].position())
  
  def collision(self):
    for seg in self.body[1:]: #slice desde el segundo al ultimo, es como haskell
      if self.head.distance(seg) == 0:
        return True
    return False
  
  def reset(self):
    for seg in self.body:
      seg.ht()
    self.body.clear()
    self.crear_vivorita()
    self.head = self.body[0]


