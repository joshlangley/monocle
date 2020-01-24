from os import * # Import bash run abilities

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class Shell():
    def __init__(self):
        sections = Gtk.Notebook.new()
        sections.insert_page(gridBasics, labelBasics, 0)
        # tabLabel = Gtk.Label.new(tabName)
        pages = Gtk.Notebook.new()
        pages.insert_page()

    def newtab(self):
        