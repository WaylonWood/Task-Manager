import json
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)

# File paths for storing task and completed task data
TASKS_FILE = "tasks.json"
COMPLETED_FILE = "completed.json"

# Load tasks from a JSON file. Return empty list if file doesn't exist or is corrupted.
def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

# Save tasks to a JSON file with indentation for readability
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Main CLI loop
while True:
    try:
        # Display menu options
        print("Welcome to the Task Manager!") 
        print()
        print(" 1. Add Task")
        print(" 2. View Tasks")
        print(" 3. Complete Task")
        print(" 4. Remove Task")
        print(" 5. Complete Subtask")
        print(" 6. Remove Subtask")
        print(" 7. View Completed Tasks")
        print(" 8. Exit")

        choice = int(input("Please select an option: "))

        # Add a new task with optional subtasks
        if choice == 1:
            task_name = input("Enter the task: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            priority = input("Enter priority (high/medium/low): ").lower()
            
            # Collect subtasks until user presses Enter with no input
            subtasks = []
            while True:
                subtask = input("Enter a subtask (or press Enter to finish): ")
                if subtask == "":
                    break
                subtasks.append({"task": subtask, "completed": False})
            
            # Create task object
            task = {
                "task": task_name,
                "due": due_date,
                "priority": priority,
                "completed": False,
                "subtasks": subtasks
            }

            # Append new task to task list and save
            tasks = load_tasks(TASKS_FILE)
            tasks.append(task)
            save_tasks(TASKS_FILE, tasks)
            print(f"Task '{task_name}' added.")

        # View all current tasks with color-coded due dates
        elif choice == 2:
            tasks = load_tasks(TASKS_FILE)
            if tasks:
                print("Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    due_date_str = task.get("due", "")
                    try:
                        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                        today = datetime.today().date()
                        color = Fore.YELLOW
                        if due_date < today:
                            color = Fore.RED  # Overdue
                        elif due_date == today:
                            color = Fore.MAGENTA  # Due today
                    except ValueError:
                        color = Fore.YELLOW  # Invalid or missing date
                    print(color + f"{idx}. {task['task']} | Due: {due_date_str} | Priority: {task['priority']}")
            else:
                print("No tasks found.")

        # Mark a main task as complete and move it to completed list
        elif choice == 3:
            tasks = load_tasks(TASKS_FILE)
            completed_tasks = load_tasks(COMPLETED_FILE)
            if tasks:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task['task']}")
                task_num = int(input("Enter the task number to mark as complete: "))
                if 1 <= task_num <= len(tasks):
                    completed_task = tasks.pop(task_num - 1)
                    completed_task["completed"] = True
                    completed_tasks.append(completed_task)
                    save_tasks(TASKS_FILE, tasks)
                    save_tasks(COMPLETED_FILE, completed_tasks)
                    print(f"Task '{completed_task['task']}' marked as complete.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks found.")

        # Remove a main task by number
        elif choice == 4:
            tasks = load_tasks(TASKS_FILE)
            if tasks:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task['task']}")
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_tasks(TASKS_FILE, tasks)
                    print(f"Task '{removed_task['task']}' removed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks found.")

        # Mark a subtask as complete
        elif choice == 5:
            tasks = load_tasks(TASKS_FILE)
            if not tasks:
                print("No tasks available.")
                continue

            # Select a main task
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task['task']}")
            task_num = int(input("Enter the task number: "))
            if not (1 <= task_num <= len(tasks)):
                print("Invalid task number.")
                continue

            selected_task = tasks[task_num - 1]
            subtasks = selected_task.get("subtasks", [])
            if not subtasks:
                print("This task has no subtasks.")
                continue

            # List and select subtask to complete
            for idx, sub in enumerate(subtasks, start=1):
                status = "✔" if sub["completed"] else "✘"
                print(f"  {idx}. [{status}] {sub['task']}")
            subtask_num = int(input("Enter the subtask number to mark as complete: "))
            if not (1 <= subtask_num <= len(subtasks)):
                print("Invalid subtask number.")
                continue

            subtasks[subtask_num - 1]["completed"] = True
            save_tasks(TASKS_FILE, tasks)
            print(f"Subtask '{subtasks[subtask_num - 1]['task']}' marked as complete.")

        # Remove a subtask
        elif choice == 6:
            tasks = load_tasks(TASKS_FILE)
            if not tasks:
                print("No tasks available.")
                continue

            # Select a main task
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task['task']}")
            task_num = int(input("Enter the task number: "))
            if not (1 <= task_num <= len(tasks)):
                print("Invalid task number.")
                continue

            selected_task = tasks[task_num - 1]
            subtasks = selected_task.get("subtasks", [])
            if not subtasks:
                print("This task has no subtasks.")
                continue

            # Select and remove a subtask
            for idx, sub in enumerate(subtasks, start=1):
                status = "✔" if sub["completed"] else "✘"
                print(f"  {idx}. [{status}] {sub['task']}")
            subtask_num = int(input("Enter the subtask number to remove: "))
            if not (1 <= subtask_num <= len(subtasks)):
                print("Invalid subtask number.")
                continue

            removed = subtasks.pop(subtask_num - 1)
            save_tasks(TASKS_FILE, tasks)
            print(f"Subtask '{removed['task']}' removed.")

        # Display completed tasks from completed.json
        elif choice == 7:
            completed_tasks = load_tasks(COMPLETED_FILE)
            if completed_tasks:
                print("Completed Tasks:")
                for idx, task in enumerate(completed_tasks, start=1):
                    print(Fore.GREEN + f"{idx}. {task['task']} | Due: {task['due']} | Priority: {task['priority']}")
            else:
                print("No completed tasks found.")

        # Exit the program
        elif choice == 8:
            print("Exiting the task manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Handle invalid input that isn't a number
    except ValueError:
        print("Invalid input. Please enter a number.")
    # Catch-all for unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    # Pause before showing the menu again
    print()
    input("Press Enter to continue...")
    print()
