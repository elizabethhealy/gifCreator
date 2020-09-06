import tkinter as tk
from tkinter import font as tkfont
from creategif import *

class GifApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=44, weight="bold")
        self.subtitle_font = tkfont.Font(family='Helvetica', size=24)
        self.label_font = tkfont.Font(family='Times New Roman', size=14)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PicPage, VidPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        buttons = tk.Frame(self)
        texts = tk.Frame(self)
        texts.pack(side = tk.TOP)
        buttons.pack(side=tk.TOP)

        label = tk.Label(self, text="GifCreator", font=controller.title_font)
        label.pack(in_ = texts, side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Welcome to GifCreator --"+
        " a program that creates gifs from a series of images or a video!",
         font=controller.subtitle_font, justify = tk.CENTER, wraplength = 350)
        label2.pack(in_ = texts, side="top", fill="x", pady=100, padx = 10)

       

        button1 = tk.Button(self, text="Convert Pics2Gif",
                            command=lambda: controller.show_frame("PicPage"))
        button2 = tk.Button(self, text="Convert Vid2Gif",
                            command=lambda: controller.show_frame("VidPage"))
        button1.pack(in_=buttons, side = tk.LEFT, pady=40, padx = 10)
        button2.pack(in_=buttons, side = tk.LEFT, pady=40, padx = 10)
        


class PicPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pic2Gif", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class VidPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Vid2Gif", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()




if __name__ == "__main__":
    app = GifApp()
    app.geometry("700x600")
    app.title = "GifCreator"
    app.mainloop()