import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')

def run_to_position(x,y):
    t.goto(x,y)
screen.onclick(run_to_position)
screen.mainloop()