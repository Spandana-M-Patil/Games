import math
from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
            and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False
    
    def distance_from_point(self, point):
        return math.sqrt((self.x-point.x)**2 + (self.y - point.y)**2)
    
class Rectangle:
    def __init__(self, lowleft, upright) -> None:
        self.lowleft = lowleft
        self.upright = upright
    
    def area_of_rectangle(self, area):
        area_of_rect = abs((self.upright.x - self.lowleft.x ) * \
                       (self.upright.y - self.lowleft.y)) 
        if area == area_of_rect:
            return 'Kudoos!! Your answer is right!!'
        else:
            return f'Oops!! Area is {area_of_rect} sq m'

class GuiRectangle(Rectangle):
    def __init__(self, lowleft, upright) -> None:
        super().__init__(lowleft, upright)

    def drawRectangle(self, canvas):
        breadth = abs(self.upright.x - self.lowleft.x)
        length = abs(self.upright.y - self.lowleft.y)
        
        canvas.penup()
        canvas.goto(self.lowleft.x,self.lowleft.y)
        
        canvas.color('black','yellow')
        canvas.begin_fill()
        canvas.pendown()
        canvas.forward(breadth)
        canvas.left(90)
        canvas.forward(length)
        canvas.left(90)
        canvas.forward(breadth)
        canvas.left(90)
        canvas.forward(length)
        canvas.end_fill()

class GuiPoint(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def drawPoint(self, canvas, size = 5, col = 'green'):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size, col)

# Generating the points for the rectangle
point1 = GuiPoint(randint(0,100),randint(0,100))
point2 = GuiPoint(randint(100, 200),randint(100,200))
rectangleA = GuiRectangle(point1, point2)
print(f"Cordinates of rectangle are {rectangleA.lowleft.x},{rectangleA.lowleft.y} and {rectangleA.upright.x},{rectangleA.upright.y}")

# Guessing the point from the user whether it lies inside the rectangle
pointx = GuiPoint(float(input('X coord: ')),float(input('Y coord: ')))
result = pointx.falls_in_rectangle(rectangleA)
print(f"Your answer is {result}")

print(rectangleA.area_of_rectangle(float(input('Area of rectangle : '))))

my_turtle = turtle.Turtle()
rectangleA.drawRectangle(my_turtle)
pointx.drawPoint(my_turtle)

turtle.done()

