import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.configure(bg="lightblue")  # Set background color

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                self.tasks = [task.strip() for task in tasks]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
