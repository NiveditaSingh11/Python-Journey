"""
Contact Manager App 

A beginner-friendly project demonstrating :
-variables , user input ,typecasting
-lists and dictionaries
-loops and control flow
-functions and f-strings
"""

contacts =[]

# add contact
def add_contact():
    "add a new contact to the list."
    name = input("enter the name:")
    phone =input("enter the phone number:")
    email =input("enter the email:")
    
    contact_info ={
        "name" :name,
        "phone":phone,
        "email":email
    }
    
    contacts.append(contact_info)
    print(f"contact for > {name}> saved successfully ✅\n")
# view contact
def view_contact():
    "view the saved contacts."
    if not contacts :
        print("no contacts found to display.\n")
        return
    
    print("\n==== Contact List ====")
    for idx ,c in enumerate(contacts ):
        print(f"{idx}. {c['name']} <-> {c['phone']} <-> {c['email']}")
        
# search contact
def search_contact(search_name):
    "search for a contact by name "
    for member in contacts:
        if member['name'].lower() == search_name.lower():
            print(f"found : {member['name']} | {member['phone']} | {member['email']}\n")
            return
        
    print(f"contact for {search_contact} not found\n")
# delete contact
def delete_contact(search_name):
    "delete the contact."
    for member in contacts:
        if member['name'].lower() == search_name.lower():
            contacts.remove(member)
            print(f"contact deleted for -> {search_name}")
          
        print(f"contact for {search_contact} not found !!\n")
            
            
            
while True :
    print("""
==== Contact Details ====
          1. Add Contact
          2. View Contact
          3. Search Contact
          4. Delete Contact
          5. Exit
          
          """)
    
    choice =input ("enter your choice (1-5) ->")
    
    if choice =="1":
        add_contact()
    
    elif choice =="2":
        view_contact()
    elif choice =="3":
        search_name= input("enter the name to be searched :")
        search_contact(search_name)
    elif choice =="4":
        delete_number =input ("enter the name to be deleted from contacts : ")
        delete_contact(delete_number)
    elif choice =="5":
        print("exiting from the contact manager app!!")
        break
        
    else:
        print("invalid input !!")