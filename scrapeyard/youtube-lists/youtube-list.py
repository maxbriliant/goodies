#!/usr/bin/env python
from bs4 import BeautifulSoup
import os
import time
import random
import shutil
import urllib.request
import sys
import subprocess
import requests


filename=  "links.py"
filename2= "links.new.py"
fileExists = 0
url = sys.argv[1]
CWD = os.getcwd()


headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
domain = 'https://www.youtube.com'


#yt <a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/playlist?list=PLfW7xXS_4ePpvZLIUD31p6PgsiFOmY_SX" dir="auto">Komplette Playlist ansehen</a>

def getLinks(url, file):
   req = requests.get(url, headers=headers)
   soup = BeautifulSoup(req.content, 'html.parser')
   search = soup.find_all('a', {'class' : 'yt-simple-endpoint style-scope yt-fromatted-string'}, limit=4)
   for lines in search:
       #ran = float(0.412)*random.randint(1,8)
       #file.write(str(lines.get("href").find("playlist?List=")))
#       time.sleep(ran)
       #print("Waited " + ran + "sec\n")
       print(lines.get("href"))
   #for lines in search:
   #   file.write(lines)
   #soup = Soup(html, 'html.parser')
   #links = soup.find_all('a', attrs = {'class':'pl-video-title-link'})
   #for l in links:
   #    file.write(l.get("href"))

try:
   if os.path.exists(CWD + "/"+ filename):
      fileExists = 1
   elif os.path.exists(CWD + "/"+ filename2):
      fileExists = 2
except:
   print("No File in Exception")
   fileExists = 0


## Download
fileOld = open('links.py','w')
if fileExists == 0:
    try:
      getLinks(url, fileOld)
      print("No File in Conditions - Downloading Site")
    except Exception as e:
      print(e)


## Reading Instead
else:
   print("Reading Existing links.py\n")
   if fileExists == 1:
      fileOld = open('links.py','r')
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


   elif fileExists == 2:
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

      fileOld.close()
      fileNew.close()

## Cleanup
try:
   os.remove('links.new.py')
except:
   print("Clear")

#   os.remove('links.py')
#   time.sleep(2)

#with open('links.new.py') as f:
#   lines= f.readlines()
#print(lines)
