# Determines the "goodness" of a search term based on the % of first page results which match criteria

import pandas as pd 
import requests, json, lxml
from bs4 import BeautifulSoup

hit_list = ["buy","sale","delivery","purchase","quick","24/7", "$", "fast", "charger"]

df = pd.read_csv("src/query_exploration/queryexploration_clean.csv") 

queries = df["title"].to_list()

del queries[:280]

results = []

for query in queries: 
    # Set the query parameters
    query_params = {
        "q": query, # query example
        "hl": "en",          # language
        "gl": "au"         # country of the search, UK -> United Kingdom
    }
    # Set the query headers
    query_headers = {
        "User-Agent": "Chrome/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    html = requests.get("https://www.google.com/search", params=query_params, headers=query_headers)

    soup = BeautifulSoup(html.text, 'lxml')

    print(soup)

    data=[]
        
    for result in soup.select(".tF2Cxc"):
        title = result.select_one(".DKV0Md").text
        try:
            snippet = result.select_one(".lEBKkf span").text
        except:
            snippet = None
        links = result.select_one(".yuRUbf a")["href"]
        
        data.append(title)

    hit_count = 0

    for item in data: 
        if [ele for ele in hit_list if(ele in item.lower())]:
            hit_count += 1
        else:
            print(item)

    if len(data) == 0:
        break

    print(query_params["q"])
    print(str(hit_count/len(data)*100) + "% of these results fit criteria for sale sites")

    results.append({
        "name": query_params["q"],
        "percent": hit_count/len(data)*100
    })

print(results)

df = pd.DataFrame(results)

df.to_csv("output4.csv")

