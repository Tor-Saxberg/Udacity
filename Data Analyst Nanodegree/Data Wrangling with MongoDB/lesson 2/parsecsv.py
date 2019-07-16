#!/usr/bin/env python
import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"

def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        info = f.readline().split(',')
        name = (info[1]).strip('"')
        header = f.readline().split(',')
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data.append(row)
    # Do not change the line below
    return (name, data)

def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)
    
    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
