#!/usr/bin/env python

import os
import sys

lib_path = os.path.realpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'lib'))
if lib_path not in sys.path:
    sys.path[0:0] = [lib_path]

import utils
import clusterers
import processors
import simplejson as json
import os
import argparse
import requests	
def extract(site_data):
    name=site_data[3]
    start=site_data[0]
    base=site_data[1]
    proc=site_data[2]
    return(name,start,base,proc)

def main(args):

    path = utils.get_data_path(args.site[0])
    urls = utils.load_urls(path)
    '''name=[]
    start=[]
    base=[]
    proc=[]
    urls=[]
    site_data= requests.get("http://1.7.151.12:8181/api/scraper_api/fetch_links.php").json()
    for sd in site_data:
        name ,start, base, proc=extract(sd)
        urls.append(base)'''

    for count in range(2, len(urls) + 1):

        print('[learner] clustering with %d urls' % count)

        # load data
        data = [utils.load_data(path, id) for id, url in enumerate(urls)]
        data = data[:count]

        # process data
        processor = processors.Processor(data)
        features = processor.extract()

        # clustering
        clusterer = clusterers.DBSCAN()
        labels = clusterer.cluster(features).labels_

        # score
        clusters = processor.score(labels)
        
        with open(os.path.join(path, 'clusters.%03d.json' % count), 'w') as f:
            f.write(json.dumps(clusters, indent=2, ensure_ascii=False).encode('utf8'))

def parse_args():
    """
    Parse commandline arguments
    """
    parser = argparse.ArgumentParser(description='Run the whole pipeline on site pages.')
    parser.add_argument('site', metavar='site', type=str, nargs=1, help='site id, for example: theverge, npr, nytimes')
    return parser.parse_args()

if __name__ == '__main__':
    main(parse_args())
