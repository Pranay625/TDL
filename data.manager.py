import json

FILENAME = "database.json"

def load_tasks():
    """Reads tasks from the JSON file. If the file doesn't exist yet, it returns an empty list."""
    try:

    # open the file in Read ('r') mode
        with open(FILENAME, "r") as file:
            #convert JSON data from file back into a Python list.
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file is not found or empty, return a fresh empty list
        return[]

def save_tasks(tasks):
    """Takes your active tasks list and writes it perfectly into the JSOn file."""
    # Open the file in Write ('w') mode (creates it if missing)

    with open(FILENAME, "w") as file:

        json.dump(tasks, file, indent = 4)

        
    
