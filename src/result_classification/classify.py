## TODO: loop iteration is broken! 

import pandas as pd

data = pd.read_csv("src/master.csv", index_col=[0]).sort_index()

output = []
excluded = []

for index, row in data.iterrows(): 
    if ".gov" in row["Domain"]:
        data = data.drop(labels = index, axis=0)
        excluded.append({
            "Domain": row["Domain"]
        })

    elif ".org" in row["Domain"]:
        print(f'Dropping the domain "{data.iloc[index]["Domain"]}" (crit1; .org)')
        excluded.append({
            "Domain": row["Domain"]
        })

    elif (str("Da Nang") in str(row["Site title"])) or (str("Da Nang") in str(row["Web snippet"])):
        print(f'Dropping the domain "{data.iloc[index]["Domain"]}" (crit2; da nang)')
        excluded.append({
            "Domain": row["Domain"]
        })
        
    elif str("news") in str(row["URL"]):
        print(f'Dropping the domain "{data.iloc[index]["Domain"]}" (crit2; news)')
        excluded.append({
            "Domain": row["Domain"]
        })

    else: 
        output.append({
            "Domain": row["Domain"]
        })

pd.DataFrame(output).drop_duplicates().to_csv("src/result_classification/output.csv")
pd.DataFrame(excluded).drop_duplicates().to_csv("src/result_classification/excluded.csv")
