#!/usr/bin/python
import os
import re
import sys

## Its not a Bug 🐮
## mxbit@yahoo.com


## Hint for Terminal Usage
## ______________________
## to split grep lines use
## tr ' ' '\n' | grep -xxx
## cut with trim, grep -v
## xargs into pacman -U


cwd = os.getcwd()+'/'
file = str(cwd) + sys.argv[1]
deptxt = cwd+"dependencies.txt"


##CleanOld
if os.path.exists(deptxt):
  os.remove(deptxt)

deps=open("deps.txt", 'w')
opts=open("opts.txt", "w")

pkgb = open(file, 'r')
pkgtext = pkgb.readlines()

for line in pkgtext:
  if re.search("depends", line):
    deps.write(line + "\n")
  if re.search("optdepends", line):
    opts.write(line + "\n")

dipants = ""
deps = open("deps.txt", 'r')
depstext = deps.readlines()


for idx,lines in enumerate(depstext):
  #print(lines)
  if idx >= 1:
    dipants = dipants + lines


## Create the young PänzList
pantslist = dipants.split(" ")


#Expecting smth. like that in Arch-PKGBUILD linux-5.4.17.1
#var1
#depends=('pacman>=5.2.0' google-chrome-developer nvidia-420x)
#var2
#depends=(python3-ml python-neurolinguistic Ruby-rulez python3-deep-learn)
#var3
#optdepends=(git-clone wget pgp-hash proxy-changer)


## thePänz
## kleene
###########

#Cleanup
#Strip left pants
index=0
for i in pantslist[0][index]:
  while "(" != pantslist[0][index] and index <= len(pantslist[0]):
    index+=1
    continue
  if "(" == pantslist[0][index] and index <= len(pantslist[0]):
    pantslist[0] = pantslist[0][index:]
    break

#Strip right pants
index=0
for i in pantslist[-1][index]:
  while ")" != pantslist[-1][index]:
    index+=1
    continue
  if ")" == pantslist[-1][index]:
    pantslist[-1] = pantslist[-1][:index-1]
    break


output=""
deps.close()
open("dependencies.txt", 'w').close()
deps = open("deps.txt", 'w')


for s in pantslist:
  deps.write(s+" ")
  output+=s+" "


deps.close()
sys.stdout.write(output)
sys.exit()
