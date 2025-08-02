class a():
    def _init_(self):
        print("A")
    def display(self):
        print("you are in class a")
class b(a):
    def _init_(self):
        super().__init__ ()
        print("B")
    
    def display(self):
        print("you ate in class b")
class c(a,b):
    def _init_(self):
        super().__init__()
        print("c")
    def display(self):
        print("you are in class C")  

ob1= c(b,a)

         
            

