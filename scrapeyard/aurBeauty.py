#!/usr/bin/env python
from bs4 import BeautifulSoup
import re
import os
import time
import shutil
import urllib.request
import sys
import subprocess
import requests
import random

filename  = "links.out"
filename2 = "links.new.py"
fileMode  = 0


# ©MxBit2020
# First time
# LinkinPark


url = ""
CWD = os.getcwd()
urlset = False

domains = ['https://www.archlinux.org/packages/?repo=Testing&sort=-pkgname','https://www.archlinux.org/packages/?repo=Testing&sort=pkgname','https://www.archlinux.org/packages/?repo=Testing&sort=name','https://www.archlinux.org/packages/?repo=Testing&sort=-name'] 
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

## Personal Page
if urlset:
  domains = sys.argv[1]

## argv[1] using any link to load pkgs with:
## still *DePuzzing (Walls.txt)

## if no Link using my preconfig domains[]
## ArchLinux & Gentoo repos <3
try:
  url = sys.argv[1]
  urlset = True
except:
  print("Using Buildin Domains: "
  \+ str(domains[0][8:25]) + "..")


else:
  print("Using randomly Domain")

## onigiri QQ
def getLinks(domains, file):
   if urlset:
      dyndns  = 0   #just a dynamicly resolving ;)
      domains = url
   else:
      ## use n'th from random domains
      dyndns = int(random.randint(0,4))
      print("Setting " + str(dyndns) + ". domain from list")
      print(domains[dyndns])

   ##Add pageflip to start randomly at bottom

   req  = requests.get(domains[dyndns], headers=headers)
   ## Dont Loop that stuff
   soup = BeautifulSoup(req.content, 'lxml')

#ONLINE ^
#--- From here experimental to use
#OFLINE v  .get might still connect

   ## using  >>  "a, href" or "td, text"
   ## target packagenames  in AUR Repo
   for lines in soup.find_all('a', href=True):

       waiting = (0.421*(random.randint(1,7)))
       print("Waiting "+str(waiting)+" sec")
       time.wait(waiting)


       file.write(lines.get('href')+"\n")


#   for a in soup:
#       file.write(a.get_attribute_list('href')[0]+"\n")

#	       if waiting < 1:
#	         flipList()
#       file.write(str(k.get("href"))+"\n")

#   for l in links:
#    file.write(l.get("href"))

try:
   if os.path.exists(CWD + "/"+ filename):
      fileMode = 1
   elif os.path.exists(CWD + "/"+ filename2):
      fileMode = 2
except:
   print("No File in Exception")
   fileMode = 0


## REQUEST
fileOld = open('links.out','w')
if fileMode == 0:
    try:
      getLinks(domains, fileOld)
      print("No File in Conditions - Downloading Site")
    except Exception as e:
      print(e)



## REUSING OLD FILE
## READING Instead of Download
else:
   print("Reading Existing links.out\n")
   if fileMode == 1:
      fileOld = open('links.out','r')
      fileNew = open('links.new.py', 'w')
      fileOk  = open('links.ok.py', 'w')

      text = fileOld.readlines()
      for lines in text:
          fileNew.write(lines)

      fileNew = open('links.new.py', 'r')
      text = fileNew.readlines()
      for lines in text:
          fileOk.write(lines)

      fileOld.close()
      fileNew.close()

   elif fileMode == 2:

      fileOld = open('links.new.py','r')
      fileNew = open('links.toCopy','w')
      fileOk  = open('links.ok.py','w')
      text2 = fileOld.readlines()

      for lines in text2:
          fileNew.write(lines)
          print(lines)

      fileNew = open('links.toCopy','r')
      tex2 = fileNew.readlines()
      for lines in text:
          fileOk.write(lines)

      ##Transfer Done
      fileOld.close()
      fileNew.close()


try:  #CLEANUP
   os.remove('links.new.py')
except:
   print("Good2Go")


#   OPTIONAL
#   os.remove('links.out')
#   time.sleep(2)

#   with open('links.new.py') as f:
#   lines= f.readlines()
#   print(lines)
