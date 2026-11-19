class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    def fall_in_rectanggle(self, lowleft, upright):
        #LOWleft[0] = 5 upright[0] = 6
        ##Upleft[1] = 9  upright[0] = 7
        if lowleft[0] < self.x < upright[0]\
        and lowleft[1] < self.y < upright[0]:
            return True
        else:
            return False
    # def distance_from_point(self, point):
    #     print("distance")
    #     return ((self.x - point.x)**2 +
    #             (self.y - point.y)**2) ** 0.5
class Rectanggle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.uprightright = upright
#create the object
pointx = Point(2,4)
rechtanglex = Rectanggle(Point(5,6), Point(7,9))
pointx.fall_in_rectanggle(rechtanglex)

#create the object 
Point1 = Point(6,7)
#point2 = Point(2,2)
#invoke the object
Point1.fall_in_rectanggle((5, 6), (7, 9))
#print(Point1.distance_from_point(Point1))

    

