######################################################################
##
## Copyright (C) 2006,  Blekinge Institute of Technology
##
## Filename:      Config.py
## Author:        Simon Kagstrom <ska@bth.se>
## Description:   Configuration storage
##
## $Id:$
##
######################################################################
import cPickle, os, os.path

PROGRAM_NAME="Dissy"
PROGRAM_VERSION="3"
PROGRAM_URL="http://www.ipd.bth.se/ska/sim_home/dissy.html"

class Config:
    def __init__(self):
	self.configfile = os.path.expanduser("~/.dissy/config.dump")

	self.defaults = {}

	self.defaults["insnFgColor"] = "blue"
	self.defaults["highLevelCodeFgColor"] = "grey50"
	self.defaults["showHighLevelCode"] = True
	self.defaults["objdump"] = "objdump"
	self.defaults["readelf"] = "readelf"
	self.defaults["nm"] = "nm"
	self.defaults["version"] = PROGRAM_VERSION

	self.restoreAllDefaults()

    def restoreAllDefaults(self):
	self.insnFgColor = self.getDefault("insnFgColor")
	self.highLevelCodeFgColor = self.getDefault("highLevelCodeFgColor")
	self.showHighLevelCode = self.getDefault("showHighLevelCode")
	self.objdump = self.getDefault("objdump")
	self.readelf = self.getDefault("readelf")
	self.nm = self.getDefault("nm")

    def copy(self, other):
	self.insnFgColor = other.insnFgColor
	self.highLevelCodeFgColor = other.highLevelCodeFgColor
	self.showHighLevelCode = other.showHighLevelCode
	self.objdump = other.objdump
	self.readelf = other.readelf
	self.nm = other.nm

    def getDefault(self, which):
	return self.defaults[which]

    def load(self):
	try:
	    f = open(self.configfile)
	    other = cPickle.load(f)
	    f.close()
	    self.copy(other)
	except IOError:
	    pass
    def save(self):
	try:
	    os.makedirs(os.path.dirname(self.configfile), 0700)
	except OSError:
	    # Already exists
	    pass
	f = open(self.configfile, "w")
	cPickle.dump(self, f)
	f.close()


config = Config()

# Load the old configuration
config.load()