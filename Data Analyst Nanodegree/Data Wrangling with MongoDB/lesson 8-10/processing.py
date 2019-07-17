import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


def process_file(filename, fields):

    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for list in reader:
            data_row = {}
            classification = {'family': '',
                             'class'  : '',
                             'phylum' : '',
                             'order'  : '',
                             'kingdom': '',
                             'genus'  : ''}
                                
            for field in process_fields:
                                                                # fill classification
                if FIELDS[field] in classification.keys():              
                    classification[FIELDS[field]] = list[field].strip()
                                                                # fill other fields
                elif field in FIELDS.keys():                   
                    data_row[FIELDS[field]] = list[field].strip()
                                                                # replace data_row "NULL" to None
                if field in data_row.keys() and data_row[FIELDS[field]] == 'NULL':           
                    data_row[FIELDS[field]] = None
                                                                # replace classification "NULL" to None
                elif FIELDS[field] in classification.keys() \
                        and classification[FIELDS[field]] == 'NULL':
                    classification[FIELDS[field]] = None
                    
            data_row['classification'] = classification         
                                                                # remove redundant
            if '(' in data_row['label']:                        
                data_row['label'] = data_row['label'].split('(')[0].strip()
                                                                # replace name if non-alphanumeric
            if data_row['name'] == None or not data_row['name'].isalnum():
                data_row['name'] = data_row['label']            
                                                                # split synonym into list
            if data_row['synonym'] != None:                     
                data_row['synonym'] = data_row['synonym'].lstrip('{').rstrip('}').split('|')
            
            data.append(data_row)
                    
    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)
    print "first entry:"
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None, 
        "name": "Argiope", 
        "classification": {
            "kingdom": "Animal", 
            "family": "Orb-weaver spider", 
            "order": "Spider", 
            "phylum": "Arthropod", 
            "genus": None, 
            "class": "Arachnid"
        }, 
        "uri": "http://dbpedia.org/resource/Argiope_(spider)", 
        "label": "Argiope", 
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

if __name__ == "__main__":
    test()
