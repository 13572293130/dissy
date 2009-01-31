######################################################################
##
## Copyright (C) 2006,  Blekinge Institute of Technology
##
## Filename:      Entity.py
## Author:        Simon Kagstrom <ska@bth.se>
## Description:   Entity (address, size etc.)
##
## $Id: Entity.py 8505 2006-06-13 09:28:22Z ska $
##
######################################################################
class Entity:
    def __init__(self):
	pass


class AddressableEntity(Entity):
    def __init__(self, address=0, baseAddress = 0, endAddress = 0):
	self.label = ""
	self.address = address + baseAddress
	self.baseAddress = baseAddress
	if endAddress == 0:
	    self.endAddress = self.address
	else:
	    self.endAddress = endAddress + baseAddress

    def getAddress(self):
	return self.address

    def getLabel(self):
	return self.label

    def getExtents(self):
	"Return the extents of this function"
	return (self.address - self.baseAddress, self.endAddress - self.baseAddress)

    def setSize(self, size):
	"Set the size of this entity"
	self.endAddress = self.address + size

    def getSize(self):
	return self.endAddress - self.address
