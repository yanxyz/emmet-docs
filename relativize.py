#!/bin/python
# -*- coding: utf-8 -*-
# Ivan Yan
# 2013-10-11
# Relativize absolute paths in emmet-docs

from __future__ import unicode_literals

import os
import re

def relativize(filename, rel):
	old = open(filename).read().decode('utf-8')
	# href="/..." src="/..."
	def repl(matchobj):
		return matchobj.group(1) + '="' + rel + '/'
	new = re.sub(r'(href|src)="/(?!/)', repl, old)
	if new != old:
		open(filename, 'wb').write(new.encode('utf-8'))

def main(dirname):
	rootpath = os.path.abspath(dirname)
	for root, dirs, files in os.walk(rootpath):
		for dirname in dirs:
			curdir = os.path.abspath(os.path.join(root, dirname))
			index = os.path.join(curdir, 'index.html')
			if dirname != 'codemirror-movie' and os.path.exists(index):
				print(curdir)
				rel = os.path.relpath(rootpath, curdir).replace('\\', '/')
				# print(rel)
				relativize(index, rel)

if __name__ == '__main__':
	relativize('out/index.html', '.')
	main('out')