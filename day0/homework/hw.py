from turtle import *

#we wanr to paint a house


#step 1: dwaw a square 
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square
#drowing a doar

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)        #height of the doar
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#left window
penup()
goto(15, 120)
pendown()

left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)

#right window
penup()
goto(185, 120)
pendown()

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)



exitonclick()