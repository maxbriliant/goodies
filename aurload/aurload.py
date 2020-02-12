#!/usr/bin/env python
#©MxBit2020

import sys
import requests
import lxml.html
import wget
import tarfile

pkg = sys.argv[1]
element='<a href="/cgit/aur.git/snapshot/"+pkg+".tar.gz">Download snapshot</a>'

aur = 'https://aur.archlinux.org'

html = requests.get(aur + '/packages/' + pkg)
page = lxml.html.fromstring(html.content)

buildPath =  "'//a[@href=\"/cgit/aur.git/snapshot/" + pkg + ".tar.gz\"]'"

href = page.xpath(buildPath)

### example '//a[@href="/cgit/aur.git/snapshot/python3-aurtar.gz"]'
##  split on " "

href = href.split('"')
link = href[1] #always

snapshot = aur + link
print(snapshot)

targz = wget.download(snapshot)
tar = tarfile.open(targz,'r')
tar.extractall()












