try:

   a=int(input())
   b=int(input())
   c=input()
   print(d)
   print(c/a)
except ValueError as e:
   print("value error",e)   
except TypeError as e:
   print ("Type Error",e) 
except Exception:
   print("something wrong")     
except Exception as e:
   print("something",e)   
finally:
   print("Done")   
