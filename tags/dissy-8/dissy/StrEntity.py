######################################################################
##
## Copyright (C) 2006,  Blekinge Institute of Technology
##
## Filename:      StrEntity.py
## Author:        Simon Kagstrom <ska@bth.se>
## Description:   String entity
##
## $Id: StrEntity.py 21087 2009-01-31 06:36:19Z ska $
##
######################################################################
from dissy.Entity import Entity

class StrEntity(Entity):
    def __init__(self, fn, string):
	self.string = string
	self.function = fn

    def getFunction(self):
	return self.function

    def __str__(self):
	return self.string
