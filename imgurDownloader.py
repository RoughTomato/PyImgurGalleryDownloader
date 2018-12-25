#!/usr/bin/python
from argparse import ArgumentParser
import requests
import json
import urllib2

authKey = ''

def downloadFromURL(url, name):
    request = urllib2.Request(url)
    img = urllib2.urlopen(request).read()
    with open (name, 'w') as f: f.write(img)

def mimeToExtension(mime):
    def jpeg():
        return "jpg"
    def png():
        return "png"
    def gif():
        return "gif"
    mimetype = { 
        "image/jpeg" : jpeg,
        "image/png"  : png,
        "image/gif"  : gif,
    }
    return mimetype[mime]()

parser = ArgumentParser()
parser.add_argument("-u", "--url", dest="url",
                            help="provide url for the gallery", metavar="URL")

args = parser.parse_args()

url = "https://api.imgur.com/3/gallery/" + args.url
payload = {}
headers = {
          'Authorization': 'Client-ID ' + authKey
          }
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=0)

if (response == 404):
    print "Page not found"
if (response == 403):
    print "Access Denied"

data = json.loads(response.text)

for images in data['data']['images']:
    print('downloading ' + images['link'])
    downloadFromURL(images['link'],images['id'] + '.' + mimeToExtension(images['type']))
