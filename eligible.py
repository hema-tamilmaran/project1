salary=int (input())
age=int(input())
if(salary>=20000 or age<=25 ):
    loan=int(input("loan:"))
    if(loan>50000):
        print("maximum loan amount")
    else:    
        print("you eligible")
else:
    print("not eligible")    
