class phone():
    def _init_(self,brand,price,chargertype):
        self.brand=brand
        self.price=price
        self.chargertpye=chargertype
    def display(self):
        print("Brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)  

Sumsung = phone("Sumsung","6000000","ctype")   
Sumsung.display()   

redmi=phone("redmi","60000","ctype")
redmi.display()