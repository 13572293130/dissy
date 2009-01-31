######################################################################
##
## Copyright (C) 2006,  Blekinge Institute of Technology
##
## Filename:      ppc.py
## Author:        Andrew May <acmay [at] acmay [dot] homeip [dot] net>
## Description:   PPC arch specific stuff
##
## $Id: ppc.py 12331 2006-11-22 06:41:47Z ska $
##
######################################################################
import sys, architecture
from dissy.architecture import Architecture

ppc_jumps = [
	      'beq',
	      'bne',
	      'bge',
	      'b',
	      'bl',
	      'beq-',
	      'bne-',
	      'bge-',
	      'blt-',
	      'ble-',
	      'b-',
	      ]

ppc_calls = ['bl']


class PpcArchitecture(Architecture):
    def __init__(self):
	Architecture.__init__(self, ppc_jumps, ppc_calls)
