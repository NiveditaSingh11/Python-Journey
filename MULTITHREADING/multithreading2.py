import time 
import threading

def greet(name):
    print(f"hello, {name}")
    
t= threading.Thread(target=greet,args=("nivi",))
t.start()
t.join()

