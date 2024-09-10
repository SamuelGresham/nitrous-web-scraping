import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os.path
from pprint import pprint
import pandas as pd 

# Define globals
domain = "https://www.nangwizard.net/"
internal_links = [domain]
internal_links_searched = []

t = {
    "_": "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
}


# Checks to see if a URL is within the predefined domain
def is_within_domain(url):
    return f'https://{urlparse(url).netloc}/' == domain

# Gets all the linked pages from a URL
def get_pages(url): 
    internal_links_searched.append(url)
    html = BeautifulSoup(requests.get(url).text, features='lxml')
    all_anchors = html.select('a[href]')
    for element in all_anchors: 
        if is_within_domain(element.get("href")): 
            internal_links.append(element.get('href'))

def explore ():
    counter = 0
    res = []
    # Iterates through the URL queue and explores for linked URLs 
    for link in internal_links: 
        if link not in internal_links_searched:
            counter+=1
            print(f"Found a new page ({counter}): {link}")
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
    

# ----------------------- v MAIN LINE v --------------------------- # 

# ~ STEP 1 ~ Find all URLs in the site and save to URLs/{domain}.txt

if os.path.isfile(f'src/scraping/URLs/{urlparse(domain).netloc}.txt'): 
    o = input("URL file already exists. Explore again? [Y/"+ '\033[1m' + "N"+ '\033[0m' + "]")
    if o == "Y":
        cont = True
    else: 
        cont = False
else: 
    cont = True

if cont:
    res = explore()

else: 
    with open(f'src/scraping/URLs/{urlparse(domain).netloc}.txt', 'r') as f:
        res = f.readlines()[1:]

    for i, r in enumerate(res): 
        res[i] = res[i].replace("\n", "")

product_first_level = determine_first_level(res)
print(f"{t['_']}Ok, searching for {domain}{product_first_level}*{t['_']}")

product_urls = []

for url in res: 
    if domain+product_first_level+"/" in url: 
        product_urls.append(url)
        print(url)

print(f"{t['_']}I found {len(product_urls)} items.{t['_']}")

cls_prodname = input("Enter the class for the product name: ")
cls_price    = input("Enter the class for the price: ")
cls_descript = input("Enter the class for the product description: ")

products = []

for url in product_urls: 
    html = BeautifulSoup(requests.get(url).text, features = "lxml") 
    prodname = html.find("h1", {"class": cls_prodname}).text
    price = html.find("p", {"class": cls_price}).text
    descript = html.find("div", {"class": cls_descript}).text
    products.append({
        "prodname": prodname,
        "price": price,
        "descript": descript
    })

pd.DataFrame(products).to_csv("out.csv")


