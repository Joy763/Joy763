import turtle
import random
turtle.shape("turtle")

turtle.speed(0)
for i in range(200):
    x = random.randint(-300,300)
    y = random.randint(-250,250)
    turtle.setposition(x,y)
    turtle.dot()
turtle.done()