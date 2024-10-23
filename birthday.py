import turtle
import time

t = turtle.Turtle()
t.speed(3)
turtle.bgcolor("black")
turtle.title("Birthday")

def draw_cake():
    def draw_layer(x, y, width, height, layer_color, border_color):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(border_color, layer_color)
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    draw_layer(-150, -100, 300, 100, "lightpink", "hotpink")

    draw_layer(-120, 0, 240, 70, "peachpuff", "orange")

    draw_layer(-90, 70, 180, 50, "lavender", "purple")

candle_positions = [-40, 0, 40]  
for pos in candle_positions:
    t.penup()
    t.goto(pos, 120)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for _ in range(2):
        t.forward(10)   
        t.left(90)
        t.forward(40)   
        t.left(90)
    t.end_fill()

    # flame
    t.penup()
    t.goto(pos + 5, 160) 
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

def typewriter_message(message, delay=0.1):
    total_length = len(message) * 20 
    start_x = -total_length / 2 

    t.penup()
    t.goto(start_x, 200)  
    t.pendown()
    t.color("#fafaf5")
    t.hideturtle()

    for char in message:
        t.write(char, font=("Arial", 24, "bold"))
        t.penup() 
        t.forward(20)  
        t.pendown()   
        time.sleep(delay)

draw_cake()

typewriter_message("Late Birthday Present tadaaaaaaaa")

turtle.done()