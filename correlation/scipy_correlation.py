import numpy as np
import pandas as pd

both_files = pd.read_csv('merged_syntax_selected_both_tasks_normalized.csv','r',delimiter=',',encoding='utf-8-sig')
graph_files = pd.read_csv('merged_syntax_selected_graph_normalized.csv','r',delimiter=',',encoding='utf-8-sig')
opinion_files = pd.read_csv('merged_syntax_selected_opinion_normalized.csv','r',delimiter=',',encoding='utf-8-sig')


import scipy.stats


def scipy_correlation(dataset, filename):

    new_names = []

    for b in dataset.columns:
        if b != 'name' and b != 'num_of_errors':
            new_names.append(b)

    results_scipy = pd.DataFrame()

    pearson_coef = []
    pearson_p = []
    
    for bc in list(new_names):
        pearson_coef.append(round(scipy.stats.pearsonr(dataset['num_of_errors'], dataset[str(bc)])[0],4))
        pearson_p.append(round(scipy.stats.pearsonr(dataset['num_of_errors'], dataset[str(bc)])[1],4))

    results_scipy['parameter'] = new_names
    results_scipy['Pearson\'s coefficient'] = pearson_coef
    results_scipy['Pearson\'s p-value'] = pearson_p

    results_scipy.to_csv(filename, sep=',', index = False)
    

scipy_correlation(both_files, 'scipy_correlation_both.csv')
scipy_correlation(graph_files, 'scipy_correlation_graph.csv')
scipy_correlation(opinion_files, 'scipy_correlation_opinion.csv')

#scipy_correlation(both_files, 'scipy_correlation_both.csv')


#def numpy_correlation(dataset, filename):

#    new_names = []

#    for b in dataset.columns:
#        if b != 'name' and b != 'num_of_errors':
#            new_names.append(b)


#    results_scipy = pd.DataFrame()

#    correlation_scores = []

#    for bc in list(new_names):
#        r_coef = np.corrcoef(dataset['num_of_errors'], dataset[str(bc)])
#        correlation_scores.append(round(r_coef[0][1],7))

#    print(correlation_scores)


#    results_scipy['parameter'] = new_names
#    results_scipy['correlation score'] = correlation_scores

#    results_scipy.to_csv(filename, sep=',', index = False)

#numpy_correlation(both_files, 'numpy_correlation_both.csv')
#numpy_correlation(graph_files, 'numpy_correlation_graph.csv')
#numpy_correlation(opinion_files, 'numpy_correlation_opinion.csv')
