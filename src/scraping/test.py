import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

domain = "https://nangs.net.au/"
internal_links = [domain]
internal_links_searched = []

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

for i in range(5): 
    for link in internal_links: 
        if link not in internal_links_searched:
            get_pages(link)
            with open(f'src/scraping/URLs/{urlparse(domain).netloc}.txt', 'w') as f:
                for line in internal_links:
                    f.write(f"{line}\n")

    print(f'Iteration {i}: {len(internal_links)} URLs discovered')    




