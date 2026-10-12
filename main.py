import os
from dotenv import load_dotenv

admin_Mode = input("Are you an admin? (yes or no): ")

load_dotenv()
ADMIN_PASSWORD = os.getenv("TASKMANAGERADMINPASSWORD")

if admin_Mode.lower() == "yes":
    authentication = input("Enter the password: ")
    if authentication == ADMIN_PASSWORD:
        print("Admin mode activated.")
    else:
        print("Access denied. password is incorrect.")
    
elif admin_Mode.lower() == "no":
    username = input("Please enter your name: ")

    print(f"Welcome {username}!")

    from tasks import taskes

    print("\n----------\n")


    for task in taskes:
        print(f" Name: {task["name"]} - \n- Status: {task["status"].title()}\n- Priority: {task["priority"].title()}\n- Description: {task["description"]}")
        if task != taskes[-1]:
            print("\n---\n")

    with open("tasks.txt", "a") as file:
        for task in taskes:
            file.write(f"- Name: {task["name"].title()}\n- Status: {task["status"].title()}\n- Priority: {task["priority"].title()}\n- Description: {task["description"]}")
            file.write("\n---\n")