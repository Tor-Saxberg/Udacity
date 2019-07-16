#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Let's assume that you combined the code from the previous 2 exercises with code
from the lesson on how to build requests, and downloaded all the data locally.
The files are in a directory "data", named after the carrier and airport:
"{}-{}.html".format(carrier, airport), for example "FL-ATL.html".

The table with flight info has a table class="dataTDRight". Your task is to
use 'process_file()' to extract the flight data from that table as a list of
dictionaries, each dictionary containing relevant data from the file and table
row. This is an example of the data structure you should return:

data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}
]

Note - year, month, and the flight data should be integers.
You should skip the rows that contain the TOTAL data for a year.

There are couple of helper functions to deal with the data files.
Please do not change them for grading purposes.
All your changes should be in the 'process_file()' function.

The 'data/FL-ATL.html' file in the tab above is only a part of the full data,
covering data through 2003. The test() code will be run on the full table, but
the given file should provide an example of what you will get.
"""
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
from pprint import pprint

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """
    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]
    """
    data = []
    info = {}
    
    info["courier"], info["airport"] = f[:6].split("-")
    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html, 'lxml')
        for tr in soup('tr', class_='dataTDRight'): 
            if tr(string='TOTAL'): # exclude some rows
                continue
            
            td_list = tr('td')
            info['year'] = int(td_list[0].text)
            info['month'] = int(td_list[1].text)
            
            flights = {}
            flights['domestic'] =  int(td_list[2].text.replace(',',''))
            flights['international'] = int(td_list[3].text.replace(',',''))
            info['flights'] = flights

            data.append(info)
    return data

def test():
    print "Running a simple test..."
    """
    open_zip(datadir)
    files = process_all(datadir)
    data = []
    # Test will loop over three data files.
    for f in files:
        data += process_file(f)
    """
    data = process_file(FL-ATL.html)
    
    assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
if __name__ == "__main__":
    test()
