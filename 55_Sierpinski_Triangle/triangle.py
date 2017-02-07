import turtle

def sp_triangle(depth, length, x, y):
    if depth == 0:
        return
    point = turtle.Turtle()
    point.speed(0)
    point.hideturtle()
    point.penup()
    point.setpos(x, y)
    point.pendown()
    sp_triangle(depth - 1, length / 2, point.xcor(), point.ycor())
    point.forward(length/2)
    sp_triangle(depth - 1, length / 2, point.xcor(), point.ycor())
    point.forward(length/2)
    point.left(120)
    point.forward(length)
    point.left(120)
    point.forward(length/2)
    sp_triangle(depth - 1, length / 2, point.xcor(), point.ycor())
    point.forward(length/2)

wn = turtle.Screen()

depth = int(input("How deep should we go? "))
sp_triangle(depth, 600, -300, -300)
#point = turtle.Turtle()
#_triangle(depth, 600, point, -300, -300)
