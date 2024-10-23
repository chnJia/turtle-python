import turtle

turtle.bgcolor("#e0d9ff")

def draw_heart():
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    turtle.circle(-112, 200)
    turtle.left(120)
    turtle.circle(-112, 200)
    turtle.forward(224)
    turtle.end_fill()

turtle.penup()  
turtle.goto(0, -200)  
turtle.pendown()  
turtle.pensize(3)  
turtle.speed(1)

draw_heart()

turtle.penup()
turtle.goto(0, -30) 
turtle.pendown()
turtle.color("white") 
turtle.write("I love you, pookie!", align="center", font=("Comic Sans MS", 24, "bold"))  

turtle.done()