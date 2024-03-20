from turtle import Turtle
from random import randint

def main():
    turtles = []
    turtles.append(set_turtles('red', 120))
    turtles.append(set_turtles('orange', 100))
    turtles.append(set_turtles('yellow', 80))
    turtles.append(set_turtles('green', 60))
    turtles.append(set_turtles('blue', 40))
    turtles.append(set_turtles('purple', 20))
    
    for _ in range(300):
        for t in turtles:
            t.forward(randint(1,10))

    input("Enter to end")

def set_turtles(color: str, vert: int) -> Turtle:
    t = Turtle()
    t.color(color)
    t.shape('turtle')
    t.penup()
    t.goto(-800, vert)
    t.pendown()
    return t

if __name__ == "__main__": 
    main()
