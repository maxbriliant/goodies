#!/usr/bin/python
import time
import tarfile
import shutil
import os
import wget
import glob
import sys

##MxBit@2020
from sh import gunzip
from datetime import datetime

timeObj = datetime.now()

cwd = os.getcwd()
srcPath = os.path.abspath(__file__)

srcDir = os.path.dirname(srcPath)
os.chdir(srcDir)

globcwd = glob.glob(srcDir+"/bauer*")
globtmp = glob.glob("/tmp/bauer*")
globtar = glob.glob(srcDir+"/*.tar")

bar = "|==================>"

for zip1 in globcwd:
    try:
      os.remove(zip1)
    except:
      print("")
      shutil.rmtree(zip1)

for zip2 in globtmp:
    os.remove(zip2)

for zip3 in globtar:
    try:
      os.remove(zip3)
    except:
      print("")

timestamp = " " +  str(timeObj.time())[:-10]

print(timestamp + " wget mxPython ->" )

url = 'https://aur.archlinux.org/cgit/aur.git/snapshot/bauerbill.tar.gz'
## WGET from AUR Source Repository
file = wget.download(url,out="/tmp")


print("\n  -> todo: remove header")

fileName = str(file)
fileName = fileName[4:]

for progress in bar:
  print(progress, end='', flush=True)
  time.sleep(0.138)


print(" "+ str(file) +" "+ timestamp +"   Downloaded from AUR well Done!!")

tmpPath = str(file)
newPath = srcDir+fileName
shutil.copy(tmpPath, newPath)
gunzip(srcDir+"/bauerbill.tar")
unzipped = (srcDir + "/bauerbill.tar")
extr = tarfile.open(name=unzipped, mode='r')
extr.extractall()

print(bar + " Extracted "+fileName+" into "+ srcDir+ fileName +"   Amazing!!")


#tarfile.extract(name=file)

#os.chdir(r, './%s', % file)
#print('./%s', %s file)

