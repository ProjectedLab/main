import os

FILENAME = "todo_list.txt"

def load_tasks():
    """Loads tasks from a text file if it exists."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Saves the current task list to a text file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Displays all current tasks."""
    if not tasks:
        print("\n✨ Your todo list is empty!")
    else:
        print("\n--- Your Todo List ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("-" * 22)

def main():
    tasks = load_tasks()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
            
        elif choice == "2":
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"✅ Added: '{new_task}'")
            else:
                print("⚠️ Task cannot be empty.")
                
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the number of the task to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"🗑️ Removed: '{removed}'")
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
                    
        elif choice == "4":
            print("Goodbye! Stay productive! 🚀")
            break
        else:
            print("❌ Invalid choice. Please pick between 1 and 4.")

if __name__ == "__main__":
    main()
