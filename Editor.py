from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class Shell():
    def __init__(self):
        super().__init__()