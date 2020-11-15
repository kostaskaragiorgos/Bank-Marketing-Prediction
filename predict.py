from tkinter import Tk, Menu, filedialog
from tkinter import messagebox as msg
import pandas as pd
class Prediction():
    def __init__(self,master):
        self.master = master
        self.master.title("Prediction")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        self.filename = ""
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Insert a csv file", accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: self.aboutmenu())
    def column_validation(self):
        if all([item in self.df.columns for item in ['default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign']]):
            msg.showinfo("SUCCESS", "CSV FILE ADDED SUCCESSFULLY")
        else:
            self.filename = ""
            msg.showerror("ERROR", "NO PROPER CSV ")

    def inputvalidation(self):
        """ input validation"""
        if ".csv" in self.filename:
            self.df = pd.read_csv(self.filename)
            self.column_validation()
        else:
            self.filename = ""
            msg.showerror("ERROR", "NO CSV IMPORTED")

    def insertfile(self):
        if self.filename is "":
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"),
                                                                  ("all files", "*.*")))
            self.inputvalidation()
        else:
            msg.showerror("ERROR", " A CSV FILE IS ALREADY OPEN")
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

        

def main():
    root=Tk()
    Prediction(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
