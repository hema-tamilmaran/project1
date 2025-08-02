class Animal():
    def sound(self):
        print("Animal Make Sound")
class Dog(Animal):
    def sound(self):  
        print("Dog Backs")  
class Bird(Animal):
    def sound(self):
        print("Birds Sing")   

d1=Dog()
d1.sound()
b1=Bird()
b1.sound()