#file =open("my_text.txt","a")
#file.write("i know c,cpp,react js,html, css,javascript,gen ai and microsoft copilot.\n")
#file.write("i love to make mini projects in react.")
#file.write("my name is nivedita")
#file.close()

#with open("my_text.txt","r") as file:
#    for line in file:
#        print(line.strip())

#with open("my_text.txt","r") as file:
#    lines =file.readlines()
#    for i in lines:
#       print(i)
    
with open("my_text.txt","r") as file:
    lines =file.readline()
    print(lines)
    

with open("my_new_file.txt","a") as file:
    file.write("python is an easy language.")

try:
    with open("newfile.txt","r") as file:
       print(file.read())
    
except FileNotFoundError:
    print("sorry bro, file not available")
    
finally:
    print("program ended without crashing.")
    