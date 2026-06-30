try :
    result = 10/0   #this gives ZeroDivisionError
    # result =10 /"6" -->this gives TypeError
    
except TypeError:
    print("passing the type-error")
    
except ZeroDivisionError:
    print ("passing the ZeroDivisionError")
    
except ValueError:
    print("passing the ValueError")
finally :
    print("Program ends here with confidential information.")



try :
   mynum = int("hello")
   print (mynum)
    
except ValueError:
    print("passing the ValueError")
    
except TypeError:
    print("passing the type-error")
    
except ZeroDivisionError:
    print ("passing the ZeroDivisionError")
    

finally :
    print("Program ends here with confidential information.")
    


