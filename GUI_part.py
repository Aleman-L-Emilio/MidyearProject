from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):



root = Tk()
root.title("Hangman!")
app = Application(root)
root.mainloop()