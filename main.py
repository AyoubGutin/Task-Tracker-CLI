import sys
import json
import os
from datetime import datetime

# const task path 
task_path = "tasks.json"

def load_tasks():
    """
    Description:
        Loads or creates JSON file and returns it
    """
    if os.path.exists(task_path):
        with open(task_path, "r") as file:
            content = file.read()
            if not content.strip(): # If it is empty
                return []
            return json.loads(content)
    else:
        with open(task_path, "x") as file:
            print("Made new file \n".)
            content = file.read()
            return json.loads(content)
        
def save_tasks(tasks):
    """
    Parameters:
        tasks: Json file that is loaded into python as a dictionary showing latest state of file

    Description:
        Overwrites JSON file with updated data, it is called everytime an action is made.
    """
    with open(task_path, "w") as file:
        json.dump(tasks, file, indent=4)


def add_tasks(description):
    """
    Parameters:
        description: Description of task 

    Description:
        Loads the JSON file by calling a function and store as dictionary tasks
        Gets unique ID and date of action.
        Appends tasks with relevant information
        Saves it by calling a function. 
    """
    tasks = load_tasks()
    task_id = int(len(tasks) + 1)
    created_at = datetime.now()
    tasks.append(
        {"id": task_id,
         "description": description,
         "status": "todo",
         "createdAt": str(created_at),
         "updatedAt": str(created_at)
        }
    )
    save_tasks(tasks)


def update_tasks(task_id, description):
    """
    Parameters:
        task_id: ID of task to be updated
        description: updated description of new task
    
    Description:
        Gets the relevant row of task to be updated and overwrite it
    """

    tasks = load_tasks()
    updated_at = datetime.now()
    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = description
            task[updated_at] = str(updated_at)
            save_tasks(tasks) # update list 
            return      
    print(f"Task not found (ID: {task_id})")

def delete_tasks(task_id):
    """
    Parameters:
        task_id: ID of task to be deleted
    """

    print("WiP")
    return 

# Handle commands from user
def main():
    # Get cli args
    args = sys.argv[1:]

    # if input is empty
    if not args:
        print("No command provided.")
        return
    
    command = args[0]

    if command == "add" and len(args) >= 2:
        description = " ".join(args[1:]) # Join remaining arguments as description
        add_tasks(description)
    
    elif command == "update" and len(args) >= 3:
        task_id = args[1]
        new_description = " ".join(args[2:])
        update_tasks(task_id, new_description)
    
    elif command == "delete" and len(args) == 2:
        task_id = args[1]
        delete_tasks(task_id)
        

if __name__ == "__main__":
    main()
