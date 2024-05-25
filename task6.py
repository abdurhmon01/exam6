class Shape:
    def __init__(self,ширина,длина):
        self.ширина=ширина
        self.длина=длина
class Area(Shape):
    def Area1(self):
        return f"area:{self.ширина*self.длина}"
class Perimetr(Shape):
    def Perimetr1(self):
        return f"perimetr:{2*(self.ширина+self.длина)}"
shape1=Area(ширина=2,длина=4)
shape2=Perimetr(ширина=2,длина=4)
print(shape1.Area1())
print(shape2.Perimetr1())        