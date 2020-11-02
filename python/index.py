import tkinter as tk

# Initialize Window

root = tk.Tk()
root.title("To-do")
root.geometry("400x300")

# Generate Widgets

topFrame = tk.Frame(root, bg="blue")
bottomFrame = tk.Frame(root, bg="blue")

btn1 = tk.Button(topFrame, text="1", height=5, width=15)
btn2 = tk.Button(topFrame, text="2", height=5, width=15)
btn3 = tk.Button(topFrame, text="3", height=5, width=15)
btn4 = tk.Button(bottomFrame, text="4", height=5, width=15)

topFrame.pack(side=tk.TOP,fill=tk.X, expand=False, padx=3, pady=3)
bottomFrame.pack(side=tk.TOP,fill=tk.X, expand=False, padx=3, pady=3)

btn1.pack(side=tk.LEFT, padx=3)
btn2.pack(side=tk.LEFT, padx=3)
btn3.pack(side=tk.LEFT, padx=3)
btn4.pack(side=tk.LEFT, padx=3)

"""
btn1.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
btn2.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
btn3.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
"""

# Run program

root.mainloop()