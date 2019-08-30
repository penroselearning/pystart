import turtle

window = turtle.Screen()
window.bgcolor('black')

pen = turtle.Turtle()

pen.pencolor('red')


# Square - Top Left

pen.penup()
pen.setpos(-200,200)
pen.pendown()

pen.begin_fill()
pen.fillcolor("yellow")
for x in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# Triangle - Top Right

pen.penup()
pen.setpos(200,200)
pen.pendown()

pen.begin_fill()
pen.fillcolor("yellow")
for x in range(3):
    pen.forward(50)
    pen.left(120)
pen.end_fill()

# Pentagon - Bottom Left

pen.penup()
pen.setpos(-200,-200)
pen.pendown()

pen.begin_fill()
pen.fillcolor("yellow")
for x in range(5):
    pen.forward(50)
    pen.left(72)
pen.end_fill()

# Hexagon - Bottom Right

pen.penup()
pen.setpos(200,-200)
pen.pendown()

pen.begin_fill()
pen.fillcolor("yellow")
for x in range(6):
    pen.forward(50)
    pen.left(60)
pen.end_fill()

window.mainloop()