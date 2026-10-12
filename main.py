import os
from dotenv import load_dotenv
from tasks import tasks
name = input("whats your name ? ")
print("welcome","name", name)
load_dotenv()

admin_password = os.getenv("QUIZ_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode ? yes/no")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password")
    if entered_password == admin_password:
        print("admin!  hi")
    else:
        print("wrong password")
number1 = int(input("enter the number : "))
print("the number", number1)

def add_task(tasks, task):
    for i in range(1, 2):
        task = input("enter the tasks number : ")
        tasks.append(task)


def show_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i, "-", task)


def mark_done(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

def show_task(tasks):

    task_number = int(input("Enter task number: "))

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] += " Done"
        print("Task marked as Done!")
    else:
        print("Invalid task number.")
tasks = []

while True:
    print("\n--- Personal Task Manager ---")
    
    print("Show Tasks / Done / exit")
    

    choice = input("Choose an option: ")

    if choice == "show tasks":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "Done":
        show_task(tasks)
        continue

    elif choice == "exit":
        mark_done(tasks)
        break


    if len(tasks) > 0:
         task_number = int(input("Enter task number to delete: "))

    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted!")
    else:
        print("Invalid task number.")

 
priority = input(tasks["tasks"])
print("Priority:", task["priority"])
   


   

    
with open("tasks.txt", "a") as file:
    file.write(f"{name} - {tasks}- {choice} - {admin_password}\n ")