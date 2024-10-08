# Site Scraping

## Overview
For each site, the following data is collected: 
1) All products - URL, title, category
2) Delivery timeframes and delivery fee
3) Locations serviced
4) Misuse warnings
5) ID check warnings
6) Customer reviews
7) Bulk pricing incentives

## Automated product retrieval 
`scrape_page.py` is used to retrieve products from a given domain. Recursive exploration is used to find all pages within a given domain. The first-level subdirectory where products are stored is then manually selected, and the element containing the product name is chosen. The script then manually extracts the URL and product title of all products within the domain. 

## Manual product categorisation 
Products are manually interrogated and categorised as follows: 

| Category Code | Description                                                                             |
|---------------|-----------------------------------------------------------------------------------------|
| NOX-CHU       | Single use UNFLAVOURED nitrous oxide cream chargers                                     |
| NOX-CHF       | Single use FLAVOURED nitrous oxide cream chargers                                       |
| NOX-TKU       | Nitrous oxide tank containing several doses of UNFLAVOURED nitrous oxide                |
| NOX-TKF       | Nitrous oxide tank containing several doses of FLAVOURED nitrous oxide                  |
| NOX-OTH       | Any nitrous oxide products which do not fit the criteria above (specify in annotations) |
| PPH-CRM       | Paraphenalia designed to produce whipped cream                                          |
| PPH-CRA       | Paraphenalia designed to "crack" chargers without whipped cream production              |
| PPH-REG       | Regulators for large gas tanks                                                          |
| PPH-BLN       | Balloons                                                                                |
| PPH-OIN       | Other inhalation devies                                                                 |
| PPH-OTH       | Other paraphenalia (specify in annotations)                                             |
| OTH-CRM       | Cream                                                                                   |
| OTH-BKE       | Baking supplies                                                                         |
| OTH-PTY       | Party supplies (excluding balloons)                                                     |
| OTH-CBO       | Combination packs                                                                       |
| OTH-OTH       | Other (specify in annotations)                                                          |

## Manual bulk pricing collection
Bulk pricing is collected manually from suitable sites.

## Other
Other data are collected manually from websites (e.g., product reviews, misuse warnings...) 

