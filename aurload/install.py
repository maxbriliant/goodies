#!/usr/bin/env python

#©MxBit2020
#Enjoy

import shutil
import os,stat,sys
import getpass
import subprocess

cwd = os.getcwd()+'/'

shutil.copy(cwd + "aurload.py", '/usr/bin/')
shutil.move('/usr/bin/aurload.py' , '/usr/bin/aurload')
os.chmod('/usr/bin/aurload', 557)




