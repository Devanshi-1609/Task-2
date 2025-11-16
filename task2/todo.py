import os

DATA_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from DATA_FILE and return a list of (done_bool, text)."""
    tasks = []
    if not os.path.exists(DATA_FILE):
        return tasks
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
 
            parts = line.split("|", 1)
            if len(parts) == 2:
                flag, text = parts
                done = flag == "1"
                tasks.append((done, text))
    return tasks

def save_tasks(tasks):
  
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for done, text in tasks:
            flag = "1" if done else "0"
            f.write(f"{flag}|{text}\n")


def view_tasks(tasks):
  
    if not tasks:
        print("\nNo tasks yet. Add one!\n")
        return
    print("\nYour To-Do List:")
    print("----------------")
    for idx, (done, text) in enumerate(tasks, start=1):
        status = "[x]" if done else "[ ]"
        print(f"{idx:2d}. {status} {text}")
    print()

def add_task(tasks):
    text = input("Enter new task: ").strip()
    if not text:
        print("Task cannot be empty.")
        return
    tasks.append((False, text))
    save_tasks(tasks)
    print("Task added.")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks(tasks)
    try:
        n = int(input("Enter task number to remove: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if 1 <= n <= len(tasks):
        removed = tasks.pop(n - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed[1]}")
    else:
        print("Task number out of range.")

def toggle_task_done(tasks):
   
    if not tasks:
        print("No tasks to update.")
        return
    view_tasks(tasks)
    try:
        n = int(input("Enter task number to toggle done/undone: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if 1 <= n <= len(tasks):
        done, text = tasks[n - 1]
        tasks[n - 1] = (not done, text)
        save_tasks(tasks)
        state = "Done" if not done else "Not done"
        print(f"Task updated: {text} -> {state}")
    else:
        print("Task number out of range.")

def clear_all(tasks):
    confirm = input("Are you sure you want to delete ALL tasks? (y/n): ").strip().lower()
    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Cancelled.")


def print_header():
    print("=" * 40)
    print("        SIMPLE TODO LIST (CLI)       ")
    print("=" * 40)

def show_menu():
    print("\nMenu:")
    print("  1. View tasks")
    print("  2. Add task")
    print("  3. Remove task")
    print("  4. Toggle done/undone")
    print("  5. Clear all tasks")
    print("  6. Exit")

def main():
    tasks = load_tasks()
    while True:
        print_header()
        show_menu()
        choice = input("Enter choice (1-6): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            toggle_task_done(tasks)
        elif choice == "5":
            clear_all(tasks)
        elif choice == "6":
            print("Goodbye! Your tasks are saved in 'tasks.txt'.")
            break
        else:
            print("Invalid choice. Please choose a number 1-6.")

if __name__ == "__main__":
    main()
