from os import * # Import bash run abilities
from os.path import expanduser, join
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

        # os.path.join automatically adds a slash between home and ".local/share"
        # so this if statement checks if there is a file or directory called "monocle" in ~/.local/share,
        # and creates one if there is not
        if "monocle" not in listdir(join(home, ".local/share")):
            system("mkdir ~/.local/share/monocle")

        path = home+"/.local/share/monocle/"
        self.notebooks = listdir(path)
        print ("Notebooks:")
        for i in self.notebooks:
            print (i)
        self.activeNotebook = self.notebooks[1]
        print("Notebook "+self.activeNotebook+" selected.")
        self.sections = listdir(path+self.activeNotebook)
        print("Sections:")
        for i in self.sections:
            print(i)
        self.activeSection = self.sections[1]
        print("Section "+self.activeSection+" selected.")
        self.pages = listdir(path+self.activeNotebook+"/"+self.activeSection)
        self.activePage = self.pages[0]

        

        
        
            # BYRON: Please don't work on trying to fix this. I forgot that 
            # there really is no real need for what I was trying to do anyway. 
            # (Besides, I bet it was just bad logic because I'm so tired.)
            # 
            # print("Section "+i+"'s contents:")
            # for i in self.pages:
            #     print(i)
        winShell = Shell()
        # self, notebooks, activeNotebook, sections, activeSection, pages, activePage
        gtkShell = winShell.tabInit(path, self.notebooks, self.activeNotebook, self.sections, self.activeSection, self.pages, self.activePage)
        self.add(gtkShell)
       
win = HomeWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
