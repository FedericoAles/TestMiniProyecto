from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 700, height = 700)
screen.bgcolor("black")
screen.title("Vivorita")
screen.tracer(0)

vivorita = Snake()
comida = Food()
score = Scoreboard()

screen.listen()
screen.onkey(vivorita.up, "Up")
screen.onkey(vivorita.down, "Down")
screen.onkey(vivorita.left, "Left")
screen.onkey(vivorita.right, "Right")

def game_loop():
  
  if vivorita.head.xcor() > 330 or vivorita.head.xcor() < -330 or vivorita.head.ycor() > 330 or vivorita.head.ycor() < -330:
    score.reset()
    vivorita.reset()

  if vivorita.collision():
    score.reset()
    vivorita.reset()

  vivorita.move()
  screen.update()
  screen.ontimer(game_loop, 100)
  if vivorita.head.distance(comida) < 15:
    comida.refresh()
    score.add_score()
    vivorita.extend()
  

game_loop()
screen.mainloop()
