import time
import threading
def print_numbers():
    for i in range(5):
        print(f"number:{i}")
        time.sleep(2)
        
def print_letters():
    for ch in 'abcdefghij':
        print(f"letter :{ch}")
        time.sleep(1)

t1= threading.Thread(target = print_numbers)
t2= threading.Thread(target = print_letters)

t1.start()
t2.start()

t1.join()
t2.join()
print("done running the program.")


#print_numbers()
#print_letters()
