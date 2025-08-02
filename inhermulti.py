class grandpa():
    def phone(self):
        print("grandpa phone")
class dad(grandpa):
    def money(self):
        print("dad money")
class son(dad):
    def laptop(self):
        print("sons laptop") 
ram= son()
ram.laptop()  
ram.money() 
d1=dad()
d1.phone()
