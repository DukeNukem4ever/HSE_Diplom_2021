import json
from csv import DictReader
import csv
import pandas as pd

type_1 = []
type_2 = []

from csv import reader
with open('dataset_mine.csv', 'r') as read_obj:
    csv_reader = DictReader(read_obj)
    for row in csv_reader:
        if row['name'].endswith('_1.txt'):
            type_1.append(row)
        elif row['name'].endswith('_2.txt'):
            type_2.append(row)


with open('syntax_dataset_graph.csv',
              'w') as f:
        keys = csv_reader.fieldnames
        
        w = csv.DictWriter(f, keys, lineterminator='\n')
        w.writeheader()
        w.writerows(type_1)

with open('syntax_dataset_opinion.csv',
              'w') as f:
        keys = csv_reader.fieldnames
        
        w = csv.DictWriter(f, keys, lineterminator='\n')
        w.writeheader()
        w.writerows(type_2)
