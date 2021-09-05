import tkinter as tk
from tkinter import ttk
from tkinter import tix
from tkinter.messagebox import showinfo
from linkcounter import Linkcounter


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label1
        self.label1 = ttk.Label(self, text='https://en.wikipedia.org/wiki/Special:Random')
        self.label1.pack(**options)

        #button1
        self.button1 = ttk.Button(self, text='Get list of links')
        self.button1['command'] = self.button1_clicked
        self.button1.pack(**options)

        #label2
        self.label2 = ttk.Label(self, text='Type article name below to get info if it was parsed before')
        self.label2.pack(**options)

        #entry
        self.entry = tk.Entry(self)
        self.entry.pack()

        #button2
        self.button2 = ttk.Button(self, text='Get detailed info')
        self.button2['command'] = self.button2_clicked
        self.button2.pack(**options)

        #button3
        self.button3 = ttk.Button(self, text='Get saved links')
        self.button3['command'] = self.button3_clicked
        self.button3.pack(**options)

        #button4
        self.button4 = ttk.Button(self, text='Count links')
        self.button4['command'] = self.button4_clicked
        self.button4.pack(**options)

        # Create the text widget
        self.text_widget = tk.Text(self, height=14, width=50)
        # Create a scrollbar
        self.scroll_bar = tk.Scrollbar(self)
        self.scroll_bar.pack(side=tk.RIGHT)
        self.text_widget.pack(side=tk.LEFT)
        # Insert text into the text widget
        self.text_widget.insert(tk.END, "Wiki data")
        # show the frame on the container
        self.pack(**options)

    def button1_clicked(self):
        session = Linkcounter()
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert(tk.END, session.get_random_links())
    
    def button2_clicked(self):
        session = Linkcounter()
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert(tk.END, session.view_article(self.entry.get()))

    def button3_clicked(self):
        session = Linkcounter()
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert(tk.END, session.show_list_of_links_by_article_name(self.entry.get()))

    def button4_clicked(self):
        session = Linkcounter()
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert(tk.END, session.show_number_of_links_by_article_name(self.entry.get()))

    

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Linkcounter')
        self.geometry('600x600')


app = App()
frame = MainFrame(app)
app.mainloop()