import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

#draw a square
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("#a0c8f0")
    brad.speed(5)
    total_sides = 4
    now = 0
    while now < total_sides:
        brad.forward(100)
        brad.right(90)
        now += 1

#draw a circle
    angie = turtle.Turtle()
    angie.shape("classic")
    angie.color("blue")
    angie.circle(100)

#draw a triangle
    tri = turtle.Turtle()
    tri.shape("turtle")
    tri.color("pink")
    total = 3
    present = 0
    while present < total:
        tri.forward(50)
        tri.right(120)
        present += 1

    window.exitonclick()

draw_shapes()
