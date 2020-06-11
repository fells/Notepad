from tkinter import *


def newFile():
    pass

def openFile():
    pass

def saveFile():
    pass

def quitApp():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass



if __name__ == "__main__":
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    # Add text area

    TextArea = Text (root, font="Times 13")
    file = None

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

    EditMenu.add_cascade(label = "Edit", menu = EditMenu)
    
    # Edit menu ends

    # Help menu starts 
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)
    MenuBar.add_cascade(label = "Help", menu = HelpMenu)

    # Help menu ends 

    root.config(menu = MenuBar)

    root.mainloop()