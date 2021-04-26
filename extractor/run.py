#!/usr/bin/env python

import os
import sys

lib_path = os.path.realpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'lib'))
if lib_path not in sys.path:
	sys.path[0:0] = [lib_path]

import utils
import os
import argparse
import subprocess
import requests
def extract(site_data):
	name=site_data[3]
	start=site_data[0]
	base=site_data[1]
	proc=site_data[2]
	return(name,start,base,proc)

def main(args):
	extractor = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'extractor.coffee')
	path = utils.get_data_path(args.site[0])
    	#urls = utils.load_urls(path)	print(path)
	name=[]
	start=[]
	base=[]
	proc=[]
	urls=[]
	site_data= requests.get("http://1.7.151.12:8181/api/scraper_api/fetch_links.php").json()
	for sd in site_data:
		name ,start, base, proc=extract(sd)
		urls.append(base)
    	# extract data from each url
	for id, url in enumerate(urls):
		url = url.strip()
		if not url:
            		continue

        	# skip already extracted
		if os.path.exists(os.path.join(path, '%03d.json' % id)):
            		continue

		print('[extractor] #%03d: %s' % (id, url))
		subprocess.call('cd "%(path)s" && phantomjs "%(extractor)s" "%(url)s" "%(label)03d" > "%(label)03d.log" 2>&1' % {
            	'path': path,
            	'extractor': extractor,
            	'url': url,
            	'label': id,
        	}, shell=True)

def parse_args():
	"""
    	Parse command line arguments
   	 """
	parser = argparse.ArgumentParser(description='Extract site pages.')
	parser.add_argument('site', metavar='site', type=str, nargs=1, help='site id, for example: theverge, npr, nytimes')
	return parser.parse_args()

if __name__ == '__main__':
	main(parse_args())
