import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Untitled - Notepad")
        self.__root.geometry("800x600")
        
        self.__thisTextArea = Text(self.__root, wrap=WORD, font=("Consolas", 12))
        self.__thisTextArea.pack(expand=True, fill=BOTH)
        
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        
        self.__file = None
        
        self.__createMenuBar()
        
    def __createMenuBar(self):
        self.__thisMenuBar = Menu(self.__root)

        self.__thisFileMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)
        
        self.__thisEditMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)
        
        self.__thisHelpMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)
        
        self.__root.config(menu=self.__thisMenuBar)
    
    def __quitApplication(self):
        self.__root.destroy()
    
    def __showAbout(self):
        showinfo("Notepad", "Simple Notepad using Python Tkinter")
    
    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                                 ("Text Documents","*.txt")])
        if self.__file:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)
            with open(self.__file, "r") as file:
                self.__thisTextArea.insert(1.0, file.read())
    
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)
    
    def __saveFile(self):
        if self.__file is None:
            self.__file = asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                       ("Text Documents","*.txt")])
        if self.__file:
            with open(self.__file, "w") as file:
                file.write(self.__thisTextArea.get(1.0, END))
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
    
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")
    
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
    
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = Tk()
    app = Notepad(root)
    root.mainloop()
