#handle exceptions 
#empty login fileds
#incorrect student credentials
#incorrect email format
import tkinter as tk
from tkinter import messagebox

class ExceptionView:
    def __init__(self, parent, message):
        self.parent = parent
        self.message = message

    def show(self):
        messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    app = tk.Tk()
    app.withdraw()
    ExceptionView(app, "Test error message").show()
