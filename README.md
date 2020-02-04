# Monocle
A simple but powerful Note taking app with a similar layout to OneNote back when it was good.

# Gtk Docs
* https://developer.gnome.org/gtk3/stable/GtkNotebook.html#gtk-notebook-set-show-tabs
* https://developer.gnome.org/gtk3/unstable/GtkWidget.html#gtk-widget-new
* https://developer.gnome.org/gtk3/stable/GtkButton.html

# Testing
To test this system, you will need a testable "~/.local/share/monocle" and "~/.monocle" directory. Please copy the ones provided in the repository to these specified locations. It will populate these things by itself at some point soon, but not yet.

# Tasks for Alpha release (0.0.*)
[-] Example - self.ex
[-] Make page tabs vertical (aligned left) - Bryden, Carter
[-] Figure out the new error (Why does it suddenly think there's nothing in the list? [I think the nblist]) - <Open>
[-] Rebuild initial code as better - Josh
[-] Make snazzy backdrops for no open page - Josh
[-] Make and test code for no open page - Josh
[-] Make and test code for no open sections - Josh
[] Create Gtk Pixbuf system (So that the appwindow determines the size of backdrop and not the other way around) - Carter
[] Make and test code for no open notebooks - Josh
[] Export logo icons (Main - 512x512 and Symbolic - 16x16) - Ben
[] Create custom Gtk Titlebar and populate it with basic buttons - Josh
[] Make ability to add notebooks, sections, and pages - <OPEN>
[] Learn how to insert plain text editor widget - Bryden
[] Figure out how to set app icon and symbolic icon - <OPEN>
[] Figure out how to set GNOME shell app name - <OPEN>[Someone running the GNOME DE: Carter, Josh, Byron?]
[] Find a good text editor API (Render md / Type with formatting / Both) - EVERYONE
    -> Perhaps Quill? (It seems to be our best shot right now)
[] Learn how to run said editor - Carter, !Ben (As has been made clear)

# Tasks for Beta release (0.1.*)
[] Create and implement save state system (Reopen active notebook, section, page, and later cursor position) - <OPEN>

# Tasks for the far future and extensions and such (side load || *.*.* [x>=2.0])
[] Evernote compatibility (Open online Evernote notebooks; will be quite easy once Evernote API and Quill API are implemented) [~17.0+]
[] OneNote compatibility (Open online OneNote notebooks as if in OneNote) [~19.0+]