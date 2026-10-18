
tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: "))
    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("Task deleted!")
    else:
        print("Invalid task number.")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
