class Shape:
    def __init__(self, color: str side: int angle: float):
        self._color = color
        self._side = side
        self._angle = angle

    def describe(self):
        return f'This is a {self._color } shape with {self._side} sides and {self._angle} angles'
    
class Polygon(Shape):
    pass
class Square(Shape):
    pass
class Circle(Shape):
    pass





def main():
    x = Shape('blue',0, 1.0)
    
    if__name__=="__main__":
        main()