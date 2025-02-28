## Scrape the first 2 pages of Bing results for all queries in queries_final.csv

import pandas as pd 
import requests, json, lxml
from bs4 import BeautifulSoup
import time
import math

queries_path = "src/query_exploration/queries_final.csv"
num_pages = 2
query_headers = {
    "User-Agent": "Chrome/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

queries = pd.read_csv(queries_path)["name"].to_list()

queries = queries

data=[]
term_num = 1

for term in queries: 
    
    query_params = {
    "q": term, # query example
    "hl": "en",          # language
    "cc": "au",         # country of the search, au -> Australia
    "count": 20
    }    

    html = requests.get("https://www.bing.com/search", params=query_params, headers=query_headers)

    soup = BeautifulSoup(html.text, 'lxml')
        
    # If there are no results (i.e. mr google has blocked me)
    if len(soup.find_all('li', class_='b_algo')) == 0: 
        print(soup.select("body"))
        break

    page = 0

    for result in soup.find_all('li', class_='b_algo'):
        try:
            title = result.find_all('a')[1].text
            url = result.find('a')['href']
            snippet= result.find('p').text

            data.append({
            "Search term": term, 
            "page": math.floor(page/10),
            "Site title": title,
            "Web snippet": snippet,
            "URL": url
            })

            page += 1
        except: 
            print("Dropped...")

        
        
    
        page += 1

        

    print("Finished for term: \"" + str(term) + "\" (" + str(term_num) + " of " + str(len(queries)) + "). I got " + str(page) + " results.")
    term_num += 1


pd.DataFrame(data).to_csv("src/bing/bing_output_TESTDOC.csv")


            
