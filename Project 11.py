#Jayson Brown Lab-11 (Python)

import tkinter as tk
from tkinter import *
from tkinter import messagebox



class Root_Window(tk.Frame): # 1.Make a root window and child window. 
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs) 
        self.button = tk.Button(self, text="Create Child", command=self.create_child_window) 
        self.button.pack(side="bottom", fill="both", expand=True, padx=100, pady=100)  
    
    # 1.Make a root window and child window.     
    def create_child_window(self):
        child = tk.Toplevel(self)
        def someFunction():
            Label(child, text="Thank you for saving.", width=20, height=2).pack()
        child.geometry("200x190")
        child.title("Child Window")
       # child['bg']='green'
        Label(child, text="Username").pack() # 2.Put two label "username" and "password" .
        username_enter = Entry(child, textvariable="username") # 2.Put two label "username" and "password" .
        username_enter.pack()
        Label(child, text="").pack()
        Label(child, text="Password").pack() # Label for password
        password_enter = Entry(child, textvariable="password") # 2.Put two label "username" and "password" .
        password_enter.pack()
        Label(child, text="").pack()
        Button(child, text="Save", width=20, height=2, command = someFunction).pack() # 4. One button
        


# 1.Make a root window and child window. 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Root Window") 
    root.geometry("300x270") 
    main = Root_Window(root)
    main['bg']='blue'
    main.pack(fill="both", expand=True)
    root.mainloop()