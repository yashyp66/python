class box:
    def __init__(self,length):
        self.len=length
    def area(self):
        ar=self.len*self.len
        return ar
    def vol(self):
        vol=self.len*self.len*self.len
        return vol
a=int(input("enter length : "))
square=box(a)
print(square.area())
print(square.vol())