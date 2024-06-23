# Description: A simple To-Do List application that allows users to add tasks, view tasks, mark tasks as complete, and delete tasks.

import os
import sys
import time
import datetime


to_do_list = []
tasks = {}

def add_task():
    title = input("Enter the title of the task: ")
    due_date = input("Does this task have a due date? Enter the due date of the task (mm/dd/yyyy) or simply type no: ")
    priority = input("Do you want to assign a priority to this task? Enter the priority of the task (High, Medium, Low) or simply type no: ")
    task = {
        "title": title,
        "status": "Incomplete",
        "due_date": due_date,
        "priority": priority
    }
    to_do_list.append(task)
    print("Task successfully added to your To-Do List!")

def view_tasks():
    if len(to_do_list) == 0:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. Title: {task['title']}, Status: {task['status']}, Due Date: {task['due_date']}, Priority: {task['priority']}")
    time.sleep(20)


def mark_complete():
    view_tasks()
    task_index = input("Enter the index of the task you want to mark as complete: ")
    try:
        task_index = int(task_index)
        if task_index < 1 or task_index > len(to_do_list):
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid index.")
        time.sleep(20)
    else:
        to_do_list[task_index - 1]["status"] = "Complete"
        print("Task marked as complete.")
        time.sleep(20)

def delete_task():
    view_tasks()
    task_index = input("Enter the index of the task you want to delete: ")
    try:
        task_index = int(task_index)
        if task_index < 1 or task_index > len(to_do_list):
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid index.")
        time.sleep(15)
    else:
        del to_do_list[task_index - 1]
        print("Task deleted successfully.")
        time.sleep(20)

def edit_due_date():
    view_tasks()
    task_index = input("Enter the index of the task you want to edit the due date: ")
    try:
        task_index = int(task_index)
        if task_index < 1 or task_index > len(to_do_list):
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid index.")
        time.sleep(15)
    else:
        new_due_date = input("Enter the new due date of the task (mm/dd/yyyy): ")
        to_do_list[task_index - 1]["due_date"] = new_due_date
        print("Due date updated successfully.")
        time.sleep(20)

def edit_priority():
    view_tasks()
    task_index = input("Enter the index of the task you want to edit the priority: ")
    try:
        task_index = int(task_index)
        if task_index < 1 or task_index > len(to_do_list):
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid index.")
        time.sleep(15)
    else:
        new_priority = input("Enter the new priority of the task (High, Medium, Low): ")
        to_do_list[task_index - 1]["priority"] = new_priority
        print("Priority updated successfully.")
        time.sleep(20)

def quit_app():
    print("Quitting the application...")
    print("Thank you for using the To-Do List App!")
    sys.exit()

def main():
    while True:
        os.system("clear")
        print("Welcome to the To-Do List App!\n")
        print("Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Edit due date")
        print("6. Edit priority")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            edit_due_date()
        elif choice == "6":
            edit_priority()
        elif choice == "7":
            quit_app()
        else:
            print("Invalid choice. Please enter a valid option.")
            time.sleep(10)

if __name__ == "__main__":
    main()

# End of To-Do List Application


