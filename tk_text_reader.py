import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.ttk as ttk
from time import sleep

WAIT = 0.01


class TkTextReader(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()
        self.create_widgets()
        self.chosen_file = None

    def create_widgets(self):
        self.file_chooser = ttk.Button(self, text='open file', command=self.choose_file)
        self.file_chooser.pack(side='top')

        self.file_name_label = ttk.Label(self, text='none')
        self.file_name_label.pack()

        self.file_chooser = ttk.Button(self, text='start reading', command=self.read_text)
        self.file_chooser.pack(side='top')

        self.text_label = ttk.Label(self, text='', wraplength=800)
        self.text_label.pack()

        self.progressbar = ttk.Progressbar(self)
        self.progressbar.pack()

        self.quit_button = ttk.Button(self, text='quit', command=self.master.destroy)
        self.quit_button.pack(side='bottom')

    def choose_file(self):
        self.chosen_file = filedialog.askopenfile()

        self.file_name_label['text'] = self.chosen_file.name

    def show(self, line):
        for c in line.strip():
            self.text_label['text'] += c
            self.text_label.update()

            sleep(WAIT)

    def read_text(self):
        if self.chosen_file is None:
            self.text_label['text'] = 'no file selected'
            return

        self.text_label['text'] = ''

        for line in self.chosen_file:
            self.show(line)


root = tk.Tk()
app = TkTextReader(master=root)
app.mainloop()
