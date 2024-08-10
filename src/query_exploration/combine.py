# Combines the output csv's

import pandas as pd 

output0 = pd.read_csv("src/query_exploration/output0.csv")
output1 = pd.read_csv("src/query_exploration/output1.csv")
output2 = pd.read_csv("src/query_exploration/output2.csv")
output3 = pd.read_csv("src/query_exploration/output3.csv")
output4 = pd.read_csv("src/query_exploration/output4.csv")

dfs = [output0, output1, output2, output3, output4]

df = pd.concat(dfs).drop_duplicates(subset = "name").drop(labels='Unnamed: 0', axis=1).sort_values('percent', ascending=False)

df.to_csv("src/query_exploration/output_clean.csv")