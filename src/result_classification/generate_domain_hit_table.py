import pandas as pd 

domains = list(pd.read_csv("src/result_classification/final.csv")["URL"])
engine_results = pd.read_csv("src/master.csv")
bing_results = engine_results.query("Engine == 'Bing'")
google_results = engine_results.query("Engine == 'Google'")
out = []

for domain in domains: 
    try:
        google_count = google_results["Domain"].value_counts()[domain]
    except: 
        google_count = 0
    try: 
        bing_count = bing_results["Domain"].value_counts()[domain]
    except: 
        bing_count = 0

    out.append({
        "Domain": domain,
        "Google_Count": google_count,
        "Bing_Count": bing_count,
        "Total_Count": google_count + bing_count
    })    

pd.DataFrame(out).sort_values(by = "Total_Count", ascending=False).to_csv("src/result_classification/domain_hit_table.csv")
