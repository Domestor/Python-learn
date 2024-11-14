task_list = []


def add_task():
    task = input("Write the task you want to add to the list: ")
    task_list.append(task)
    print("Task successfully added to your tasks-list!")


def view_tasks():
    print('Tasks:')
    if task_list:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in your list")


def mark_task_completed():
    view_tasks()
    try:
        choose = int(input("Enter the number of the task you want to mark as completed: "))
        if task_list:
            if 1 <= choose <= len(task_list):
                task_list[choose - 1] += " ✅"
                print(f"You have marked the task {choose} as completed!")
            else:
                print("Invalid number! Please enter a number between 1 and", len(task_list))
    except ValueError:
        print("Please enter a valid number")


def delete_task():
    view_tasks()
    try:
        choose = int(input("Enter the number of the task you want to delete: "))
        if task_list:
            if 1 <= choose <= len(task_list):
                del task_list[choose - 1]
                print(f"Task number {choose} deleted from your list")
            else: 
                print(f"Invalid number! Please enter a number between 1 and", len(task_list))
    except ValueError:
        print("Please enter a valid number")


actions = {
    '1': add_task,
    '2': view_tasks,
    '3': mark_task_completed,
    '4': delete_task
}

while True:
    print("1. add new task")
    print("2. view your tasks list")
    print("3. mark tasks completed")
    print("4. delete task from your list")
    print("5. leave")

    choice = input("Choose action: ")

    if choice == 5:
        print("bye")
        break
    elif choice in actions:
        actions[choice]()
    else:
        print("Syntax Error. undefind action.")