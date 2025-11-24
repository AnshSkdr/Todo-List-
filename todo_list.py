#Name: ANSH SAIKHEDKAR 
#Registration Number: 25BCE10383
# Simple To-Do List Application with Pie Chart Visualization

tasks = []  # List to store all tasks

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"name": task, "done": False})
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "⬜"
        print(f"{i+1}. {status} {task['name']}")

def mark_done():
    view_tasks()
    if tasks:
        num = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("🎉 Task marked as done!")
        else:
            print("Invalid number!")

def show_pie_chart():
    if not tasks:
        print("No tasks to show in chart!")
        return
    
    completed = 0
    pending = 0
    
    for task in tasks:
        if task["done"]:
            completed += 1
        else:
            pending += 1
    
    # Data for pie chart
    labels = ['Completed', 'Pending']
    sizes = [completed, pending]
    colors = ['#90EE90', '#FFB6C1']  # light green and pink
    
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title("My To-Do List Progress")
    plt.axis('equal')  # Equal aspect ratio ensures pie is circular
    plt.show()

# Main menu
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
        print("Goodbye! Have a productive day! 👋")
        break
    else:
        print("Invalid choice! Please try again.")
