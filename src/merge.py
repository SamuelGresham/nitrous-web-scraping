import pandas as pd 

google = pd.read_csv("src/search_results_google.csv", index_col=[0])
bing = pd.read_csv("src/search_results_bing.csv", index_col=[0])

pd.concat([google, bing], ignore_index=True).sort_values(["URL"]).to_csv("src/master.csv")