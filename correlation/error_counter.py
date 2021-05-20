import os
import re
import pandas as pd
import csv
import json

errors_1 = []
errors_2 = []

start_path = './Exam2014'
for root, dirs, files in os.walk(start_path):

    print('Где мы сейчас:', root)
    for file in files:
        if file.endswith('.ann'):
            with open(os.path.join(root, file),'r',encoding='utf-8-sig') as opened:
                open_file = opened.read()
                file_analyzed = {}
                file_analyzed['name'] = re.sub('.ann','.txt',file)
                find_mistakes = re.findall(r"Agreement_errors|Confusion_of_structures|Word_order|Emphatic|Cleft|Interrogative|Standard|Attributes|Attr_participial|Parallel_construction|Negation|Comparative_", open_file)                
                file_analyzed['num_of_errors'] = len(find_mistakes)

                if file.endswith('_1.ann'):
                    errors_1.append(file_analyzed)
                else:
                    errors_2.append(file_analyzed)

errors_all = errors_1 + errors_2

with open('error_table_synt_all.csv',
              'w') as f:
        keys = ['name',
                'num_of_errors']
        
        w = csv.DictWriter(f, keys, lineterminator='\n')
        w.writeheader()
        w.writerows(errors_all)

with open('error_table_synt_graph.csv',
              'w') as f:
        keys = ['name',
                'num_of_errors']
        
        w = csv.DictWriter(f, keys, lineterminator='\n')
        w.writeheader()
        w.writerows(errors_1)

with open('error_table_synt_opinion.csv',
              'w') as f:
        keys = ['name',
                'num_of_errors']
        
        w = csv.DictWriter(f, keys, lineterminator='\n')
        w.writeheader()
        w.writerows(errors_2)
