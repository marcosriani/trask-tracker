import datetime
import json
import os
import shortuuid

FILE_NAME = "data_base.json"
VALID_STATUSES = ["pending", "in progress", "done"]
VALID_PRIORITIES = ["critical", "high", "medium", "low", "minimal"]

task_manager_on = True

if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME) as json_file:
            task_data = json.load(json_file)
    except (json.JSONDecodeError, IOError):
        print(f"Error reading {FILE_NAME}. The file may be corrupted.")
        task_data = []
else:
    task_data = []

def create_task():
    task_title = input("Task title: ")
    task_description = input("Task description: ")

    while True:
        task_priority = input("Task priority:\n('Critical', 'High', 'Medium', 'Low', 'Minimal')\n").lower()
        if task_priority in VALID_PRIORITIES:
            break
        else:
            print("Invalid task priority. Please choose from 'Critical', 'High', 'Medium', 'Low', 'Minimal'")

    new_task = {
        "id": shortuuid.uuid(),
        "title": task_title,
        "description": task_description,
        "priority": task_priority,
        "status": "pending",
        "createdAt": str(datetime.datetime.now()),
        "updatedAt": str(datetime.datetime.now())
    }

    task_data.append(new_task)
    with open(FILE_NAME, "w") as file:
        json.dump(task_data, file, indent=4)

    print_formated_data(new_task)
    print("Task created successfully!")


def print_formated_data(task):
    print("------------ * -----------")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Priority: {task['priority']}")
    print(f"Status: {task['status']}")
    created_date = datetime.datetime.strptime(task['createdAt'], "%Y-%m-%d %H:%M:%S.%f")
    updated_date = datetime.datetime.strptime(task['updatedAt'], "%Y-%m-%d %H:%M:%S.%f")
    print(f"Created at: {created_date.strftime('%A, %B %d, %Y at %I:%M %p')}")
    print(f"Updated at: {updated_date.strftime('%A, %B %d, %Y at %I:%M %p')}")
    print(f"ID: {task['id']}")
    print("------------ * -----------")

def list_all_tasks():
    for task in task_data:
        print_formated_data(task)

def list_all_tasks_by_status(status):
    for task in task_data:
        if task["status"] == status:
            print_formated_data(task)

def find_task_by_id(task_id):
    for task in task_data:
        if task["id"] == task_id:
            return task
    return None

def update_task(task_id):
    task = find_task_by_id(task_id)
    if not task:
        print("Task not found.")
        return

    print_formated_data(task)
    updated = False

    update_title = input("Do you want to update task title? (Y/N): ").lower()
    if update_title == "y":
        task["title"] = input("Update task title: ")
        updated = True

    update_description = input("Do you want to update task description? (Y/N): ").lower()
    if update_description == "y":
        task["description"] = input("Update task description: ")
        updated = True

    update_priority = input("Do you want to update task priority? (Y/N): ").lower()
    if update_priority == "y":
        new_priority = input("Update task priority: ").lower()
        if new_priority in VALID_PRIORITIES:
            task["priority"] = new_priority
            updated = True
        else:
            print("Invalid priority. Priority not updated.")

    update_status = input("Do you want to update task status? (Y/N): ").lower()
    if update_status == "y":
        new_status = input("Update task status (pending/in progress/done): ").lower()
        if new_status in VALID_STATUSES:
            task["status"] = new_status
            updated = True
        else:
            print("Invalid status. Status not updated.")

    if updated:
        task["updatedAt"] = str(datetime.datetime.now())
        with open(FILE_NAME, "w") as file_data:
            json.dump(task_data, file_data, indent=4)
        print("Update successful!")
    else:
        print("No changes made.")

    print_formated_data(task)

def delete_task(task_id):
    task = find_task_by_id(task_id)
    if not task:
        print("Task not found.")
        return

    print_formated_data(task)
    task_data.remove(task)
    with open(FILE_NAME, "w") as file_data:
        json.dump(task_data, file_data, indent=4)
    print("Delete successful!")

options = {
    "create": create_task,
    "update": update_task,
    "delete": delete_task,
    "list all": list_all_tasks,
    "list done": lambda: list_all_tasks_by_status("done"),
    "list pending": lambda: list_all_tasks_by_status("pending"),
    "list in progress": lambda: list_all_tasks_by_status("in progress")
}

while task_manager_on:
    user_choice = input("What would you like to do?\nType one of the options to continue: 'Create', 'Update', 'Delete', 'List all', 'List done', 'List pending', 'List in progress', 'Exit': \n").lower()

    if user_choice == "exit":
        print("Exiting program, goodbye!")
        task_manager_on = False
    elif user_choice in options:
        if user_choice in ["update", "delete"]:
            user_task_id = input("Enter the task ID:\n")
            options[user_choice](user_task_id)
        else:
            options[user_choice]()
    else:
        print("Invalid choice. Please try again.")