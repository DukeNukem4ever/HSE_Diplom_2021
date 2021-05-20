from sklearn import preprocessing
import numpy as np
import pandas as pd

both_descriptions = pd.read_csv('merged_syntax_selected_both_tasks.csv','r',encoding='utf-8', delimiter=',')
graph_description = pd.read_csv('merged_syntax_selected_graph.csv','r',encoding='utf-8', delimiter=',')
argument_description = pd.read_csv('merged_syntax_selected_opinion.csv','r',encoding='utf-8', delimiter=',')
scaler = preprocessing.MinMaxScaler()
names_1 = graph_description.columns
names_2 = argument_description.columns

both_descriptions[[
     'num_coord',
     'num_noun_inf',
     'num_part_noun',
     'num_poss',
     'num_tu']] = scaler.fit_transform(both_descriptions[[
                                                          'num_coord',
                                                          'num_noun_inf',
                                                          'num_part_noun',
                                                          'num_poss',
                                                          'num_tu']])


graph_description[[
     'num_coord',
     'num_noun_inf',
     'num_part_noun',
     'num_poss',
     'num_tu']] = scaler.fit_transform(graph_description[[
                                                          'num_coord',
                                                          'num_noun_inf',
                                                          'num_part_noun',
                                                          'num_poss',
                                                          'num_tu']])


argument_description[[
     'num_coord',
     'num_noun_inf',
     'num_part_noun',
     'num_poss',
     'num_tu']] = scaler.fit_transform(argument_description[[
                                                          'num_coord',
                                                          'num_noun_inf',
                                                          'num_part_noun',
                                                          'num_poss',
                                                          'num_tu']])

scaled_df_1 = pd.DataFrame(both_descriptions, columns=names_1)
scaled_df_2 = pd.DataFrame(graph_description, columns=names_2)
scaled_df_3 = pd.DataFrame(argument_description, columns=names_2)

scaled_df_1.to_csv(
    r'merged_syntax_selected_both_tasks_normalized.csv', index = False)
scaled_df_2.to_csv(
    r'merged_syntax_selected_graph_normalized.csv', index = False)
scaled_df_3.to_csv(
    r'merged_syntax_selected_opinion_normalized.csv', index = False)
