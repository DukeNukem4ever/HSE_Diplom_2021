import numpy as np
import pandas as pd

both_files = pd.read_csv('merged_syntax_selected_both_tasks_normalized.csv','r',delimiter=',',encoding='utf-8-sig')
graph_files = pd.read_csv('merged_syntax_selected_graph_normalized.csv','r',delimiter=',',encoding='utf-8-sig')
opinion_files = pd.read_csv('merged_syntax_selected_opinion_normalized.csv','r',delimiter=',',encoding='utf-8-sig')


import scipy.stats


def pandas_correlation(dataset, filename):

    new_names = []

    for b in dataset.columns:
        if b != 'name' and b != 'num_of_errors':
            new_names.append(b)

    results_pandas = pd.DataFrame()

    pearson_coef = []

    for bc in list(new_names):
        pearson_coef.append(dataset['num_of_errors'].corr(dataset[str(bc)]))

    results_pandas['parameter'] = new_names
    results_pandas['Pearson\'s coefficient'] = pearson_coef


    results_pandas.to_csv(filename, sep=',', index = False)
    

pandas_correlation(both_files, 'pandas_correlation_both.csv')
pandas_correlation(graph_files, 'pandas_correlation_graph.csv')
pandas_correlation(opinion_files, 'pandas_correlation_opinion.csv')

