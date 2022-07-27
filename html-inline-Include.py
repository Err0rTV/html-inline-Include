#!/usr/bin/python3

import sys
import base64
import magic
import re
from bs4 import BeautifulSoup

def filebase64encode(filename):
	with open(filename,mode='rb') as f:
		return base64.b64encode(f.read())

def getfilemimetype(filename):
	mime = magic.Magic(mime=False)
	return mime.from_file(filename)

def base64encodetag(soup,tagname):
	if tagname == 'script':
		src = 'src'
	else:
		src = 'href'
	r = soup.find_all(tagname)
	for e in r:
		m = e.get(src)
		if m is not None:
			param = "data:"
			if e.has_attr('include'):
				del e['include']
				if e.has_attr('type'):
					param += e.get('type')
				elif tagname.lower() == 'script':
					param += 'text/javascript'
				else:
					param += getfilemimetype(m)
				param += ";base64,"
				param += filebase64encode(m).decode('utf8')
				e[src] = param



if len(sys.argv) > 0:
	with open(str(sys.argv[1])) as fp:
		soup = BeautifulSoup(fp, 'html.parser')
		base64encodetag(soup, 'script')
		base64encodetag(soup, 'link')
		print(soup)

