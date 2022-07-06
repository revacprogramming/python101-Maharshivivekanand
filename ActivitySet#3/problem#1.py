from turtle import *
import random

t = Turtle()
h = Turtle()
h.speed("slow")
h.hideturtle()
t.hideturtle()
my_screen = Screen()
my_screen.screensize(100, 600)
my_screen.bgcolor("grey")
my_screen.colormode(255)


def coloor():
    r = random.randint(1, 255)
    g = random.randint(0, 255)
    b = random.randint(1, 255)
    return r, g, b

def heart(t):

    t.speed("fastest")

    t.pensize(3)
    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()


def move(h)  :
    h.penup()
    h.goto(0, 50)
    h.pendown()
    h.color("white")
    h.write("Happy birthaday ", False, "center", ('AkayaKanadaka', 100, "bold"))
    h.color("black")
    h.write("Happy birthaday ", False, "center", ('AkayaKanadaka', 102, "bold"))

def maggy(h):
    h.penup()
    h.home()
    h.goto(0, -150)
    h.color("white")
    h.write('Maggy', False, "center",("Arial", 150, "bold"))
    h.color("black")
    h.write('Maggy', False, "center", ("Arial", 155, "bold"))

def circle(t):

    t.penup()
    t.goto(random.randint(1, 100), random.randint(1, 100))
    t.speed("fastest")
    colour = color()
    t.color(colour)
    t.begin_fill()
    t.circle(100)
    t.end_fill()


while True:

    t.clear()
    t.home()


    t.left(140)
    move(h)
    circle(t)





my_screen.exitonclick()