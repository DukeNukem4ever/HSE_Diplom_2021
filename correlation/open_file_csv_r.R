library(dplyr)
library(stringr)

CSV1 <- read.csv("syntax_dataset_graph.csv", stringsAsFactors = FALSE)
CSV1_2 <- read.csv("error_table_synt_graph.csv", stringsAsFactors = FALSE)

CSV2 <- read.csv("syntax_dataset_opinion.csv", stringsAsFactors = FALSE)
CSV2_2 <- read.csv("error_table_synt_opinion.csv", stringsAsFactors = FALSE)


CSV4 <- read.csv("dataset_mine.csv", stringsAsFactors = FALSE)
CSV4_2 <- read.csv("error_table_synt_all.csv", stringsAsFactors = FALSE)


CSV3_1 = merge(x=CSV1,y=CSV1_2,by="name",all=TRUE)
CSV3_2 = merge(x=CSV2,y=CSV2_2,by="name",all=TRUE)
CSV3_3 = merge(x=CSV4,y=CSV4_2,by="name",all=TRUE)

CSV1
CSV1_2

CSV2
CSV2_2

CSV3_1 %>% select(name, num_of_errors, num_coord, num_poss, num_tu, num_part_noun, num_noun_inf, pos_sim_nei, lemma_sim_nei, pos_sim_all, lemma_sim_all) -> CSV3_SYNT

CSV3_SYNT

write.csv(CSV3_SYNT,"merged_syntax_selected_graph.csv", row.names = FALSE)

CSV3_2 %>% select(name, num_of_errors, num_coord, num_poss, num_tu, num_part_noun, num_noun_inf, pos_sim_nei, lemma_sim_nei, pos_sim_all, lemma_sim_all) -> CSV3_SYNT_2

CSV3_SYNT_2

write.csv(CSV3_SYNT_2,"merged_syntax_selected_opinion.csv", row.names = FALSE)

CSV3_3 %>% select(name, num_of_errors, num_coord, num_poss, num_tu, num_part_noun, num_noun_inf, pos_sim_nei, lemma_sim_nei, pos_sim_all, lemma_sim_all) -> CSV3_SYNT_3

CSV3_SYNT_3

write.csv(CSV3_SYNT_3,"merged_syntax_selected_both_tasks.csv", row.names = FALSE)
