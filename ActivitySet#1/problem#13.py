# Network Programming
# https://www.py4e.com/lessons/network
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl, sys

url = input('Enter url: ')
count = input('Enter count: ')
position = input('Enter position: ')

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
print("Retrieving",url)
tags = soup('a')
for i in range(int(count)):
    links = []
    for tag in tags:
        links.append(str(tag.get('href', None)))
    html = urllib.request.urlopen(links[int(position)-1], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving",links[int(position)-1])
    tags = soup('a')
