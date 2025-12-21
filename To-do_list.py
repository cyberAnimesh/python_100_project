tasks = []

def show_menu():
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({'task': task, 'done': False})
        print("Task added")

    elif choice == '2':
        if not tasks:
            print("No tasks found")
        else:
            for i, t in enumerate(tasks):
                status = "Done" if t["done"] else "Not Done"
                print(f"{i+1}. {t['task']} [{status}]")

    elif choice == '3':
        num = int(input("Enter task number to mark done: "))
        tasks[num-1]["done"] = True
        print("Task marked as done")

    elif choice == '4':
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted")

    elif choice == '5':
        print("Exit")
        break

    else:
        print("Invalid choice")
