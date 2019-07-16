#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    #keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    if element.tag == "tag":
        k_val = element.get('k') # check the k attribute value
        if lower.search(k_val):keys['lower'] +=1
        elif lower_colon.search(k_val):keys['lower_colon'] +=1
        elif problemchars.search(k_val): keys['problemchars'] +=1
        else: keys['other'] +=1

    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    keys = process_map('example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()
