from tkinter import *
from tkinter import ttk
from functools import partial


class Application():

    # list containing all the clippings
    myClippings = []

    def __init__(self, root):

        ''' GUI '''
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
        # open My Clippings kindle file
        with open('My Clippings.txt') as file:
            fileContent = file.read()
            self.parseFileContent(fileContent)


    def parseFileContent(self, fileContent):
        # separate each element in the file
        elements = fileContent.split('==========')

        # remove last element witch is always blank
        elements.pop()

        # parse elements and add to my clippings variable
        for element in elements:
            clipping = self.parseElement(element)
            
            if clipping is not None:
                self.myClippings.append(clipping)            


    def parseElement(self, element):
        # separate the elements of a clipping and strip the blank values
        element = element.split('\n')
        element = list(filter(None, element))

        # if element is not a bookmark (len == 3) parse element
        if len(element) == 3:
            parsedElement = {}
            parsedElement['book'] = element[0]
            parsedElement['info'] = self.parseElementInfo(element[1])
            parsedElement['content'] = element[2]
            return parsedElement
        # if it is a bookmark
        else:
            return None

        
    def parseElementInfo(self, elementInfo):
        # separate the info present in the line of text
        elementInfo = elementInfo.split(' | ')

        # parse the info according to it's size
        parsedElementInfo = {}
        if len(elementInfo) == 3:
            parsedElementInfo['type'] = elementInfo[0]
            parsedElementInfo['position'] = elementInfo[1]
            parsedElementInfo['date'] = elementInfo[2]
        else:
            parsedElementInfo['type'] = elementInfo[0]
            parsedElementInfo['position'] = None
            parsedElementInfo['date'] = elementInfo[1]

        return parsedElementInfo


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