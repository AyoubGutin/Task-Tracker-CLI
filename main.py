import argparse
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
        with open(task_path, "w") as file:
            print("Made new file \n")
            json.dump([], file)
            return []
        
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
           # save_tasks(tasks) # update list 
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

    # create an ArgumentParser object to define and parse command line arguments
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    # Create collection of subcommands to the parser object
        # dest="command" specifies name of chosen subcommand 
        # help provides a help message for subcommand section
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", nargs="+", help="Task description") # one or more arguments

    # Update Command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("task_id", type=int, nargs=1, help="ID of task to update") # one argument
    update_parser.add_argument("description", nargs="+", help="New task description") # one or more arguments

    # Add the rest after testing 

    # Parse arguments
    args = parser.parse_args()

    
    # Conditional statements to select right function
    if args.command == "add":
        description = " ".join(args.description)
        add_tasks(description)
    
    elif args.command == "update":
        task_id = int(args.task_id[0])
        description = " ".join(args.description)
        update_tasks(task_id, description)

    else:
        parser.print_help()
    



        

if __name__ == "__main__":
    main()
