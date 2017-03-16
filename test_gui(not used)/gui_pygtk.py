import gtk
import pygtk
import gst
import pygst
import sys

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Alignment")
        self.set_size_request(1200, 720)
        self.set_position(gtk.WIN_POS_CENTER)

        vbox = gtk.VBox(False, 6)
        hbox = gtk.HBox(False, 3)
        valign = gtk.Alignment(0, 1, 0, 0)
        vbox.pack_start(valign)

        self.drawingarea = gtk.DrawingArea()
        self.set_size_request(1100,600)
        self.multimedia_file="/home/asitava/Downloads/paradise.ogv"
        self.player = gst.element_factory_make("playbin2", "MultimediaPlayer")
        self.player.set_property('uri',"file://" + self.multimedia_file)
        
        #vbox = gtk.VBox(False, 5)
        #hbox = gtk.HBox(True, 3)
        #valign = gtk.Alignment(0, 1, 0, 0)
        #vbox.pack_start(valign)
        
        homeButton = gtk.ToolButton(gtk.STOCK_HOME)
        homeButton.set_is_important(True)
        homeButton.set_size_request(70,35)
        
        camera = gtk.ToolButton(gtk.STOCK_MEDIA_RECORD)
        camera.set_is_important(True)
        camera.set_size_request(70,35)

        maps = gtk.ToolButton(gtk.STOCK_SELECT_COLOR)
        maps.set_is_important(True)
        maps.set_size_request(70,35)

        upButton = gtk.ToolButton(gtk.STOCK_CLOSE)
        upButton.set_is_important(True)
        upButton.set_sensitive(True)
        upButton.set_size_request(70,34)
        
        hbox.add(homeButton)
        hbox.add(camera)
        hbox.add(maps)
        hbox.add(upButton)
        
        halign = gtk.Alignment(0, 1, 0, 0)
        halign.add(hbox)
        
        #vbox.pack_start(drawingarea, False, False, 3)
        vbox.pack_start(halign, False, False, 3)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
        self.player.set_state(gst.STATE_PLAYING)

        #self.player = gst.element_factory_make("playbin", "MultimediaPlayer")
PyApp()
gtk.main()