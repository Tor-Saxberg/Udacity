#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint

def process_map(filename):
    # how many unique users have contributed to 
    # the map in this particular area?
    
    users = set()
    for _, element in ET.iterparse(filename):
        if element.get('user'):
            users.add(element.get('user'))
    
    print users
    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()