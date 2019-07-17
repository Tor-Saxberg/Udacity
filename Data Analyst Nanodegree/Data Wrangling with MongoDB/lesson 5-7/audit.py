"""
Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should not be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}
    for field in fields:
        fieldtypes[field] = set()
    with open(filename,'r') as f:
        reader = csv.DictReader(f)
        ignored_rows = [next(reader) for i in range(0,3)] # ignore first 3 rows
        for row in reader:
            for field in fields:
                if row[field] == 'NULL' or row[field]=='': fieldtypes[field].add(type(None))
                elif row[field].startswith('{'): fieldtypes[field].add(type([]))
                else: 
                    try:
                        test = int(row[field])
                        fieldtypes[field].add(type(1))
                    except ValueError: 
                        try: 
                            test = float(row[field])
                            fieldtypes[field].add(type(1.1))
                        except ValueError: fieldtypes[field].add(type(""))

    #print fieldtypes
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)
    #print type(None)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()

