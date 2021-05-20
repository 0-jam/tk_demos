import tkinter as tk
import tkinter.filedialog as filedialog


class MyApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_chooser = tk.Button(self, text='open', command=filedialog.askopenfile)
        self.file_chooser.pack(side='top')

        self.quit_button = tk.Button(self, text='quit', fg='red', command=self.master.destroy)
        self.quit_button.pack(side='bottom')


root = tk.Tk()
app = MyApplication(master=root)
app.mainloop()
