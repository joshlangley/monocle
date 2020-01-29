from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

from Shell import * # Import our classes from other files

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        # Construct window
        Gtk.Window.__init__(self, title="Monocle")
        self.set_border_width(10)
        system("mkdir ~/.local/share/monocle")
        system("mkdir ~/.monocle")

        appdata = home+"/.local/share/monocle/"
        nbpath = home+"/.monocle/"
        self.notebooks = listdir(nbpath)
        print ("Notebooks:")
        for i in self.notebooks:
            print (i)
        self.activeNotebook = self.notebooks[0]
        print("Notebook "+self.activeNotebook+" selected.")
        self.sections = listdir(nbpath+self.activeNotebook)
        print("Sections:")
        for i in self.sections:
            print(i)
        self.activeSection = self.sections[1]
        print("Section "+self.activeSection+" selected.")
        self.pages = listdir(nbpath+self.activeNotebook+"/"+self.activeSection)
        self.activePage = self.pages[0]

        winShell = Shell()
        # self, notebooks, activeNotebook, sections, activeSection, pages, activePage
        gtkShell = winShell.tabInit(appdata, nbpath, self.notebooks, self.activeNotebook, self.sections, self.activeSection, self.pages, self.activePage)
        self.add(gtkShell)
       
win = HomeWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()