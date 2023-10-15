import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_list = []

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(root, width=40)
        self.listbox.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_list.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def remove_task(self):
        selected_task = self.listbox.get(tk.ACTIVE)
        if selected_task in self.task_list:
            self.task_list.remove(selected_task)
            self.listbox.delete(tk.ACTIVE)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
