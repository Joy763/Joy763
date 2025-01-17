import turtle
import random
turtle.shape("turtle")

turtle.speed(0)
for i in range(100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turtle.setposition(x,y)
    turtle.dot()
turtle.done()