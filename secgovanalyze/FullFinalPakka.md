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


```r
# Amazon 10K filed in 2015 
amzn2015
```

```
Financial statements repository
                                                  From         To Rows
ConsolidatedBalanceSheets                   2013-12-31 2014-12-31    2
ConsolidatedStatementsOfCashFlows           2012-12-31 2014-12-31    3
ConsolidatedStatementsOfComprehensiveIncome 2012-12-31 2014-12-31    3
ConsolidatedStatementsOfOperations          2012-12-31 2014-12-31    3
                                            Columns
ConsolidatedBalanceSheets                        28
ConsolidatedStatementsOfCashFlows                33
ConsolidatedStatementsOfComprehensiveIncome      11
ConsolidatedStatementsOfOperations               23
```

```r
# Amazon 10K filed in 2016
amzn2016
```

```
Financial statements repository
                                                  From         To Rows
ConsolidatedBalanceSheets                   2014-12-31 2015-12-31    2
ConsolidatedStatementsOfCashFlows           2013-12-31 2015-12-31    3
ConsolidatedStatementsOfComprehensiveIncome 2013-12-31 2015-12-31    3
ConsolidatedStatementsOfOperations          2013-12-31 2015-12-31    3
                                            Columns
ConsolidatedBalanceSheets                        28
ConsolidatedStatementsOfCashFlows                32
ConsolidatedStatementsOfComprehensiveIncome      11
ConsolidatedStatementsOfOperations               23
```

Slide With Plot
========================================================
