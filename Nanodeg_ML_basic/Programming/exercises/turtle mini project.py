#draw letters KC
import turtle

def letters():
    window = turtle.Screen()
    kc = turtle.Turtle()
    kc.speed(3)
    kc.shape("turtle")
    kc.color("white")
    kc.setpos(-200,300)
    kc.color("blue")
    kc.rt(90)
    kc.forward(500)#first draw

    kc.setpos(-200,50)
    kc.setpos(0,300)
    kc.setpos(-200,50)
    kc.setpos(0,-200)#K completed

    kc.color("white")
    kc.setpos(300,300)
    kc.color("blue")
    kc.lt(90)
    kc.bk(200)
    kc.lt(90)
    kc.bk(500)
    kc.lt(90)
    kc.bk(200)#C completed

    window.exitonclick()

letters()
