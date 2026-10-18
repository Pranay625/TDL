tasks = []


while True:
    print("\n\n")
    n = int(input(
    '''
    Enter the command:\n
    1 for Adding task
    2 for viewing 
    3 for deleting  
    4 for editing 
    Anything other than this for exit. '''))

    if n == 1:
        add = input("Enter the task: ")
        tasks.append(add)
        print(f"Here is the updated list;\n{tasks}.")

    elif n == 2:
        print(tasks)

    elif n == 3:
        d = int(input("Enter the position to be deleted: "))
        tasks.delete(d)

    elif n == 4:
        e = input("Enter the new task")
        en = int(input("Enter the serial number of the task."))
        tasks[en] = e
        print(f"Updated list {tasks}")
    else:
        print("GoodBye and GodSpeed.")
        break


