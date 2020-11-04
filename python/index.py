import tkinter as tk
from tkinter import ttk

# Initialize Window

root = tk.Tk()
root.title("To-do")
root.geometry("400x300")

# Generate Widgets

taskview = ttk.Treeview(root, selectmode='browse')

# Set up the cols

taskview['columns'] = ('Task','Due','Points')
taskview['show'] = 'headings'

taskview.column('Task', width=200)
taskview.column('Due', width=50)
taskview.column('Points', width=50)

taskview.heading('Task', text = 'Task')
taskview.heading('Due', text = 'Due')
taskview.heading('Points', text = 'Points')

# Populate the cols

taskview.insert(parent='', index='end', values=('Discrete Structures Lecture','1','5'))

# Run program

taskview.pack(side = 'left')

root.mainloop()

'''
# To-do

- Add colors to the items based on due date
- work on populating from the http requests and not dummys
- add new task

'''