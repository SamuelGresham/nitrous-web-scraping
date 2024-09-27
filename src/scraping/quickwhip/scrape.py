from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

internal_links = []

# Checks to see if a URL is within the predefined domain
def is_within_domain(url):
    print(url[0])
    return f'https://{urlparse(url).netloc}/' == "www.quickwhip.com.au" or url[0] == "/"

file = open("src/scraping/quickwhip/page.txt", "r")
html = BeautifulSoup(file.read(), features='lxml')
all_anchors = html.select('a[href]')
for element in all_anchors: 
    if is_within_domain(element.get("href")) and "product" in element.get("href"): 
        if element.get("href")[0] == "/":
            print("here")
            internal_links.append("www.quickwhip.com.au"+element.get("href"))
        else:
            internal_links.append(element.get('href'))

res = []

 # List comprehension to remove duplicates from internal_links and export to res
[res.append(x) for x in internal_links if x not in res]  

# Save the explored URLs to the .txt file 
with open(f'src/scraping/URLs/quickwhip_manual.txt', 'w') as f:
    f.write(f"Finished exploring the site https://www.quickwhip.com.au/collections/all. I found {len(res)} unique pages on this site.")
    for line in res:
        print(".")
        f.write(f"https://{line}\n")
