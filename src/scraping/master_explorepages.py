import os 
import pandas as pd

URLs = list(pd.read_csv("src/result_classification/domain_hit_table.csv")["Domain"])

for url in URLs[7:]:
    print(f"Now exploring {url}!")
    os.system(f"python3 src/scraping/getpages.py https://{url}/")
