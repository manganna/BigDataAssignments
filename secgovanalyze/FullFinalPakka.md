Company Balance Sheet Analysis
========================================================
author: Karan Sharma
date: 15th November 2016
autosize: true

List of Companies
========================================================

10k forms scraped from: <https://www.sec.gov/>.

- $AMZN (Amazon)
- $AAPL (Apple)
- $PEP (Pepsi)
- $FB (Facebook)
- $GM (General Motors)

Setting up things
========================================================


```r
# To parse XML documents
library(XBRL)
old_o <- options(stringsAsFactors = FALSE)
# To visualize results
library(plotly)
library(ggplot2)
# To analyze balance sheets
library(finstr)
# Data munging
library(dplyr)
setwd("~/Work/BigDataAssignments/secgovanalyze")
```

Analyzing Amazon
========================================================


```r
#AMZN forms
amzn_url2015<-'http://localhost:8000/amzn/2015/amzn-20141231.xml'
amzn_url2016<- 'http://localhost:8000/amzn/2016/amzn-20151231.xml'
amzn_2015 <- xbrlDoAll(amzn_url2015)
amzn_2016 <- xbrlDoAll(amzn_url2016)
options(old_o)
amzn2015 <- xbrl_get_statements(amzn_2015)
amzn2016 <- xbrl_get_statements(amzn_2016)
```

Amazon 10K in 2015
========================================================

![picture of spaghetti](amzn/amzn2015.png)

## Amazon 10K in 2016

![picture of spaghetti](amzn/amzn2016.png)

Merge the result!
========================================================


```r
amzn <- merge(amzn2015,amzn2016)
amznIncome <- merge(amzn2015$ConsolidatedStatementsOfComprehensiveIncome, amzn2016$ConsolidatedStatementsOfComprehensiveIncome)
amznSOP <- merge(amzn2015$ConsolidatedStatementsOfOperations,amzn2016$ConsolidatedStatementsOfOperations)
amznBalanceSheet<- merge(amzn2015$ConsolidatedBalanceSheets,amzn2016$ConsolidatedBalanceSheets)
```
![picture of spaghetti](amzn/amazonbs.png)

Financial ratios!
========================================================
It's the ratio of current assests / current liabilities.  



```r
amznBalanceSheet %>% transmute(
  date = endDate, 
  CurrentRatio = AssetsCurrent / LiabilitiesCurrent
)
```

```
        date CurrentRatio
1 2013-12-31     1.071584
2 2014-12-31     1.115276
3 2015-12-31     1.075961
```

`Inference : Amazon consistently had a ratio of 1.0 or greater which indicates that Amazon possesed more assets than liablities, which is a good sign for company's growth.`

Visualize the result!
========================================================