import os
import json
from dotenv import load_dotenv
import pandas as pd 
import requests, json, lxml
from bs4 import BeautifulSoup
import time

companies = []

# Load secret .env file
load_dotenv()
# Store credentials
key = os.getenv('WHOIS_KEY')

domainList = pd.read_csv("src/result_classification/final.csv")["URL"].to_list()

print(domainList)
for domain in domainList:
    query_params = {"domainName": domain, "apiKey": key, "outputFormat": "JSON"}
    res = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService", params=query_params, headers={"Content-Type": "application/json"})
    try:
        companies.append({
            "URL": domain,
            "Company": json.loads(res.content)["WhoisRecord"]["registryData"]
        })

        print(f'URL: {domain} is linked to {json.loads(res.content)["WhoisRecord"]["registryData"]}')    
    except:
        companies.append({
            "URL": domain,
            "Company": json.loads(res.content)
        })

        print(f'URL: {domain} failed... dumping all data into the file')

    time.sleep(1)

pd.DataFrame(companies).to_csv("src/whois/registryoutput.csv")
