# Simple To-Do List with Pie Chart (No Emojis)

tasks = []  # List to store tasks

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"name": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "[Done]" if task["done"] else "[Pending]"
        print(f"{i+1}. {status} {task['name']}")

def mark_done():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to mark as done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def show_pie_chart():
    if not tasks:
        print("No tasks to show in chart!")
        return
    
    completed = sum(1 for task in tasks if task["done"])
    pending = len(tasks) - completed
    
    labels = ['Completed', 'Pending']
    sizes = [completed, pending]
    colors = ['lightgreen', 'lightcoral']
    
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title("To-Do List Progress")
    plt.axis('equal')
    plt.show()

# Main menu loop
while True:
    print("\n" + "="*30)
    print("   SIMPLE TO-DO LIST")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Show Pie Chart")
    print("5. Exit")
    
    choice = input("\nChoose an option (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        show_pie_chart()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
