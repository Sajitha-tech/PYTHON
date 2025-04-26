class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

rect1= Rectangle(6,5)
rect2= Rectangle(7,5)

print("Rectangle-1:")

print("Length:",rect1.length)
print("Width:",rect1.width)
print("Area:",rect1.area())
print("Perimeter:",rect1.perimeter())

print()

print("Rectangle-2:")

print("Length:",rect2.length)
print("Width:",rect2.width)
print("Area:",rect2.area())
print("Perimeter:",rect2.perimeter())

if rect1.area()>rect2.area():
    print("rectangle-1 area is bigger")
elif rect2.area()>rect1.area():
     print("rectangle-2 area is bigger")
else:
    print("Area of both rectangle is same")

