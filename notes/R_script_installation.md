# Intalling the Google Trends Search Narratives R Tool 

## Installing R 
R was downloaded from https://cran.rstudio.com/ and installed according to instructions. 

## Installing Dependencies for GTNarratives.R
Dependencies for GTNarratives.R were installed manually. There is probably an easier way of doing this but I am not sure how. 

Dependencies were installed using the R dependencies installer tool. 

## Installing RStudio
I found it was easiest to run the R script using RStudio. 

RStudio was downloaded from https://posit.co/download/rstudio-desktop/ and installed according to instructions. 

## Running GTNarratives.R 
Initially, GTNarratives.R would not run. 

Line 46 needed to be modified to include the full path to the custom CSS resource. I am not sure why this was, but it may be due to differences in compatibility between Windows and MacOS. 

The script could then be run without issue! 