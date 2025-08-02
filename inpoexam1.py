class Person():
    def __init__ (self,name):
        self.name=name

class student():
    def __init__(self,name,grade):
        super(). __init__(name)
        self.grade=grade 
        
    def display(self):
        print(self.name,self.grade)             
s1=student("john","A")
s1.display()
         