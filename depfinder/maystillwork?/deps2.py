#!/usr/bin/python
##MxBit@2020
import os
import re
import sys



## to split grep lines use
## tr ' ' '\n' | grep -XXX



cwd = os.getcwd()+'/'

file = str(cwd) + sys.argv[1]
deptxt = cwd+"dependencies.txt"

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

#deps.close()
deps = open("deps.txt", 'r')
depstext = deps.readlines()

dipanz = ""

for idx,lines in enumerate(depstext):
  #print(lines)
  if idx >= 1:
    dipanz = dipanz + lines

panzlist = dipanz.split(" ")

#var1
#depends=('pacman>=5.2.0' pbget pm2ml powerpill python-xdg python3 python3-aur python3-colorsysplus python3-memoizedb python3-xcgf python3-xcpf)
#var2
#depends=(pyalpm python-xdg python3 python3-xcgf python3-xcpf)


index=0
for i in panzlist[0][index]:
  while "(" != panzlist[0][index] and index <= len(panzlist[0]):
    index+=1
    continue
  if "(" == panzlist[0][index] and index <= len(panzlist[0]):
    index-=1
    panzlist[0] = panzlist[0][index:]
    break


index=0
for i in panzlist[-1][index]:
  while ")" != panzlist[-1][index]:
    index+=1
    continue
  if ")" == panzlist[-1][index]:
    panzlist[-1] = panzlist[-1][:index-1]
    break

deps.close()
open("dependencies.txt", 'w').close()
deps = open("deps.txt", 'w')

output=""

for s in panzlist:
  deps.write(s+" ")
  output+=s+" "

deps.close()


sys.stdout.write(output)
sys.exit()
