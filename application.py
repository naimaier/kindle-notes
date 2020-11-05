from tkinter import *
from tkinter import ttk
from functools import partial


class Application():

    def __init__(self, root):

        self.root = root
        self.root.title("Kindle Notes Exporter")
        self.root.resizable(height=False, width=False)

        self.main_frame = Frame(self.root, padx=10, pady=10)
        self.main_frame.pack(expand=True)

        self.lbl_title = Label(master=self.main_frame,
                               font="Verdana 20 bold",
                               padx=10, pady=10,
                               text="Kindle Note Exporter")

        self.lbl_title.pack()

        """ Input Button """
        self.btn_input = Button(master=self.main_frame, text="Load 'My Clippings.txt'")
        self.btn_input["command"] = partial(self.load_input_file)
        self.btn_input.pack()

        """ Options """
        self.combobox_books = ttk.Combobox(master=self.main_frame)
        self.combobox_books.pack()

        """ Export Button """
        self.btn_export = Button(master=self.main_frame, text="Export")
        self.btn_export["command"] = partial(self.export)
        self.btn_export.pack()

    def load_input_file(self):
        with open('My Clippings.txt') as file:
            data = file.read()
            self.parse(data)

    def parse(self, data):
        pass

    def export(self):
        pass


# Generate main window
root = Tk()
gui = Application(root)

# Necessary for winfo_width and winfo_heigh to work properly
root.update()

""" Centering the window on the screen """
# https://yagisanatode.com/2018/02/24/how-to-center-the-main-window-on-the-screen-in-tkinter-with-python-3/
# Changed winfo_reqwidth and winfo_reqheight to winfo_width and winfo_height

# Gets the requested values of the height and widht.
windowWidth = root.winfo_width() 
windowHeight = root.winfo_height()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()