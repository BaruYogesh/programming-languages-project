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

taskview.insert(parent='', index='end', values=('Discrete Structures Lecture','1','5'), tags=('1'))

'''
Task: Final Column population.

Procedure: Method 
- asks for the user's name 
- gets all of the tasks
- retrives all of the values
- transform the due date if it is due 'Today' or 'Tomorrow' if the value is 0 or 1
- (?) decide a background color based off of point values
- injects items with format: taskview.insert(parent='', index='end', values=('Task Description','Due','# of Points'))

'''

# Set Tags

taskview.tag_configure('1', foreground='red', background='red')

# Place objects

taskview.pack(side = 'left')

# Run program

root.mainloop()

'''
# To-do

- (?) Add colors to the items based on due date if possible
- work on populating from the http requests and not dummys
- Add / Remove task buttons

'''