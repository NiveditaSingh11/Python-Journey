"""
To-Do List Application

-user input , variables and strings
-Lists and sets
-loops and conditions
-functions and strings 
"""

tasks =[]
completed_tasks =set()

# add a task
def add_task():
    "add a new task to to-do list"
    task= input("enter the new task :")
    tasks.append(task)
    print(f"<{task}> added successfully.\n")
# view the task

def view_task():
    "view all the tasks"
    if not tasks :
        print("no tasks available to display.")
    
    print("\n==== To-Do List ====")
    for idx,task in enumerate(tasks):
        status ="✅ Completed" if task in completed_tasks else "Pending"
        print(f"{idx}. {task} - {status}")
# mark the task as completed
def mark_completed(task_number):
    "mark a task as completed using it's number."
    if 1<= task_number <=len(tasks):
        task_item= tasks[task_number-1]
        completed_tasks.add(task_item)
        print(f"task -> {task_item} << marked as completed.\n")
        
    else:
        print("invalid task number.\n")
# delete a task
def delete_task(task_number):
    "delete a task from the list using its number"
    
    if 1<= task_number <= len(tasks):
        task_item =tasks.pop(task_number-1)
        completed_tasks.discard(task_item)
        print(f"Task >> {task_item} << deleted successfully ")
    
    else:
        print("invalid task number.\n")
        
while True :      
    print(""" ==== To-Do List App ====
      1. Add Task
      2. View Task
      3. Mark Task As Completed
      4. Delete Task
      5. Exit
      """)

    choice = input ("enter your choice (1-5) :")
    if choice == "1":
        add_task()

    elif choice=="2":
        view_task()

    elif choice=="3":
        task_no=int(input("enter the task number to be marked as completed :"))
        mark_completed(task_no)

    elif choice=="4":
      task_num=int(input("enter the task number to be deleted :"))    
      delete_task(task_num)
    elif choice=="5":
        print("exiting To-Do List .\n ")
        break
    else:
        print("invalid input.\n")