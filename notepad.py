from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Douments", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    pass

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad created by Michel Calil")



if __name__ == "__main__":
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    # Add text area

    TextArea = Text (root, font="Times 13")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    # Lets create a menu bar
    MenuBar = Menu(root)
    
    # File menu starts
    FileMenu = Menu(MenuBar, tearoff = 0)

    # To open new file
    FileMenu.add_command (label = "New", command = newFile)

    # To open already an existing file
    FileMenu.add_command(label = "Open", command = openFile)

    # To save the current File

    FileMenu.add_command (label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu = FileMenu)

    # File menu ends

    # Edit menu starts
    EditMenu = Menu(MenuBar, tearoff = 0)
    
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label = "Edit", menu = EditMenu)
    
    # Edit menu ends

    # Help menu starts 
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)
    MenuBar.add_cascade(label = "Help", menu = HelpMenu)

    # Help menu ends 

    root.config(menu = MenuBar)

    # Adding a scroll bar
    ScrollBar = Scrollbar(TextArea)
    ScrollBar.pack(side = RIGHT, fill = Y)
    ScrollBar.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = ScrollBar.set)

    root.mainloop()