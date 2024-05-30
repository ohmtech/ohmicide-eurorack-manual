#!/usr/bin/env python3
#
#     configure.py
#     Copyright (c) 2024 Raphael DINGE
#
#Tab=3########################################################################


##### IMPORT #################################################################

from __future__ import print_function
import os
import sys
import subprocess

PATH_THIS = os.path.abspath (os.path.dirname (__file__))



##############################################################################

if sys.version_info < (3, 7):
   print ('This script requires python 3.7 or greater.', file = sys.stderr)
   sys.exit (1)



"""
==============================================================================
Name : build
==============================================================================
"""

def build ():
   os.chdir (PATH_THIS)

   subprocess.check_call (
      ['make', 'clean']
   )

   subprocess.check_call (
      ['make', 'html']
   )



##############################################################################

if __name__ == '__main__':
   try:
      sys.exit (build ())

   except subprocess.CalledProcessError as error:
      print ('Configure command exited with %d' % error.returncode, file = sys.stderr)
      sys.exit (1)
