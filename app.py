from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field 
import data_manager
import task_service
import os
import uvicorn

app = FastAPI(title="To Do List")

# Enable CORS so frontend apps can safely communicate with this backend
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

tasks = data_manager.load_tasks()

# ==========================================
# PYDANTIC SCHEMA DEFINITION
# ==========================================
class TaskCreateSchema(BaseModel):
    """
    Defines the exact structural contract for creating a new task.
    FastAPI will automatically validate that incoming payloads match this shape.
    """
    title: str = Field(..., min_length=1, max_length=100, description="The descriptive title of the task.")
    priority: str = Field(default="Medium", description="Can be High, Medium, or Low.")
    due_date: str = Field(default="None", description="Optional deadline date string.")

# ==========================================
# ENDPOINTS
# ==========================================

@app.get("/")
def home():
    return {"status": "Online", "message": "Welcome to your Web Backend!"}

@app.get("/tasks")
def read_all_tasks():
    return tasks

@app.post("/tasks")
def create_task(task_payload: TaskCreateSchema):
    """
    Receives a structured JSON request body validated by TaskCreateSchema.
    """
    global tasks
    
    # Convert Pydantic object back into a standard Python dictionary
    task_dict = task_payload.model_dump()
    
    # Prepare the standard item structure our app expects
    new_record = {
        "text": task_dict["title"],
        "completed": False,
        "priority": task_dict["priority"],
        "due_date": task_dict["due_date"]
    }
    
    tasks.append(new_record)
    data_manager.save_tasks(tasks)
    
    return {"message": "Success! Task recorded.", "current_dataset": tasks}


# DELETE PARTICULAR TASK

@app.delete("/tasks/{task_index}")
def delete_task(task_index: int):
    global tasks
    # Proper HTTP 404 Error Handling if index is out of bounds
    if task_index < 0 or task_index >= len(tasks):
        raise HTTPException(status_code=404, detail="Task index out of bounds.")
        
    deleted_item = tasks.pop(task_index)
    data_manager.save_tasks(tasks)
    return {"message": f"Successfully deleted: {deleted_item['text']}"}

# UPDATE COMPLETION OF A TASK
@app.put("/tasks/{task_index}/toggle")
def toggle_task_completion(task_index: int):
    global tasks
    # Proper HTTP 404 Error Handling if index is out of bounds
    if task_index < 0 or task_index >= len(tasks):
        raise HTTPException(status_code=404, detail="Task index out of bounds.")
        
    tasks[task_index]["completed"] = not tasks[task_index]["completed"]
    data_manager.save_tasks(tasks)
    
    status_string = "Completed" if tasks[task_index]["completed"] else "Incomplete"
    return {"message": f"Task status updated to {status_string}!", "task": tasks[task_index]}

# DELETE ALL THE TASKS

@app.delete("/tasks")
def delete_everything():

    tasks.clear()
    data_manager.save_tasks(tasks)
    return {"message": f"All Tasks Deleted!!"}

# SEARCH TASK USING KEYWORD

@app.get("/tasks/search/{snippet}")
def search_snippet(snippet: str):
    global tasks
    found = task_service.search_task(tasks, snippet)
    return {
        "message": f"Search Successfull.",
        "query": snippet,
        "results": found
    }

# TO COUNT THE COMPLETED TASKS OUT OF TOTAL

@app.get("/tasks/count")
def count_complete():
    global tasks
    count, total = task_service.get_counts(tasks)
    return{
        "Message": f"{count} completed out of {total}.", 
    }



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)