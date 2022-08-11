# surfs_up

## Overview

An investor considering opening a business in Oahu, Hawaii has requested information on regional temperatures for June and December. This analysis provides summary statistics using data from a SQLite database, which was converted to a pandas dataframe.

## Results

- June's average temperature is 74.9 degrees, and December's average temperature is 71 degrees.
- The recorded temperatures ranged from 64 to 85 degrees in June, and from 56 to 83 degrees in December.
- More temperatures were recorded in June (1,700) than in December (1,517)

![june summary](/images/june_summary.png) ![dec summary](/images/dec_summary.png)

![june hist](/images/june_hist.png) ![dec hist](/images/dec_hist.png)

## Summary

June is warmer than December in Oahu (although not by much, compared to other regions!). To further flesh out the weather differences, you could write a query that shows the average temperatures measured by each station, which might reveal some bias in reporting. You could also refactor the queries in this analysis to produce summary statistics on precipitation rather than temperature. That could be just as important as temperature for the prospects of a business in this area.
