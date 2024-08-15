## Scrape the first 2 pages of google results for all queries in queries_final.csv

import pandas as pd 
import requests, json, lxml
from bs4 import BeautifulSoup

queries_path = "src/query_exploration/queries_final.csv"
num_pages = 2
query_headers = {
    "User-Agent": "Chrome/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

queries = pd.read_csv(queries_path)["name"].to_list()

data=[]
term_num = 1

for term in queries: 
    page = 0
    while page < num_pages: 
        query_params = {
        "q": term, # query example
        "hl": "en",          # language
        "gl": "au",         # country of the search, UK -> United Kingdom
        "start": page
        }

        html = requests.get("https://www.google.com/search", params=query_params, headers=query_headers)

        soup = BeautifulSoup(html.text, 'lxml')
        
        # If there are no results (i.e. mr google has blocked me)
        if len(soup.select(".tF2Cxc")) == 0: 
            break

        for result in soup.select(".tF2Cxc"):
            title = result.select_one(".DKV0Md").text
            try:
                snippet = result.select_one(".VwiC3b span").text
            except:
                snippet = None
            links = result.select_one(".yuRUbf a")["href"]
        
            data.append({
                "Search term": term, 
                "page": page,
                "Site title": title,
                "Web snippet": snippet,
                "URL": links
            })

        page += 1

    print("Finished for term: \"" + str(term) + "\" (" + str(term_num) + " of " + str(len(queries)) + ")")
    term_num += 1

pd.DataFrame(data).to_csv("src/google/google_output.csv")


        