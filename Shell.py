from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class Shell():
    def __init__(self, notebooks, nb, sections, pages):
        self.sections = Gtk.Notebook.new()
        self.sections.insert_page(gridBasics, labelBasics, 0)
        # tabLabel = Gtk.Label.new(tabName)
        self.pages = Gtk.Notebook.new()
        
        # for i in sections:
            
            
    # def newtab(self):
        
    def makeSection(self, sectionName, order):
        self.sections.insert_page()