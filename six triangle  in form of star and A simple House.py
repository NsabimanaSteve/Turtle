import turtle
def draw_triangle():
    for i in range(3):
        steve.forward(50)
        steve.left(120)

wn=turtle.Screen()
steve=turtle.Turtle()
steve.speed(100)
turn_angle=72
for _ in range(5):      
  steve.color("red")
  steve.left(turn_angle) 
  draw_triangle()
steve.penup()
steve.goto(40,80)
steve.pendown()

for i in range(4):
    steve.forward(100)
    steve.left(90)

steve.penup()
steve.goto(40,180)
steve.backward(15)
steve.pendown()
steve.forward(130)
steve.left(135)
steve.forward(90)
steve.left(90)
steve.forward(90)

wn.exitonclick()