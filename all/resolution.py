from main import *
from kivy.core.window import Window
import tkinter;

class Resolution():
    def check(self):
    # try cutch todo
        root = tkinter.Tk()
        WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()
        if WIDTH == 1920 or 1600 or 1366 and HEIGHT == 1080 or 900 or 768: Window.size = (720/2, 1280/2); Window.resizeble = (False);
        else:   Window.fullscreen = (True); Window.resizeble = (False);
