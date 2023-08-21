#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(pady=10)
        
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
            
    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task to update.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")
        
    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index[0])
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Select an operation (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == '1':
    print("Result:", add(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")


# In[ ]:





# In[ ]:




