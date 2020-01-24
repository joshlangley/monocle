from os import * # Import bash run abilities

from Shell import * # Import our classes from other files
from Shell import *

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        # Construct window
        Gtk.Window.__init__(self, title="Proprietary Notes")
        self.set_border_width(10)

        winShell = Shell()
        winShell.

    



win = HomeWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()