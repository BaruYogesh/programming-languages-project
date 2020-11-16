import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

import requests
from enum import Enum

# Color Enum

class Color(Enum):
    RED = '#FFCCCB',
    YELLOW = '#FFFF99',
    GREEN = '#90EE90'

# Functions

# takes in a 'due' string and returns a tuple with form ('due date', 'urgency tag') where:
# 'due date' represents the number of days from now the task is due and 'urgency tag' is a TKinter tag that styles the task. 
def dueDate(due):
    if due == '0':
        return ('Today', 'urgent')
    elif due == '1':
        return ('Tomorrow','moderate')
    else:
        return (due,'safe')

# inserts a new task dictionary into the TreeView
def insertTask(task):
    urgency = dueDate(task['due'])
    taskView.insert(parent='', index='end', values=(task['title'], urgency[0], task['points']), tags=(urgency[1]))


# removes all task items from the TreeView
def clearTasks():
    for task in taskView.get_children():
        taskView.delete(task)

# removes then replaces all task items in TreeView
def updateTasks():
    clearTasks()
    for task in userTasks: 
        insertTask(task)

# adds a task to the TreeView and the working list of tasks
def createTask(taskList, title, due, points):

    task = {
        'name' : userName,
        'title' : title,
        'due' : due,
        'points' : points
    }

    taskList += task # userData['tasks']

    return task


def addTask(task):
    requests.post('http://localhost:3001/addtask', params=task)

def removeTask(task):
    requests.post('http://localhost:3001/removetask', params=task)

def newTask():

    title = simpledialog.askstring(title='New Task for '+userName, prompt='Enter title of new task:')
    due = str(simpledialog.askinteger(title='New Task for '+userName, prompt='Enter days due from now for new task:'))
    points = str(simpledialog.askinteger(title='New Task for '+userName, prompt='Enter point value for new task:'))

    task = createTask(userTasks, title, due, points)

    insertTask(task)

    addTask(task) # http post

def deleteTask():

    focus = taskView.focus()

    if focus == '':
        messagebox.showerror('Error', 'No Task Selected')
        return

    item = taskView.item(focus)
    itemValues = item['values']

    task = {
        'name' : userName,
        'title' : itemValues[0]
    }

    if (messagebox.askyesno('Remove Task for '+task['name'], 'Do you wish to delete task: '+task['title']) == True):
        removeTask(task) # http post

        taskView.delete(focus)

        messagebox.showinfo('Success', 'Task '+task['title']+' has been removed successfully')


def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.

    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if
      elm[:2] != ('!disabled', '!selected')]

# Main Script

userName = 'none'

while True:
    userName = simpledialog.askstring(title='Sign in', prompt='Enter the name of the user') # Get the user string

    request = requests.get('http://localhost:3001/get?name='+userName.lower())

    if (request.status_code == 200):
        break
    else:
        messagebox.showerror(title='Error', message="Error code: {errorCode} for user {userName}".format(request.status_code,userName))

userData = request.json() # userData['tasks'], userData['name']
userTasks = userData['tasks']

''' # SAMPLE TASKS STRUCTURE FOR TESTING
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

style = ttk.Style() # These 2 lines hopefully make TreeView item colors work properly.
style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

taskView = ttk.Treeview(root, selectmode='browse')

addButton = tk.Button(root, text='Add New Task', command=newTask)
removeButton = tk.Button(root, text='Remove Selected Task', command=deleteTask)

# Set up the cols

taskView['columns'] = ('Task','Due','Points')
taskView['show'] = 'headings'

taskView.column('Task', width=200)
taskView.column('Due', width=75)
taskView.column('Points', width=50)

taskView.heading('Task', text = 'Task')
taskView.heading('Due', text = 'Due')
taskView.heading('Points', text = 'Points')

# Populate the cols

updateTasks()

# sample task

insertTask(createTask(userTasks,'This task persists for testing','1','5'))

# Set Tags

taskView.tag_configure('urgent', foreground = 'black', background=Color.RED.value)
taskView.tag_configure('moderate', foreground = 'black', background=Color.YELLOW.value)
taskView.tag_configure('safe', foreground = 'black', background=Color.GREEN.value)

# Place objects

taskView.pack(side = 'top')
removeButton.pack(side = 'bottom')
addButton.pack(side = 'bottom')


# Run program

root.mainloop()


'''
# To-do

- work on populating from the http requests and not dummys
- Add / Remove task buttons
- Add scrollbar

'''