class company():
    def __init__(self):
        self.__companyname="Google"
    def companyname(self):  
        print(self.__companyname)  
c1=company()
c1.companyname()
print(c1.__companyname)