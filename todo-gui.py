import tkinter as tk
from tkinter import messagebox
import os


TASKS_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the tasks.txt file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    """Saves the current list of tasks to the tasks.txt file."""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def populate_listbox():
    """Clears the listbox and re-populates it with current tasks."""
    list_tasks.delete(0, tk.END)
    for task in tasks:
        list_tasks.insert(tk.END, task)

def add_task_gui():
    """Adds a task from the entry box to the list."""
    task = entry_task.get()
    if task:  
        tasks.append(task)
        save_tasks(tasks)
        populate_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task_gui():
    """Deletes the currently selected task from the list."""
    try:
        selected_task_index = list_tasks.curselection()[0]
        tasks.pop(selected_task_index)
        save_tasks(tasks)
        populate_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def update_task_gui():
    """Updates the currently selected task with the text from the entry box."""
    try:
        selected_task_index = list_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task:
            tasks[selected_task_index] = new_task
            save_tasks(tasks)
            populate_listbox()
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "The task description cannot be empty.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

def load_task_for_update(event):
    """
    Called when a user clicks on a task in the listbox.
    It loads the task's text into the entry box for editing.
    """
    try:
        selected_task = list_tasks.get(list_tasks.curselection())
        entry_task.delete(0, tk.END)
        entry_task.insert(0, selected_task)
    except tk.TclError:
        pass


# main window
root = tk.Tk()
root.title("Python To-Do List")
root.geometry("400x450")

# Load the tasks from the file
tasks = load_tasks()

# --- Create the GUI Widgets ---

# Frame for the listbox and scrollbar
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

# Listbox to display tasks
list_tasks = tk.Listbox(frame_tasks, height=15, width=50, selectmode=tk.SINGLE)
list_tasks.pack(side=tk.LEFT)

# Scrollbar for the listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Link scrollbar to listbox
list_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=list_tasks.yview)

# Bind the 'load_task_for_update' function to a click event in the listbox
list_tasks.bind('<<ListboxSelect>>', load_task_for_update)

# Entry widget to add/update tasks
entry_task = tk.Entry(root, width=54)
entry_task.pack(pady=10)

# Frame for the buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack()

# Buttons
button_add_task = tk.Button(frame_buttons, text="Add Task", width=15, command=add_task_gui)
button_add_task.pack(side=tk.LEFT, padx=5)

button_update_task = tk.Button(frame_buttons, text="Update Task", width=15, command=update_task_gui)
button_update_task.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", width=15, command=delete_task_gui)
button_delete_task.pack(side=tk.LEFT, padx=5)

# Load tasks into the listbox when the app starts
populate_listbox()

# Start the main GUI event loop
root.mainloop()