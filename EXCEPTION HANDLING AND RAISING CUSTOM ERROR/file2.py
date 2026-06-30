try : #wraps the risky code
    file = open("my_file.txt","r")
    content =file.read()
    print(content)

except FileNotFoundError: #rums if an exception occurs
    print("passing the FileNotFoundError")
else: #runs only if no exception occurs
    print("kuch gdbd ho gyi but it's fine !!")
    
finally: #always runs - whether there's an error or not
    print("important kaam ho gya yaha !!")
