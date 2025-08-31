todo_list = []
print("Welcome to ToDoList program")
print("Availbe commands: add/remove/show/exit")
        
def show_list(tasks):
            if not todo_list:
                print("Your list is empty!")
            else:
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task}")
def add_task(tasks):
            newtask = input("what task do you want to add: ")
            if newtask.lower() == "exit":
                return
            elif not newtask.strip():
                print("A task cannot be empty!")
                return
            else:
                todo_list.append(newtask)
                print(f"The new task ({newtask}) have been added")
def remove_task(tasks):
            if not todo_list:
                print("The list is empty")
            else:
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task}")
                try:
                    remtask = int(input("Please enter the number of task you want to remove: "))
                    
                    if 1 <= remtask <= len(todo_list):
                        todo_list.pop(remtask-1)
                        print("Task was removed!")
                    else:
                        print("The task was not found!")
                except ValueError:
                    print("Enter a vaild number!")
                    return
while True:
    command = input("--- ").lower()
    if command == "show":
         show_list(todo_list)
    elif command == "add":
         add_task(todo_list)
    elif command == "remove":
         remove_task(todo_list)
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("command was not found!")