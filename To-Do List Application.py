# Description: A simple To-Do List application that allows users to add tasks, view tasks, mark tasks as complete, and delete tasks.

to_do_list = []

def add_task():
    title = input("Enter the title of the task: ")
    task = {"title": title, "status": "Incomplete"}
    to_do_list.append(task)
    print("Task successfully added to your To-Do List!")

def view_tasks():

    if len(to_do_list) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(to_do_list):
            print(f"{index + 1}. {task['title']} - {task['status']}")

def mark_complete():
    view_tasks()
    task_number = int(input("Enter the task number to mark as complete: "))
    if task_number > 0 and task_number <= len(to_do_list):
        to_do_list[task_number - 1]["status"] = "Complete"
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if task_number > 0 and task_number <= len(to_do_list):
        del to_do_list[task_number - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    print("Welcome to the To-Do List Application!")
    print("This application allows you to add tasks, view tasks, mark tasks as complete, and delete tasks.")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("What do you need to do to you To-Do List? Enter the number choice: ")
        try:
            int(choice) # Check if the input is a number
        except:
            print("Invalid choice. Please try again.")
            continue
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


