s_username="ECE"
S_password="123"
uname=input("enter user name")
password=input("enter password")
def validate():
    if (s_username==uname and s_password==password):
       return True
    else:
       return False
a=validate
print(a)

       