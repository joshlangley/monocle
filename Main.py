from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        # Construct window
        Gtk.Window.__init__(self, title="Monocle")
        # self.set_border_width(3)
        system("mkdir ~/.local/share/monocle")
        system("mkdir ~/.monocle")

        self.appdata = home+"/.local/share/monocle/"
        self.nbpath = home+"/.monocle/"

        # self.selectednb = nbpath+appstate.??[1]

        # self.appStates = "INIT" # Alt READY

    def init(self):
        self.sectionnb = Gtk.Notebook.new()
        self.sections = []

        #Notebook
        self.nblist = listdir(self.nbpath)
        if not self.nblist:
            self.nblist = self.nblist+["isempty"]
        else:
            self.selectednb = self.nblist[0]


        #Make Sections widgets
        self.seclist = listdir(self.nbpath+self.selectednb)
        if not self.seclist:
            self.seclist = self.seclist+["isemptynotebook"]
        else:
            for sec in self.seclist:
                sec = Gtk.Notebook.new()
                self.sections = self.sections+[sec]

        #Set nb gtk.notebook widget up (top level nb widget)
        if "isemptynotebook" in self.seclist:
            emptnb = Gtk.Image.new()
            emptnb.set_from_file(self.appdata+"walls"+"/bionic.png")
            emptlab = Gtk.Label.new("Nothing Opened")
            self.sectionnb.insert_page(emptnb, emptlab, -1)
        else:
            k=0                            # Add the pages to top level nb widget
            for sec in self.seclist:
                secwid = self.sections[k]
                seclab = Gtk.Label.new(sec)
                self.sectionnb.insert_page(secwid, seclab, -1)
                k=k+1
                
                #Set section pages
                # pglist = listdir(self.nbpath+self.selectednb+"/"+sec)
                
                # if not pglist:
                #     pglist = pglist+["isemptysection"]
                # else:
                #     for pg in pglist:
                #         pgwid = Gtk.Image.new()
                #         pgwid.set_from_file(self.appdata+"tuxmonocle.png")
                #         pglab = Gtk.Label.new(pg)

                #         secwid.insert_page(pgwid, pglab, -1)
     

        self.add(self.sectionnb)

    def ready(self):
        print("READY")

    def debugout(self):
        print("Notebooks:")
        print(self.nblist)

class SectionWidget():
    def __init__(self, name, appdata, nbpath, selectednb):
        self.name = name
        self.appdata = appdata
        self.nbpath = nbpath
        self.selectednb = selectednb
        self.pages = Gtk.Notebook.new()

        self.pglist = listdir(self.nbpath+self.selectednb+"/"+self.name)

        if not pglist:
            pglist = pglist+["isemptysection"]
        else:
            for pg in pglist:
                pgwid = Gtk.Image.new()
                pgwid.set_from_file(self.appdata+"tuxmonocle.png")
                pglab = Gtk.Label.new(pg)
        
                secwid.insert_page(pgwid, pglab, -1)        

        return pages
    
    # def 

win = HomeWindow()
win.init()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()