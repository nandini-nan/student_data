#oops
#syntax
'''class classname():
    #attributes
    name="codegnan"
    year=2026
    place="vja"
    def fname(Self):
        print(statements....)
a=classmate()
a.fname()'''

#class declaration
'''class Details():
    name="nandu"
    place="pamarru"
    age="22"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.display()'''

#object instantiation
'''class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("nandu",22,"vja")
a.display()'''

'''class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("nandu",22,"vja")
a.display()
a.Data("nandini",22,"vja")
a.display'''

class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
name=input("enter name:")
age=input("enter age:")
place=input("enter Place:")
a.Data("name","age","place")
a.display()
