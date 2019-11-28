# ga-api-benchmark

## Purpose
This project was conducted to establish industry benchmarks within plastic & cosmetic surgery, medical spas, and addiction treatment centers. The secondary purpose of this project is to use the aggregated data to analyze the effects of numerous Google Search Algorithm Upates occurring throughout 2019.

### Data Source
- The data was acquried from multiple Google Analytics accounts utilizing the [Google Analytics API](https://developers.google.com/analytics/devguides/reporting/core/v4/).

### Relational Database
- The relational database used is [SQLite](https://www.sqlite.org/index.html)

### Python Libraries
- Primary Python libraries used include Pandas, Matplotlib, NumPy, Datetime, and OS

## How to Access and Utilize the Google Analytics API
1. [Enabling the API](https://console.developers.google.com/start/api?id=analyticsreporting.googleapis.com&credential=client_key)
    -   Creating a project in the Google API Console
    -   Enabling the API
    -   Creating credentials (cred.json)

## Benefits Google Analytics API vs Google Analytics Native

-   Aggregating data across multiple clients to create industry benchmarks
    -   Ability to compare individual clients to benchmark to assess performance
    -   Analyzing effects of Google Algorithm update
-   Better data visualization with more flexiblity
    -   Better internal reporting for Account Managers and Search Engine Optimization Specialists to use when creating client strategies
    -   Publishing of industry data analysis
-   Combine metrics to get more insight
    -   For example: goal completions per number of sessions
