# ga-api-benchmark (on-going project)

## Purpose
This project was conducted to establish industry benchmarks for website traffic, engagement, and conversions for medical device companies, plastic & cosmetic surgery businesses, medical spas, and addiction treatment centers. The secondary purpose of this project is to use the aggregated data to analyze the effects of numerous Google Search Algorithm Upates occurring throughout 2019. This is an ongoing project that has not yet been completed.

### Data Source
- The data was acquried from multiple Google Analytics accounts utilizing the [Google Analytics API](https://developers.google.com/analytics/devguides/reporting/core/v4/).

### Relational Database
- The relational database used is [SQLite](https://www.sqlite.org/index.html)

### Python Libraries
- Primary Python libraries used include pandas, matplotlib, NumPy, datetime, and os

## How to Access and Utilize the Google Analytics API
-   [Enabling the API](https://console.developers.google.com/start/api?id=analyticsreporting.googleapis.com&credential=client_key)
    -   Creating a project in the Google API Console
    -   Enabling the API
    -   Creating credentials (cred.json)
    
## How to Get This Project Running Locally 
-   After following the setup guide for [Google Analytics API using Python](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py) you will need to grant read and analyze access to the email address on the Google Analytics accounts you want to pull data from. This email should be provided to you by Google
-   Add the view id of every Google Analytics account you want to pull data from into the config.py file
-   Run main.py, which will pull Google Analytics data into the SQLite database and then into a CSV file in the sheets folder
-   Open ga-api-benchmark.ipynb using Jupyter Notebook and run the cells which will manipulate the data and plot it according to the analysis conducted
## Benefits Google Analytics API vs Google Analytics Native  
-   Aggregating data across multiple clients to create industry benchmarks
    -   Ability to compare individual clients to benchmark to assess performance
    -   Analyzing effects of Google Algorithm update
-   Better data visualization with more flexiblity
    -   Better internal reporting for Account Managers and Search Engine Optimization Specialists to use when creating client strategies
    -   Publishing of industry data analysis
-   Combine metrics to get more insight
    -   For example: goal completions per number of sessions
