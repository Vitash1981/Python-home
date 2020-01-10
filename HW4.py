# readcsv.py -path_csv example.csv -col_name Marker_Strategy

import argparse
import csv
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-path_csv')
parser.add_argument('-col_name')
ns = parser.parse_args(sys.argv[1:])

result = []
with open(ns.path_csv) as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    result = [row[ns.col_name.replace('_', ' ')] for row in reader]
print('\n'.join(result))
