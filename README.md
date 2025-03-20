# Task Manager

This is a simple command-line task management application written in Python. It allows users to create, update, delete, and list tasks with various attributes such as title, description, priority, and status.

## Features

- Create new tasks with title, description, priority, and status
- Update existing tasks (title, description, priority, status)
- Delete tasks
- List all tasks
- List tasks by status (done, pending, in progress)
- Persistent storage using JSON file

## Requirements

- Python 3.x
- shortuuid library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required library:
```
pip install shortuuid
```
3. Clone or download this repository to your local machine.

## Usage

Run the script using Python:
```
python main.py
```

Follow the on-screen prompts to interact with the task manager. Available commands:

- `create`: Add a new task
- `update`: Modify an existing task (requires task ID)
- `delete`: Remove a task (requires task ID)
- `list all`: Display all tasks
- `list done`: Show completed tasks
- `list pending`: Show pending tasks
- `list in progress`: Show tasks in progress
- `exit`: Quit the application

## Data Storage

Tasks are stored in a JSON file named `data_base.json` in the same directory as the script. This file is created automatically if it doesn't exist.

## Task Attributes

- `id`: Unique identifier for each task (automatically generated)
- `title`: Brief description of the task
- `description`: Detailed explanation of the task
- `priority`: Importance level (Critical, High, Medium, Low, Minimal)
- `status`: Current state of the task (pending, in progress, done)
- `createdAt`: Timestamp of task creation
- `updatedAt`: Timestamp of last update

## Notes

- The application uses a simple command-line interface.
- Input validation is implemented for task priorities and statuses.
- Task IDs are required for updating and deleting tasks.


# project URL
[https://github.com/marcosriani/trask-tracker/tree/main](https://roadmap.sh/projects/task-tracker)


