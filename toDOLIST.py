import tkinter as tk
from tkinter import messagebox


TASK_FILE = "tasks.txt"

app = tk.Tk()
app.title("To-Do List App")
app.geometry("400x500")


tasks = []


def load_tasks():
    """Load tasks from the file when the app starts."""
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  

def save_tasks():
    """Save tasks to the file when the app closes."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    """Add a new task to the list."""
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    """Delete the selected task."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

def mark_task_complete():
    """Mark the selected task as completed."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        if "✔" not in tasks[selected_task_index]:
            tasks[selected_task_index] += " ✔"
            update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

def update_task_list():
    """Update the task list display."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        if "✔" in task:
            task_listbox.insert(tk.END, task)
            task_listbox.itemconfig(tk.END, fg="green")   
        else:
            task_listbox.insert(tk.END, task)


task_entry = tk.Entry(app, font=("Arial", 14))
task_entry.pack(pady=10)


add_task_button = tk.Button(app, text="Add Task", command=add_task, font=("Arial", 14))
add_task_button.pack(pady=5)

task_listbox = tk.Listbox(app, font=("Arial", 14), height=15)
task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)


buttons_frame = tk.Frame(app)
buttons_frame.pack(pady=10)

delete_button = tk.Button(buttons_frame, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(buttons_frame, text="Mark Complete", command=mark_task_complete, font=("Arial", 12))
complete_button.pack(side=tk.LEFT, padx=10)


load_tasks()
update_task_list()


app.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), app.destroy()))


app.mainloop()
