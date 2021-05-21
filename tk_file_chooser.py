import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog


class TkFileChooser(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_chooser = ttk.Button(self, text='open', command=self.choose_file)
        self.file_chooser.pack(side='top')

        self.file_name_label = ttk.Label(self, text='none')
        self.file_name_label.pack()

        self.quit_button = ttk.Button(self, text='quit', command=self.master.destroy)
        self.quit_button.pack(side='bottom')

    def choose_file(self):
        chosen_file = filedialog.askopenfile()

        self.file_name_label['text'] = chosen_file.name


root = tk.Tk()
app = TkFileChooser(master=root)
app.mainloop()
