import os
from dotenv import load_dotenv
from tasks import add_task, show_task
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
tasks = []

admin_mode = input("do you open the admin mode yes/ no" )
if admin_mode ==
   

    
with open("tasks.txt", "a") as file:
    file.write(f"{name} - {tasks} \n ")