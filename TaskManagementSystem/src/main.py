from task_manager import TaskManager

def menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Toggle Complete")
    print("6. Exit")

def main():
    manager = TaskManager()
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Enter title: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(title, due)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            id = int(input("Enter task ID to edit: "))
            title = input("New title: ")
            due = input("New due date: ")
            manager.edit_task(id, title, due)
        elif choice == '4':
            id = int(input("Enter task ID to delete: "))
            manager.delete_task(id)
        elif choice == '5':
            id = int(input("Enter task ID to toggle complete: "))
            manager.toggle_complete(id)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
