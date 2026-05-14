#object intialization
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("nandu",22,"vja")
print(dir(a))
a.display()'''

#difference b/w _&__
'''class Employee1():
    def __init__(self):
        self.name="nandini"
        self.__salary=10000
        self._mailid="nandu@gmail.com"
class Employee2():
    def __init__(self):
        self.name="nandu"
        self.__salary=20000
        self._mailid="nandini@gmail.com"
a=Employee2()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee2__salary)'''

#polymorphism
#operation overloading
'''a=3;b=5
print(a+b)
print(a.__add__(b))
print(a.__add__(6))
print(a.__sub__(2))
print(a.__mul__(b))
#print(a._div_(2))
print(a.__pow__(2))
print(a.__ge__(2))
print(a.__le__(4))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(2))
print(a.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b))
print("nandu".__add__(" "+"n").title())'''

#operator over riding
#operator over riding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(4)
y=B(5)
#x=4
#y=5
#print(x+y)-> 9
print(x+y)'''

#method overloaing
'''class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is ",a+b+c)
        elif a!=None and b!=None:
            print("the produt is",a*b)
        else:
            print("program ends")


a=New()
a.sum(2,3,4)
a.sum()
a.sum(5,6)

#method overriding
class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#single inheritance
'''class RBI(): #parent class
    cash=100000
    def available_cash(cls):
       # print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI): #child-1
    pass
class HDFC(RBI): #child-2
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
b=HDFC()
b.available_cash()
b.new_cash()'''

'''class RBI(): #parent class
    cash=100000
    def available_cash(cls):
       print("available cash is",cls.cash)
       print("available cash is",RBI.cash)
       class SBI(RBI):
           cash=25000
    def new_cash(cls):
        print("new_cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
        class HDFC(RBI): #child-2
            cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
b=HDFC()
b.available_cash()
b.new_cash()'''

#MULTIPLE INHERITANCE
'''class Father: #Parent1
    weight=70
    def weight(self):
        print("70kgs")
class Mother: #parent2
    height=60
    def height(self):
        print("5.5 inches")
class kid(Father,Mother):
     def DOB(self):
        print("Just Born....")
c=kid()
c.weight()
c.height()
c.DOB()'''

'''class Father(): #parent-1
    def weight(self):
        print("70kgs")
class Mother(): #parent-2
    def height(self):
        print("5.5 inches")
class kid(): #child
    def DOB(self):
        print("Just Born....")
a=Father()
a.weight()
b.height()
c.DOB()'''

#MULTI LEVEL INHERITANCE
'''class grandparent():
    def land(self):
        print("5 acres")
class parent(grandparent):
    def house(self):
        print("1bhk")
class child(parent):
    def vehicle(self):
        print("pulsar")
a=child()
a.land()
a.house()
a.vehicle()'''

#encapsulation
#public data
'''class parent():
publicdata=10
def method1(self):
    print(self.publicdata)
class child(Parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''
        
#protecteddata
'''class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
print(obj1._protecteddata)
obj1.method1()
obj1.method2()'''

#_private data
'''class parent():
    _privatedata="nandu"
    def method1(self):
        print(self._privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''

#abstraction
'''class A():
 def method(self):
    #pass
obj1=A()
obj1.method()'''

'''class A():
    def method(Self):
        print("python class")
obj1=A()
obj1.method()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
obj1=A()
obj1,method1()'''

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 implemented")
    @abstractmethod
    def method3():
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()
