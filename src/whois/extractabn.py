import pandas as pd
import json
import ast

data = pd.read_csv("src/whois/registryoutput.csv", index_col=[0])

clean = []

for index, row in data.iterrows(): 
    try:
        clean.append({
            "URL": row["URL"],
            "Company": str(ast.literal_eval(row["Company"])["registrant"])
        })
    except: 
        clean.append({
            "URL": row["URL"],
            "Company": "unknown"
        })

pd.DataFrame(clean).sort_values(by=["Company"]).to_csv("src/whois/companies.csv")
