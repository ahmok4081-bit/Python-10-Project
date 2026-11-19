class point:
    def __init__(self, x , y):
        self.x = x 
        self.y = y
    def guess_condition(self,lowerleft, upperright):
        if lowerleft[0] <= x_value <= upperright[0] and lowerleft[1] <= y_value <= upperright[1] :
            return True
        else:
            return False

x_value = float(input("guess the value in the x: " ))
y_value = float(input("guess the value in the y: "))
point_value = point(x_value, y_value)

class Rectangle:
    def __init__(self, lowerleft, upperright):
        self.lowerleft = lowerleft
        self.upperright = upperright

rechangle_value = Rectangle([1, 2], [4,6])
print(rechangle_value.lowerleft[0])
