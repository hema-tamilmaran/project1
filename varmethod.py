class laptop():
    chargertype="b type"
    def _init_(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod
    def changechargertype(cls):
        cls.chargertype="bype"
        print("charger type changed to b")
    @staticmethod
    def info():
        print("This is laptop class")    

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype()
hp.info()