## Remove duplicates from the raw data from GTNarratives.R and format nicely 

## -- IMPORTS --
import pandas as pd 

# Define the path for the raw data
path = "/Users/samuelgresham/Library/CloudStorage/OneDrive-TheUniversityofSydney(Students)/Documents/SCDL3992_src/nitrous-web-scraping/src/query_exploration/queryexploration_raw.csv"

# Read from the CSV and drop unwanted columns
df = pd.read_csv(path, header=0).drop(["Unnamed: 0", "start_date", "end_date", "mid", "isBreakout", "date_level", "group_id"], axis=1)

# Remove duplicated title values, if any.
df = df.drop_duplicates(subset=["title"])

# Write to queryexploration_clean.csv with the cleaned data
df.to_csv("src/query_exploration/queryexploration_clean.csv")