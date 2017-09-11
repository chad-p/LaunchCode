import turtle              # 1. import the modules


wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('green')

turtle = turtle.Turtle()    # 3. Create turtle
turtle.color('blue')
turtle.shape('classic')

turtle.up()                  # 4. Move the turtle to starting point
turtle.goto(0, 0)
turtle.down()



wn.exitonclick()
