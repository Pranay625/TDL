import data_manager
import task_service



tasks = []
print(
'''
    Enter the command:\n
    1 for Adding task
    2 for viewing 
    3 for deleting  
    4 for editing 
    5 for marking
    6 for delete everything.
    7 for finding the index
    8 for the count
    Anything other than this for exit. '''
)
while True:
    print("\n")
    user_input = input("Enter your command:")

    if user_input.isdigit():
        n = int(user_input)

    else:
        print("Please Enter a valid number!!")

    if n == 1:
        add = input("Enter the task, priority, and due date: ")

        if add in tasks:
            ans = input("Task already exists? Do you wish add anyway?")
            if ans == 'Y':
                task_data = {"text": add, "completed": False}
                tasks.append(task_data)
            else:
                print("Task not added.")
        else:
            task_data = {"text": add, "completed": False}
            tasks.append(task_data)


        print(f"Here is the updated list;\n{tasks}.")

    elif n == 2:
        print("--Current Tasks--")

        if not tasks:
            print("No tasks!!")
        else:

            for serial_num, task in enumerate(tasks, start = 1):

                status = "[X]" if task["completed"] else "[ ]"
                print(f"{serial_num}. {status}. {task['text']}")


    elif n == 3:
        d = int(input("Enter the position to be deleted: "))
        ans = input(f"Are you sure you want to delete {task[d-1]}? If yes type 'Y'\n")
        if ans == 'Y':
            tasks.pop(d)
        else:
            print("Task not deleted.")

    elif n == 4:
        e = input("Enter the new task")
        en = int(input("Enter the serial number of the task."))

        index_to_edit = en-1

        if 0 <= index_to_edit < len(tasks):
            tasks[index_to_edit] = e
            print(f"Updated List: {tasks}")
        else:
            print("Invalid Serial number.")

    elif n == 5:
        num = int(input("Enter the task number to mark:"))
        index = num - 1

        if 0 <= index < len(tasks):

            tasks[index]["completed"] = True
            print("Task marked completed!")
        else:
            print("Invalid serial number.")

    elif n == 6:
        ans = input("Are you sure you want to delete all the records??")
        if ans == 'Y':
            tasks.clear(), task_data.clear()

    elif n ==7:
        word = input("Enter the keyword:")

        indices = [index for index, item in enumerate(tasks) if word.lower() in str(item)]
        print(indices)

    elif n == 8:

        completed_count = sum(1 for task in tasks if task["completed"])
        print(f"Completed: {completed_count} out of {len(tasks)}")

    else:
        print("GoodBye and GodSpeed.")
        break


