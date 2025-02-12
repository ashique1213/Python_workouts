
class Area:
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
    
    def area(self):

        return self.length * self.bredth

tri = Area(10,4)
print(tri.area())

        