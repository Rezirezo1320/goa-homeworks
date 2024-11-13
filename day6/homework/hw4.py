from turtle import *

speed(30)
bgcolor("skyblue")

#field
color("green")
penup()
goto(-770, -100)
pendown()
begin_fill()
forward(1600)
right(90)
forward(500)
right(90)
forward(1600)
right(90)
forward(500)
end_fill()

#sun
color("yellow")
penup()
goto(-560, 290)
pendown()
begin_fill()
circle(100)
end_fill()

#home
color("orange")
penup()
goto(-200, -300)
pendown()
begin_fill()
forward(400)
right(90)
forward(400)
right(90)
forward(400)
right(90)
forward(400)
end_fill()

color("blue")
penup()
goto(-200, 100)
pendown()
begin_fill()
right(130)
forward(310)
right(100)
forward(310)
end_fill()

#door
color("red")
penup()
goto(-50, -300)
pendown()
begin_fill()
left(50)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
end_fill()

color("black")
penup()
goto(40, -200)
pendown()
begin_fill()
circle(5)
end_fill()

#window
width(7)
color("red")
penup()
goto(-160, -90)
pendown()
left(90)
forward(70)
left(90)
forward(100)
left(90)
forward(70)
left(90)
forward(100)

penup()
goto(160, -90)
pendown()
right(90)
forward(70)
right(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)

penup()
goto(125, -90)
pendown()
left(180)
forward(100)

penup()
goto(-125, -90)
pendown()
forward(100)













































































exitonclick()