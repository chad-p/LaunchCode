import turtle

def draw_line(length, angle):
    mike = turtle.Turtle()
    mike.color('blue')
    mike.left(angle)
    mike.forward(length / 2)
    mike.forward(-length)
    mike.left(90)
    mike.forward(length / 2)
    mike.right(90)
    mike.forward(length)
    mike.right(90)
    mike.forward(length)
    mike.right(90)
    mike.forward(length)
    mike.right(90)
    mike.forward(length / 2)
    mike.hideturtle()

def star(lines):
    for angle in range(0, 180, int(180/lines)):
        draw_line(200, angle)


wn = turtle.Screen()
wn.bgcolor('green')

star(10)

wn.exitonclick()