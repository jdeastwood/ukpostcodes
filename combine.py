#! /usr/bin/env python3

"""
Combines and cleans OS CodePoint CSV files.

Expects a list of CodePoint csv files. Example usage:

./combine.py ./Codepoint/Data/CSV/* > all.csv

./combine.py ./Codepoint/Data/CSV/eh.csv ./Codepoint/Data/CSV/gl.csv > eh_and_gl.csv

"""

import sys
import re

print('inbound, outbound, area, northing, easting')

for point_file in sys.argv[1:]:
    with open(point_file, 'r') as data:
        for row in data:
            cols = row.strip().split(",")
            code, northing, easting = cols[0], cols[2], cols[3]
            code = code.replace(" ", "").replace('"', "")
            area = re.match(r'^([A-Z]{1,2})[0-9]', code).group(1)
            inbound, outbound = code[:-3], code[-3:]
            print('{},{},{},{},{}'.format(inbound, outbound, area, northing, easting))
