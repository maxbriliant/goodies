#!/usr/env python
##MxBit@2020
import os
import re
import sys

cwd = os.getcwd()+'/'

file = str(cwd) + sys.argv[1]
deptxt = cwd+"dependencies.txt"

if os.path.exists(deptxt):
  os.remove(deptxt)

deps=open("dependencies.txt", 'w')
deps.write("Dependencies from " +file+ ":")

pkgb = open(file, 'r')
pkgtext = pkgb.readlines()

for line in pkgtext:
  if re.search("dep", line):
    deps.write("\n" + line + "\n")

#deps.close()
deps = open("dependencies.txt", 'r')
depstext = deps.readlines()

dipanz = ""

for idx,lines in enumerate(depstext):
  #print(lines)
  if idx >= 1:
    dipanz = dipanz + lines

panzlist = dipanz.split(" ")

index=0
for i in panzlist[0][index]:
  while "(" != panzlist[0][index]:
    index+=1
    continue
  if "(" == panzlist[0][index]:
    panzlist[0] = panzlist[0][index+1:]
    panzlist[0] = panzlist[0][1:]
    panzlist[0] = panzlist[0][:-1]
    break


index=0
for i in panzlist[-1][index]:
  while ")" != panzlist[-1][index]:
    index+=1
    continue
  if ")" == panzlist[-1][index]:
    panzlist[-1] = panzlist[-1][:index]
    break

deps.close()
open("dependencies.txt", 'w').close()
deps = open("deps.txt", 'w')

for s in panzlist:
  deps.write(s+" ")
  print(s)

deps.close()

