class point:
    def __init__(self, x , y):
        self.x = x 
        self.y = y
x_value = float(input("guess the value in the x: " ))
y_value = float(input("guess the value in the y: "))
#creat the object
point_value = point(x_value, y_value)
class Rectangle:
    def __init__(self, lowerleft, upperright):
        self.lowerleft = lowerleft
        self.upperright = upperright

rechangle_value = Rectangle([1, 2], [4,6])
print(rechangle_value.lowerleft[0])