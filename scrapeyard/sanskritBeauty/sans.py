#!/usr/bin/python
import os;

path = "./"

#if os.path.exists("./sanskrit.csv"):
#  os.remove("./sanskrit.csv")

file = open('sanskrit.csv','r')
file = file.readlines()
counter = 0
for line in file: counter += 1
print(counter - 8, "different words to express Beauty in Sanskrit")

