######################################################################
##
## Copyright (C) 2006,  Blekinge Institute of Technology
##
## Filename:      ppc.py
## Author:        Andrew May <acmay [at] acmay [dot] homeip [dot] net>
## Description:   PPC arch specific stuff
##
## $Id: ppc.py 16325 2007-10-11 09:30:50Z ska $
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
	      'beq+',
	      'bne+',
	      'bge+',
	      'blt+',
	      'ble+',
	      'b-',
	      ]

ppc_calls = ['bl']


class PpcArchitecture(Architecture):
    def __init__(self):
	Architecture.__init__(self, ppc_jumps, ppc_calls)

    def getJumpDestination(self, insn, args):
	r = args.split(",")
	if len(r) == 1:
	    return Architecture.getJumpDestination(self, insn, args)
	return Architecture.getJumpDestination(self, insn, r[-1])