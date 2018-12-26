#!/usr/bin/python
from argparse import ArgumentParser
import requests
import json
import urllib2
import os

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
parser.add_argument("-g", "--gallery", dest="gallery",
                            help="provide gallery hash e.g. \"x3z0vpj\"", metavar="GALLERY")
parser.add_argument("-a", "--auth", dest="authkey",
                            help="provide authorisation API key", metavar="AUTH")
parser.add_argument("-s", "--save", dest="savekey", 
                            help="store authorisation API key", metavar="SAVE")

args = parser.parse_args()
if args.gallery is None:
    parser.print_help()
elif args.authkey is None and not os.path.isfile('./authkey.txt'):
    parser.print_help()
else:
    if args.authkey is None and os.path.isfile('./authkey.txt'):
        with open('./authkey.txt','r') as authfile:
            authkey = authfile.read()
    else:
        authkey = args.authkey
    if not args.savekey is None:
        authfile = open('./authkey.txt', 'w')
        authfile.write(authkey)

    url = "https://api.imgur.com/3/gallery/" + args.gallery
    payload = {}
    headers = {
              'Authorization': 'Client-ID ' + authkey
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

