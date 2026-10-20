import data_manager
import task_service

# This is where the list is officially defined and populated from your database!
tasks = data_manager.load_tasks()

print('''
    ========================================
                 TODO APP MENU              
    ========================================
    1 for Adding task
    2 for viewing 
    3 for deleting  
    4 for editing 
    5 for marking task complete
    6 for deleting everything
    7 for searching tasks
    8 for task counts
    Anything other than this for exit. 
    ========================================''')

while True:
    print("\n")
    user_input = input("Enter your command: ").strip()

    # If the user types anything that isn't a clean number, exit gracefully
    if not user_input.isdigit():
        print("GoodBye and GodSpeed.")
        break
        
    n = int(user_input)

    # 1. Add Task
    if n == 1:
        text = input("Enter the task description: ").strip()
        
        # Call the duplicate check logic from our service file
        if task_service.check_duplicate(tasks, text):
            ans = input("Task already exists! Do you wish to add anyway? (Y/N): ").strip().upper()
            if ans != 'Y':
                print("Task not added.")
                continue # Skip the rest of this loop iteration
        
        priority = input("Enter priority (Low/Medium/High): ").strip().capitalize()
        if priority not in ["Low", "Medium", "High"]:
            priority = "Medium" # Fallback default if they mistype
            
        due_date = input("Enter due date: ").strip()
        
        # Pass the 'tasks' list to the service to append and save
        tasks = task_service.add_task(tasks, text, priority, due_date)
        print("Task added successfully.")

    # 2. View Tasks
    elif n == 2:
        print("\n--- CURRENT TASKS ---")
        if not tasks:
            print("[ Your list is empty! ]")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "[X]" if t["completed"] else "[ ]"
                print(f"{i}. {status} {t['text']} | Priority: {t['priority']} | Due: {t['due_date']}")

    # 3. Delete Task
    elif n == 3:
        if not tasks:
            print("Nothing to delete. Your list is empty!")
            continue
            
        d = int(input("Enter the serial number to delete: "))
        idx = d - 1 # Convert user counting to Python index
        
        if 0 <= idx < len(tasks):
            ans = input(f"Are you sure you want to delete '{tasks[idx]['text']}'? (Y/N): ").strip().upper()
            if ans == 'Y':
                task_service.delete_task(tasks, idx)
                print("Task deleted.")
        else:
            print("Invalid serial number.")

    # 4. Edit Task
    elif n == 4:
        if not tasks:
            print("Nothing to edit. Your list is empty!")
            continue
            
        en = int(input("Enter the serial number of the task to edit: "))
        idx = en - 1
        
        if 0 <= idx < len(tasks):
            new_text = input("Enter the new task details: ").strip()
            task_service.edit_task(tasks, idx, new_text)
            print("Task updated.")
        else:
            print("Invalid serial number.")

    # 5. Mark Completed
    elif n == 5:
        if not tasks:
            print("No tasks available to mark.")
            continue
            
        num = int(input("Enter the task number to mark completed: "))
        if task_service.mark_completed(tasks, num - 1):
            print("Task marked completed!")
        else:
            print("Invalid serial number.")

    # 6. Delete Everything
    elif n == 6:
        ans = input("⚠️ CRITICAL: Are you sure you want to delete ALL records? (Y/N): ").strip().upper()
        if ans == 'Y':
            task_service.clear_all(tasks)
            print("All tasks permanently cleared.")

    # 7. Search Keyword
    elif n == 7:
        word = input("Enter the keyword to find: ").strip()
        found = task_service.search_tasks(tasks, word)
        if not found:
            print("No matching tasks found.")
        else:
            print("\n--- SEARCH RESULTS ---")
            for idx, task in found:
                print(f"Match at Serial #{idx}: {task['text']}")

    # 8. Count Completed
    elif n == 8:
        completed, total = task_service.get_counts(tasks)
        print(f"Metrics: {completed} out of {total} tasks completed.")
        
    else:
        print("GoodBye and GodSpeed.")
        break
