#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def problem(k_val):
	if lower.search(k_val): return True
	elif lower_colon.search(k_val): return True
	elif problemchars.search(k_val): return True
	else: return False 

def shape_element(element):
 	#print '\t \t new element'
	if 'node' not in element.tag and \
		 'way' not in element.tag: return None

	else:
		node = {}

		for name,val in element.attrib.items():

			if element.tag == 'node': node['type'] = 'node'
			else: node['type'] = 'way'
	
			if name in CREATED: 
				if 'created' not in  node.keys(): node['created'] = {}
				node['created'][name] = val
			elif name == 'lat' or name == 'lon': 
				if 'pos' not in node.keys(): node['pos'] = [0,0]
				if name == 'lat': node['pos'][0] = (float(val))
				if name == 'lon': node['pos'][1] = (float(val))
			else: node[name] = val

		for child in element.getchildren():
			#print "\t new child"
			if 'tag' == child.tag:
				k = child.attrib['k']
				v = child.attrib['v']
				#if problem(v): 
					#print "\t\t\t\t\t\t\t\t [{}]".format(v)
				if not k.startswith('addr'):
					 node[k] = v
				else:
					if 'address' not in node.keys(): node['address'] = {}
					k_vals =  k.split(":")
					if len(k_vals) == 1: node['address'][k] = v
					elif len(k_vals) == 2: 
						node['address'][k_vals[1]] = v

			if 'nd' == child.tag:
				ref = child.attrib['ref']
				if 'node_refs' not in node.keys(): node['node_refs'] = []
				node['node_refs'].append(ref)
		return node

def process_map(file_in, pretty = False):
	file_out = "{0}.json".format(file_in)
	data = []
	with codecs.open(file_out, "w") as fo:
		for _, element in ET.iterparse(file_in):
			el = shape_element(element)
			if el:
				data.append(el)
				if pretty:
					fo.write(json.dumps(el, indent=2)+"\n")
				else:
					fo.write(json.dumps(el) + "\n")
	return data

def dict_diff(dict_a, dict_b):
    return dict([
        (key, dict_b.get(key, dict_a.get(key)))
        for key in set(dict_a.keys()+dict_b.keys())
        if (
            (key in dict_a and (not key in dict_b or dict_a[key] != dict_b[key])) or
            (key in dict_b and (not key in dict_a or dict_a[key] != dict_b[key]))
        )
    ])

def test():
	data = process_map('example.osm', True)

	correct_first_elem = {
		"id": "261114295",
		"visible": "true",
		"type": "node",
		"pos": [41.9730791, -87.6866303],
		"created": {
			"changeset": "11129782",
			"user": "bbmiller",
			"version": "7",
			"uid": "451048",
			"timestamp": "2012-03-28T18:31:23Z"
		}
	}
	assert data[0] == correct_first_elem
	assert data[-1]["address"] == {
									"street": "West Lexington St.",
									"housenumber": "1412"
									  }
	assert data[-1]["node_refs"] == [ "2199822281", "2199822390",
"2199822392", "2199822369",  "2199822370", "2199822284", "2199822281"]

if __name__ == "__main__":
	test()

