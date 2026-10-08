from tasks import add_task, show_task
name = input("whats your name ? ")
print("welcome","name", name)

number1 = int(input("enter the number : "))
print("the number", number1)
tasks = []


   

    
with open("tasks.txt", "a") as file:
    file.write(f"{name} - {tasks} \n ")