import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

import requests

user = 'none'

while True:
    user = simpledialog.askstring(title='Sign in', prompt='Enter the name of the user') # Get the user string

    request = requests.get('http://localhost:3001/get?name='+user.lower())

    if (request.status_code == 200):
        break
    else:
        messagebox.showerror(title='Error', message="User: '{name}' not found".format(user))

userData = request.json()
userTasks = userData['tasks']

''' # TASKS STRUCTURE FOR TESTING INJECTION
userTasks = [
        {
            "title": "task1",
            "due": "1",
            "points": "1"
        },
        {
            "title": "task2",
            "due": "2",
            "points": "2"
        },
    ]
'''

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

for task in userTasks: 
    taskview.insert(parent='', index='end', values=(task['title'],task['due'],task['points']), tags=('1'))

taskview.insert(parent='', index='end', values=('Discrete Structures Lecture','1','5'), tags=('1'))

'''
Task: Final Column population.

- transform the due date if it is due 'Today' or 'Tomorrow' if the value is 0 or 1
- (?) decide a background color based off of point values

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