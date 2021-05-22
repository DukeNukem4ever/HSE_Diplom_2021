import numpy as np
import pandas as pd

both_files = pd.read_csv('merged_syntax_selected_both_tasks_normalized.csv','r',delimiter=',',encoding='utf-8-sig')
graph_files = pd.read_csv('merged_syntax_selected_graph_normalized.csv','r',delimiter=',',encoding='utf-8-sig')
opinion_files = pd.read_csv('merged_syntax_selected_opinion_normalized.csv','r',delimiter=',',encoding='utf-8-sig')


def numpy_correlation(dataset, filename):

    new_names = []

    for b in dataset.columns:
        if b != 'name' and b != 'num_of_errors':
            new_names.append(b)


    results_numpy = pd.DataFrame()

    correlation_scores = []

    for bc in list(new_names):
        r_coef = np.corrcoef(dataset['num_of_errors'], dataset[str(bc)])
        correlation_scores.append(round(r_coef[0][1],7))

    # print(correlation_scores)


    results_numpy['parameter'] = new_names
    results_numpy['correlation score'] = correlation_scores

    results_numpy.to_csv(filename, sep=',', index = False)

numpy_correlation(both_files, 'numpy_correlation_both.csv')
numpy_correlation(graph_files, 'numpy_correlation_graph.csv')
numpy_correlation(opinion_files, 'numpy_correlation_opinion.csv')
