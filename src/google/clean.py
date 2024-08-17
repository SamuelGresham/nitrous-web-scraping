# NOTE: this code was produced with the assistance of generative AI (ChatGPT)

import pandas as pd

df = pd.read_csv("src/google/google_output.csv")

# Assuming df is your DataFrame
# Group by 'URL' and apply the desired transformations
merged_df = df.groupby('URL').apply(
    lambda x: pd.Series({
        'Search term': list(zip(x['Search term'], x['page'])),
        'Site title': x['Site title'].iloc[0],  # Keep the first occurrence of Site title
        'Web snippet': x['Web snippet'].iloc[0],  # Keep the first occurrence of Web snippet
    })
).reset_index()

# Display the resulting DataFrame
merged_df.to_csv("src/google/clean.csv")