from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
import sys

class DataManager():
    def __init__(self):
        if ("./monocle/" not in home+"/.local/share"):
            system("mkdir ~/.local/share/monocle")

        path = home+"/.local/share/monocle/"
        notebooks = listdir(path)
        for i in notebooks:
            print (i)

debug = DataManager()