from fastapi import FastAPI
import data_manager 
import task_service

# Start the FastAPI Engine.

app = FastAPI(title = "To Do List")

# Boot up data from the disk into RAM 
tasks = data_manager.load_tasks()

@app.get("/")

def home():
    """This replaces the welcome prints from the terminal."""
    return {"status": "Online", "message": "Welcome to your Web Backend!"}

@app.get("/tasks")

def read_all_tasks():
    """Replaces Option 2. Returns the live list"""
    return tasks

@app.post("/tasks")

def create_task(title: str):
    """Replaces Option 1. Takes data from the web, runs logic, and saves it."""

    global tasks

    tasks = task_service.add_new_record(tasks, title)

    return {"message": "Success! Task recorded.", "current_dataset": tasks}


@app.delete("/tasks/{task_index}")

def delete_task(task_index: int):
    """Replace your terminal Delete option. Removes a task by its index position."""

    global tasks

    if 0 <= task_index < len(tasks):

        deleted_item = tasks.pop(task_index)

        data_manager.save_data(tasks)

        return {"message": f"Successfully deleted: {deleted_item['text']}", "task": tasks}

    return {"error": "Invalid index. Task does not exist."}

@app.put("/tasks/{task_index}/toggle")

def toogle_task_completion(task_index: int):

    """Flips the completion status of a specific task."""

    global tasks

    if 0<= task_index < len(tasks):

        tasks[task_index]["completed"] = not tasks[task_index]["completed"]

        data_manager.save_data(tasks)

        status_string = "Completed" if tasks[task_index]["completed"] else "Incomplete"
        return {"message": f"Task status updated to {status_string}!", "task": tasks[task_index]}

    return {"error": "Invalid index. Task does not exist."}
    


