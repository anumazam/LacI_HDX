#!/usr.bin/python

from pymol import cmd
import sys
import os

os.chdir('/Users/anumglasgow/Dropbox/Research/Data/HDX/20200922_compile_rates')

input_structure = "2P9H"

#cmd.fetch(input_structure)

def color_peptide(first_pos, last_pos):
#    cmd.orient()
    peptide = "resi " + first_pos + "-" + last_pos
    cmd.color("yellow",peptide)

cmd.extend("color_peptide", color_peptide)
