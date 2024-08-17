# NOTE: this code was produced with the assistance of generative AI (ChatGPT)

import pandas as pd
from urllib.parse import urlparse


df = pd.read_csv("src/google/google_output.csv")
# Function to extract the domain from a URL
def extract_domain(url):
    return urlparse(url).netloc

# Assuming df is your DataFrame
# Add a new column to df for the domain
df['Domain'] = df['URL'].apply(extract_domain)

# Group by 'Domain' and aggregate the data
merged_df = df.groupby('Domain').agg({
    'Search term': lambda x: list(set(zip(x, df.loc[x.index, 'page']))),  # Combine and deduplicate tuples of 'Search term' and 'page'
    'Site title': 'first',  # Keep the first occurrence of 'Site title'
    'Web snippet': 'first',  # Keep the first occurrence of 'Web snippet'
    'URL': lambda x: list(set(x))  # Collect all URLs, removing duplicates
}).reset_index()

# Display the resulting DataFrame
merged_df.to_csv("src/google/clean_domain.csv")