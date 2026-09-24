import tkinter as tk
import json


# ==========================================
# CREATE WINDOW
# ==========================================

root = tk.Tk()
root.title("My To-Do List")
root.geometry("500x650")


# ==========================================
# ADD TASK
# ==========================================

def add_task():
    task = task_entry.get().strip()

    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)


# ==========================================
# DELETE TASK
# ==========================================

def delete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task[0])


# ==========================================
# COMPLETE TASK
# ==========================================

def complete_task():
    selected_task = task_list.curselection()

    if selected_task:
        index = selected_task[0]
        task = task_list.get(index)

        if not task.startswith("✓ "):
            task_list.delete(index)
            task_list.insert(index, "✓ " + task)


# ==========================================
# UPDATE TASK
# ==========================================

def update_task():
    selected_task = task_list.curselection()

    if selected_task:
        index = selected_task[0]
        new_task = task_entry.get().strip()

        if new_task:
            task_list.delete(index)
            task_list.insert(index, new_task)
            task_entry.delete(0, tk.END)


# ==========================================
# SAVE TASKS
# ==========================================

def save_tasks():
    tasks = task_list.get(0, tk.END)

    with open("tasks.json", "w") as file:
        json.dump(list(tasks), file)

    print("Tasks saved successfully!")


# ==========================================
# LOAD TASKS
# ==========================================

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        for task in tasks:
            task_list.insert(tk.END, task)

    except FileNotFoundError:
        pass


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


# ==========================================
# TASK INPUT
# ==========================================

task_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=30
)

task_entry.pack(pady=10)


# ==========================================
# ADD BUTTON
# ==========================================

add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 14),
    command=add_task
)

add_button.pack(pady=5)


# ==========================================
# DELETE BUTTON
# ==========================================

delete_button = tk.Button(
    root,
    text="Delete Task",
    font=("Arial", 14),
    command=delete_task
)

delete_button.pack(pady=5)


# ==========================================
# COMPLETE BUTTON
# ==========================================

complete_button = tk.Button(
    root,
    text="Complete Task",
    font=("Arial", 14),
    command=complete_task
)

complete_button.pack(pady=5)


# ==========================================
# UPDATE BUTTON
# ==========================================

update_button = tk.Button(
    root,
    text="Update Task",
    font=("Arial", 14),
    command=update_task
)

update_button.pack(pady=5)


# ==========================================
# SAVE BUTTON
# ==========================================

save_button = tk.Button(
    root,
    text="Save Tasks",
    font=("Arial", 14),
    command=save_tasks
)

save_button.pack(pady=5)


# ==========================================
# TASK LIST
# ==========================================

task_list = tk.Listbox(
    root,
    font=("Arial", 15),
    width=35,
    height=15
)

task_list.pack(pady=20)


# ==========================================
# LOAD OLD TASKS
# ==========================================

load_tasks()


# ==========================================
# START PROGRAM
# ==========================================

root.mainloop()