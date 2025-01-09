import os

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['task']} [{status}]")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Marked task '{self.tasks[task_index]['task']}' as completed.")
        else:
            print("Invalid task index.")

    def clear_tasks(self):
        self.tasks = []
        print("Cleared all tasks.")

    def edit_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            old_task = self.tasks[task_index]["task"]
            self.tasks[task_index]["task"] = new_task
            print(f"Edited task '{old_task}' to '{new_task}'.")
        else:
            print("Invalid task index.")

    def save_tasks(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['completed']}\n")
        print(f"Tasks saved to '{filename}'.")

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.tasks = []
                for line in file:
                    task, completed = line.strip().split("|")
                    self.tasks.append({"task": task, "completed": completed == "True"})
            print(f"Tasks loaded from '{filename}'.")
        else:
            print(f"File '{filename}' does not exist.")

def main():
    manager = ToDoListManager()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear Tasks")
        print("5. Edit Task")
        print("6. Save Tasks")
        print("7. Load Tasks")
        print("8. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            manager.add_task(task)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            manager.mark_task_completed(task_index)
        elif choice == "4":
            manager.clear_tasks()
        elif choice == "5":
            task_index = int(input("Enter the task number to edit: ")) - 1
            new_task = input("Enter the new task: ")
            manager.edit_task(task_index, new_task)
        elif choice == "6":
            filename = input("Enter the filename to save tasks: ")
            manager.save_tasks(filename)
        elif choice == "7":
            filename = input("Enter the filename to load tasks: ")
            manager.load_tasks(filename)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
