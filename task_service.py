import data_manager

def check_duplicate(tasks, task_text):
    """Checks if a task text already exists inside the list (case-insensitive)."""
    for t in tasks:
        if t["text"].lower() == task_text.lower():
            return True
    return False

def add_task(tasks, text, priority="Medium", due_date="None"):
    """Creates a new task dictionary, appends it, and saves the file."""
    task_data = {
        "text": text,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task_data)
    data_manager.save_tasks(tasks)
    return tasks

def delete_task(tasks, index):
    """Safely removes an item by index and saves the file."""
    if 0 <= index < len(tasks):
        tasks.pop(index)
        data_manager.save_tasks(tasks)
        return True
    return False

def edit_task(tasks, index, new_text):
    """Safely modifies the description text of an existing task and saves."""
    if 0 <= index < len(tasks):
        tasks[index]["text"] = new_text
        data_manager.save_tasks(tasks)
        return True
    return False

def mark_completed(tasks, index):
    """Safely updates a task's status to completed and saves."""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        data_manager.save_tasks(tasks)
        return True
    return False

def clear_all(tasks):
    """Empties the entire list and updates the storage file."""
    tasks.clear()
    data_manager.save_tasks(tasks)

def search_tasks(tasks, keyword):
    """Searches for text matches and returns a list of (serial_number, task) pairs."""
    results = []
    for index, task in enumerate(tasks, start=1):
        if keyword.lower() in task["text"].lower():
            results.append((index, task))
    return results

def get_counts(tasks):
    """Returns a tuple containing (completed_count, total_count)."""
    completed = sum(1 for t in tasks if t["completed"])
    return completed, len(tasks)