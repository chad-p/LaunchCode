import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

lance = turtle.Turtle()
lance.color('black')
lance.shape('classic')

infile = open("helpers/mystery.txt", "r")

for line in infile:
    line = line.strip("\n")
    if line == "UP" or line == "DOWN":
        line = line.lower()
        method_to_call = getattr(lance, line)()
    else:
        values = line.split()
        lance.goto(int(values[0]), int(values[1]))
infile.close()


wn.exitonclick()
