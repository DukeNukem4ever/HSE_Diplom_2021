# HSE_Diploma_2021

Файлы для ВКР "Статистические методы исследования коррелятивности признаков автоматизированной оценки сложности текста".

## Принцип действия

1. Через программу Inspector (https://authors.elsevier.com/a/1d07s3qVb8MJRq) выводится таблица dataset_mine.csv, в которой распределяются параметры сложности.
2. Программа type_reader.py разбивает таблицу dataset_mine на две части: syntax_dataset_graph.csv и syntax_dataset_opinion.csv в зависимости от задания.
3. Параллельно с этим программа error_counter.py анализирует файлы эссе на количество ошибок; проверка проходит для обеих групп текстов. На выход получаются файлы error_table_synt_all.csv, error_table_synt_graph.csv и error_table_synt_opinion.csv.
4. Через open_file_csv.R таблицы dataset_mine, syntax_dataset_graph.csv и syntax_dataset_opinion.csv присоединяют к себе количество ошибок из таблиц error_table_synt_all.csv, error_table_synt_graph.csv и error_table_synt_opinion.csv соответственно. Затем извлекаются значения ключевых признаков (num_coord, num_poss, num_tu, num_part_noun, num_noun_inf, pos_sim_nei, lemma_sim_nei, pos_sim_all и lemma_sim_all) и сохраняются в файлы merged_syntax_selected_graph.csv, merged_syntax_selected_opinion.csv и merged_syntax_selected_both_tasks.csv.
5. Полученные из пункта 4 датасеты подвергаются нормализации через normalizer.py. На выход подаются файлы merged_syntax_selected_both_tasks_normalized.csv (для эссе из обоих заданий), merged_syntax_selected_graph_normalized.csv (для описаний графиков) и merged_syntax_selected_opinion_normalized.csv (для аргументированных эссе).
6. На основании нормализованных датасетов проводится корреляционный анализ четырьмя способами. Три из них базируются на коде Python, а одна - на R.
  1) Корреляция через пакет NumPy для языка Python (numpy_correlation.py); на выход подаёт таблицы numpy_correlation_both.csv (для эссе из обоих заданий), numpy_correlation_graph.csv (для описаний графиков) и numpy_correlation_graph.csv (для аргументированных эссе).
  2) Корреляция через пакет SciPy для языка Python (scipy_correlation.py); на выход подаёт таблицы scipy_correlation_both.csv (для эссе из обоих заданий), scipy_correlation_graph.csv (для описаний графиков) и scipy_correlation_graph.csv (для аргументированных эссе).
  3) Корреляция через пакет Pandas для языка Python (pandas_correlation.py); на выход подаёт таблицы pandas_correlation_both.csv (для эссе из обоих заданий), pandas_correlation_graph.csv (для описаний графиков) и pandas_correlation_graph.csv (для аргументированных эссе).
  4) Корреляция через пакет Psych для языка R (correlation_code.R). На вывод не подаёт ничего; все значения отображаются при последовательном запуске строк кода.
