class A :
    attr ="Hello World"
    def hello(self):
        print(self.attr)
a=A()
obj1=a.hello()
print(obj1)



class Person:
    def __init__(self,name,age,surname=""):
        self.name=name
        self.age=age
        self.surname=surname
    def my_method(self):
        print("Менің атым: "+self.name)
        print("Менің аты жөнім: "+self.surname)
        print("Менің жасым: " + str(self.age))


P1=Person("Kuka", 17,"Abdrazakov Kurmangazy")
P2=Person("Kuka", 17)
P1.my_method() 
P2.my_method()



class Car:
    def __init__(self,brand,year,submodel):
        self.brand=brand
        self.year=year
        self.surmodel=submodel
    def my_information(self):
        print("brand: "+self.brand)
        print("year: "+self.year)
        print("submodel: "+self.surmodel)


P1=Car("Mersedes","2010","Benz")
P1.my_information() 






