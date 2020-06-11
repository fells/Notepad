from tkinter import *


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
    FileMenu = Menu(MenuBar, tearoff = 0)

    # To open new file

    root.mainloop()