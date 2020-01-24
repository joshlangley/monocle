from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
import sys

class DataManager():
    def __init__(self):
        if ("./monocle/" not in home+"/.local/share"):
            system("mkdir ~/.local/share/monocle")

        path = home+"/.local/share/monocle/"
        self.notebooks = listdir(path)
        for i in self.notebooks:
            print (i)

        # return self.notebooks

    def initData(self, notebooks):
        return self.notebooks, self.nbselection, self.sections, self.pages
        # return self.sections
        # return self.pages
    # def tabConversion(self, notebooks):
    #     for i in notebooks:
            

debug = DataManager()