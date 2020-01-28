from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class Shell():
    def __init__(self):
        self.sections = Gtk.Notebook.new()
        # tabLabel = Gtk.Label.new(tabName)
        self.pages = Gtk.Notebook.new()
        self.pages.set_tab_pos (Gtk.PositionType.LEFT)
            
    def tabInit(self, path, notebooks, activeNotebook, sections, activeSection, pages, activePage):
        numberofSections = 0
        for i in sections:
            # self.makeSection(i, k, self.pages)
            self.sections.insert_page(self.pages, Gtk.Label.new(i), numberofSections)
            numberofSections = numberofSections+1
            # self.add()
        numberofPages = 0
        for i in pages:
            self.pages.insert_page(Gtk.Image.new_from_file(path+"tuxmonocle.png"), Gtk.Label.new(i), numberofPages)
            numberofPages = numberofPages+1

        return self.sections
    # def makeSection(self, sectionName, position, pages):
    #     self.sections.insert_page(pages, Gtk.Label.new(sectionName), position)
    #     # self.add()

    
# win = HomeWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()