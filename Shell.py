from os import * # Import bash run abilities
import platform
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
        linuxdistver = platform.linux_distribution()[2]
            
    def tabInit(self, appdata, nbpath, notebooks, activeNotebook, sections, activeSection, pages, activePage):
        numberofSections = 0
        for i in sections:
            # self.sections.add(self.empty(appdata))
            if (i == activeSection):
                self.sections.insert_page(self.pages, Gtk.Label.new(i), numberofSections)
            else:
                self.sections.insert_page(self.pages, Gtk.Label.new(i), numberofSections)
                # self.sections.insert_page(empty(), Gtk.Label.new(i), numberofSections)

            numberofSections = numberofSections+1
            # self.add()
        numberofPages = 0
        for i in pages:
            self.pages.insert_page(Gtk.Image.new_from_file(appdata+"walls/tuxmonocle.png"), Gtk.Label.new(i), numberofPages)
            numberofPages = numberofPages+1
        return self.sections

    def empty(self, appdata):
        linuxdistver = platform.linux_distribution()[2]
        bgname = appdata+"walls/"+linuxdistver+".png"
        widget = Gtk.Image.new_from_file(appdata+bgname)
        return widget

        
    def update(self, activePage):
        Gtk.Widget.new()
        activeSection = self.sections.get_current_page()
        activePage = self.pages.get_current_page()
        # for i in sections:
            
    

    # def makeSection(self, sectionName, position, pages):
    #     self.sections.insert_page(pages, Gtk.Label.new(sectionName), position)
    #     # self.add()

    
# win = HomeWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()