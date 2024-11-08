#Create a  studen class that takesname and marks of  3   subjects as arguments in constructorand ocrete a method for avg ofmarks

class student:
    def __init__(self, name, m1, m2, m3):
        self.name= name

        self.m1= m1
        self.m2=m2
        self.m3=m3

    def avgmarks(self):
        sum = self.m1+self.m2+self.m3

        print("hi " ,self.name, "  and avg marks is " , sum/3)


s1=student("zarin", 89,69,89 )        

s1.avgmarks()


