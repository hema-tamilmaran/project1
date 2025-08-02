class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    super().__init__(self,name,salary)
    def __init__(self,department):
        self.department=department
    def display(self):
        print(self.name,self.salary,self.departmant)                 
m1=Manager("ECE")
m1.display()