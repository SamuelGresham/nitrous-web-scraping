# Search Query Selection Protocol 

## Context
In order to extract search results which reflect the true web market for nitrous oxide sales in Australia, we first must identify which nitrous oxide related search terms: 

1. Are most commonly queried in Australia 
2. Yield webpages which sell nitrous oxide (rather than simply provide information regarding nitrous oxide)

## Methods
This method is based on the findings that **only 0.44% of Google Search users reach the second page of Google Search results**. Hence, to emulate the pages that users will actually interact with when using online search engines, results have been limited to the first page.

![search diagram](img/search_analysis.png "Search diagram")

## Step 1: exploring related search terms
For this step, the "Google Trends Narratives" tool was used to explore for terms related to the master query "nitrous oxide".

A recursive depth of 2 was used, with region set to "Australia: all" and time interval of 12 months. Data was used since January 1 2020. 

This left me with a long list of related search terms. This list can be found in `src/query_exploration/queryexploration_raw.csv`.

## Step 2: ranking search terms based on set criteria
A python script was written to query the first-page results (FPRs) for each identified search term. The title of each search result was then compared with a list of known terms relating to nitrous oxide sale:

`hit_list = ["buy","sale","delivery","purchase","quick","24/7", "$", "fast", "charger"]`

The percentage of FPRs that fit this criteria was then calculated for each search term. 

The majority of search terms returned 0% FPRs which matched the criteria, indicating that these search terms did not yield sites selling nitrous oxide. On the other hand, several sites returned 100% FPRs which matched the criteria, indicating that these are high-yield search terms for exploring the online market for nitrous oxide sales.

## Step 3: determining the final search terms
It was decided that a criteria of $\geq50\%$ FPRs must match the criteria in order to be included in the study. In addition, some search terms were removed which clearly did not relate to the sale of illicit nitrous oxide: 

| Search Term Removed (%FPRs fit criteria)      | Reason for Removal                      | 
| --------------------------------------------- | --------------------------------------- | 
| calcium oxide (50%)                           | Unrelated chemical entity               |
| fast and furious (85.71%)                     | Relates to genuine use of nitrous oxide |
| nos fast and furious (100%)                   | Relates to genuine use of nitrous oxide |

This leaves a list of 35 search terms for inclusion in this study.

## Included search terms

| Search Term                      | %FPRs fit criteria |
|----------------------------------|--------------------|
| nangs delivery near me           | 100                |
| melbourne nang delivery          | 100                |
| nangs buy                        | 100                |
| nangs near me                    | 100                |
| melbourne nangs delivery         | 100                |
| nangs sydney                     | 100                |
| nang delivery                    | 100                |
| nangs buy melbourne              | 100                |
| cream chargers                   | 100                |
| nangs perth                      | 100                |
| whipped cream chargers           | 100                |
| nangs delivery                   | 100                |
| melbourne nangs                  | 100                |
| nang sydney                      | 100                |
| nangs delivery melbourne         | 100                |
| buy nangs                        | 100                |
| nangs melbourne                  | 100                |
| nangs cream chargers             | 90                 |
| nangs delivery brisbane          | 90                 |
| where to buy nangs               | 88.8888889         |
| nitrous oxide buy                | 80                 |
| where to buy nitrous oxide       | 77.7777778         |
| nitrous oxide canister           | 77.7777778         |
| buy nitrous oxide canisters      | 77.7777778         |
| buy nitrous oxide                | 70                 |
| nangs brisbane                   | 70                 |
| best nangs                       | 70                 |
| nitrous oxide canisters for sale | 70                 |
| nitrous oxide for sale           | 70                 |
| nitrous oxide whipped cream      | 70                 |
| nitrous oxide canisters          | 66.6666667         |
| nang city                        | 60                 |
| all night nangs                  | 57.1428571         |
| nitrous oxide tank               | 50                 |
| nang cracker                     | 50                 |