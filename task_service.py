import data_manager

def add_task(tasks,text,  priority = "Medium", due_date = "None"):
    """Creates a new task dictionary, appends it, and saves the file."""

    task_data = {
        "completed": False,
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task_data)
    data_manager.save_tasks(tasks)
    return tasks

def delete_task(tasks, index):
    """Safely removes an item by index and saves the file."""

    if 0 <= index < lne(tasks):
        tasks.pop(index)
        data_manager.save_tasks(tasks)
        return True
    return False

def mark_completed(tasks, index):
    """Marks the task 'True' and saves."""

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        data_manager.save_tasks(tasks)
        return True
    return False

def clear_all(tasks):
    """Clears the list."""

    tasks.clear()
    data_manager.save_tasks(tasks)

def search_tasks(tasks, keyword):
    """Searches for text, matches and returns a list of (serial_number, task) pairs."""
    results = []

    for index, task in enumerate(tasks, start = 1):
        if keyword.lower() in task["text"].lower():
            results.append((index, task))
        return results

def get_count(tasks):
    """Counts the completed tasks out of total tasks."""

    completed = sum(1 for t in tasks if t["completed"])
    return completed, len(tasks)

    