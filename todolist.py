'''
Console-based to-do list. Users add, remove and view tasks
To function, create a file named 'todolist.txt' in the directory 
'''

def main():
    while True:
        operation = choice()
        if operation == 'add':
            add()
        elif operation == 'remove':
            remove()
        elif operation == 'view':
            view()
        elif operation == 'quit':
            quit()


def choice():
    while True:
        print("This is a to-do list.")
        choice = input("What would you like to do? Please enter 'add, 'remove', 'view' or 'quit' to exit: ")
        if choice.lower() == 'add':
            return 'add'
        elif choice.lower() == 'remove':
            return 'remove'
        elif choice.lower() == 'view':
            return 'view'
        elif choice.lower() == 'quit':
            return 'quit'
        else:
            print("Invalid input. Try again.")
            continue


def add():
    task = input("Enter task to add: ")
    
    filename = "todolist.txt"
    try:
        with open(filename, 'a') as file:
            file.write(task)
            file.write('\n')
    except Exception as ex:
        print("An error occurred:")
        print(ex)


def remove():
    task = input("Enter task to remove: ")
    filename = 'todolist.txt'
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                if line.strip() != task:
                    file.write(line)
    except Exception as ex:
        print("Error:")
        print(ex)


def view():
    filename = 'todolist.txt'

    try:
        with open(filename) as file:
                content = file.readlines()
    except Exception as ex:
        print("Error:")
        print(ex)
    else:
        print("Open tasks:\n")
        for task in content:
            print(task.strip())
        print()


main()