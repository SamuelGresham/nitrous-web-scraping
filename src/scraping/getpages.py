import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os.path
from pprint import pprint
import pandas as pd 

# Define globals
domain = sys.argv[1]
internal_links = [sys.argv[1]]
internal_links_searched = []

t = {
    "_": "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
}


# Checks to see if a URL is within the predefined domain
def is_within_domain(url):
    return f'https://{urlparse(url).netloc}/' == domain or url[0] == "/"

# Gets all the linked pages from a URL
def get_pages(url): 
    internal_links_searched.append(url)
    html = BeautifulSoup(requests.get(url).text, features='lxml')
    all_anchors = html.select('a[href]')
    for element in all_anchors: 
        if is_within_domain(element.get("href")): 
            if element.get("href")[0] == "/":
                internal_links.append(domain+element.get("href"))
            else:
                internal_links.append(element.get('href'))

def explore ():
    counter = 0
    res = []
    # Iterates through the URL queue and explores for linked URLs 
    for link in internal_links: 
        if link not in internal_links_searched:
            counter+=1
            print("~", end='', flush=True)
            get_pages(link)

    # List comprehension to remove duplicates from internal_links and export to res
    [res.append(x) for x in internal_links if x not in res]  

    # Save the explored URLs to the .txt file 
    with open(f'src/scraping/URLs/{urlparse(domain).netloc}.txt', 'w') as f:
        f.write(f"Finished exploring the site {domain}. I found {len(res)} unique pages on this site.")
        for line in res:
            f.write(f"{line}\n")

    return res 

def determine_first_level (res): 
    first_levels = []

    for line in res: 
        try: 
            first_levels.append(line.split("/")[3])
        except: 
            pass

    first_levels = list(set(first_levels))
    for index, value in enumerate(first_levels): 
        print(f'{index}: {value}')

    first_level_index = input("Which first-level are the products located under? ")

    if int(first_level_index) < 0 or int(first_level_index) >= len(first_levels): 
        raise ValueError("The index provided is out of bounds.")
    else: 
        return first_levels[int(first_level_index)]

explore()