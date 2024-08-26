# Exports data into the search_results.csv file

import pandas as pd 
from urllib.parse import urlparse

def extract_domain(url):
    return urlparse(url).netloc

df = pd.read_csv("src/google/google_output.csv", index_col = [0])
df['Engine'] = "Google"
df['Domain'] = df['URL'].apply(extract_domain)

df = df[["Engine", "Search term", "page", "Site title", "Web snippet", "Domain", "URL"]]

df = df.sort_values(by = ["URL"])

df.to_csv("src/search_results.csv")