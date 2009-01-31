######################################################################
##
## Copyright (C) 2006,  Blekinge Institute of Technology
##
## Filename:      PreferencesDialogue.py
## Author:        Simon Kagstrom <ska@bth.se>
## Description:   Preferences dialog
##
## $Id: PreferencesDialogue.py 8422 2006-06-02 06:05:30Z ska $
##
######################################################################
import pygtk

pygtk.require('2.0')
import gtk, gobject

from Config import *

class PreferencesDialogue:
    def __init__(self, w=None):
	dialog = gtk.Dialog("%s - Preferences" % (PROGRAM_NAME))
	defaults = gtk.Button("Defaults")
	cancel = gtk.Button("Cancel", gtk.STOCK_CANCEL)
	ok = gtk.Button("OK", gtk.STOCK_OK)

	table = gtk.Table(3, 3, False)
	objdump = gtk.Entry()
	readelf = gtk.Entry()
	nm = gtk.Entry()
	showHighLevel = gtk.CheckButton("Show high level code")

	cancel.connect("clicked", lambda w: dialog.destroy())
	ok.connect("clicked", self.okSelected,
		   dialog, objdump, readelf, nm, showHighLevel)
	defaults.connect("clicked", self.defaultsSelected,
			 objdump, readelf, nm, showHighLevel)

	objdump.set_text(config.objdump)
	readelf.set_text(config.readelf)
	nm.set_text(config.nm)
	showHighLevel.set_active(config.showHighLevelCode)

	table.attach(gtk.Label("Objdump:"), 0, 1, 0, 1,  ypadding=2)
	table.attach(gtk.Label("Readelf:"), 0, 1, 1, 2,  ypadding=2)
	table.attach(gtk.Label("nm:"), 0, 1, 2, 3,  ypadding=2)
	table.attach(objdump, 1, 2, 0, 1,  ypadding=2)
	table.attach(readelf, 1, 2, 1, 2,  ypadding=2)
	table.attach(nm, 1, 2, 2, 3,  ypadding=2)
	table.attach(showHighLevel, 0, 2, 3, 4,  ypadding=6)

	dialog.vbox.pack_start(table, True, True, 0)
	dialog.action_area.pack_start(defaults, True, True, 0)
	dialog.action_area.pack_start(cancel, True, True, 0)
	dialog.action_area.pack_start(ok, True, True, 0)
	dialog.show_all()

    def defaultsSelected(self, widget, objdump, readelf, nm, showHighLevel):
	config.restoreAllDefaults()
	objdump.set_text(config.objdump)
	readelf.set_text(config.readelf)
	nm.set_text(config.nm)
	showHighLevel.set_active(config.showHighLevelCode)

    def okSelected(self, widget, dialog, objdump, readelf, nm, showHighLevelCode):
	if objdump.get_text() == "":
	    config.objdump = config.getDefault("objdump")
	else:
	    config.objdump = objdump.get_text()

	if readelf.get_text() == "":
	    config.readelf = config.getDefault("readelf")
	else:
	    config.readelf = readelf.get_text()

	if nm.get_text() == "":
	    config.nm = config.getDefault("nm")
	else:
	    config.nm = nm.get_text()

	config.showHighLevelCode = showHighLevelCode.get_active()
	config.save()

	dialog.destroy()
