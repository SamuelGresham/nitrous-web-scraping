import pandas as pd
import matplotlib.pyplot as plt 

domains = list(pd.read_csv("src/result_classification/final.csv")["URL"])
engine_results = pd.read_csv("src/master.csv")
queries = list(pd.read_csv("src/query_exploration/queries_final.csv")["name"])

successful_queries = []
output = []

for index, result in engine_results.iterrows():
    if result["Domain"] in domains: 
        successful_queries.append({
            "Engine": result["Engine"],
            "Term": result["Search term"],
            "Domain": result["Domain"]
        })

successful_queries = pd.DataFrame(successful_queries)

bing_results = successful_queries.query("Engine == 'Bing'")
google_results = successful_queries.query("Engine == 'Google'")

for query in queries: 
    try:
        google_count = google_results["Term"].value_counts()[query]
    except: 
        google_count = 0
    try:
        bing_count = bing_results["Term"].value_counts()[query]
    except: 
        bing_count = 0

    output.append({
        "Term": query,
        "Google_Count": google_count,
        "Bing_Count": bing_count,
        "Total_Count": google_count + bing_count
    })

pd.DataFrame(output).sort_values(by = "Total_Count", ascending=False).to_csv("src/result_classification/query_hit_table.csv")
df = pd.DataFrame(output).sort_values(by = "Total_Count", ascending=False)



queries = []
total_count = []

for out in output: 
    queries.append(out["Term"])
    total_count.append(out["Total_Count"])


#plt.bar(queries, total_count, color ='maroon', 
#        width = 0.4)

#plt.xlabel("Courses offered")
#plt.ylabel("No. of students enrolled")
#plt.title("Students enrolled in different courses")
#plt.show()

df.set_index(["Term"]).plot(kind="bar")
plt.subplots_adjust(bottom=0.5)
plt.xticks(rotation=45, ha='right')
plt.show()