class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first +self.second

a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(1,3)
print(a.first)
print(b.first)