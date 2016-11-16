Companies Balance Sheet Analysis
========================================================
author: Karan Sharma
date: 15th November 2016
autosize: true

List of Companies
========================================================

10k forms scraped from: <https://www.sec.gov/>.

- $AMZN
- $AAPL
- $PEP
- $FB
- $GM

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

Getting data
========================================================


```r
#FB forms
fb_url2015 <-'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/fb/2015/fb-20141231.xml'
fb_url2016 <- 'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/fb/2016/fb-20151231.xml'

#PEPSI forms
pep_url2015 <- 'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/pep/2015/pep-20141227.xml'
pep_url2016 <- 'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/pep/2016/pep-20151226.xml'

#AMZN forms
amzn_url2015<-'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/amzn/2015/amzn-20141231.xml'
amzn_url2016<- 'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/amzn/2016/amzn-20151231.xml'

#AAPL forms
aapl_url2015 <-'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/aapl/2015/aapl-20140927.xml'
aapl_url2016 <- 'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/aapl/2016/aapl-20150926.xml'

#GM forms
gm_url2015 <-'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/GM/2015/gm-20141231.xml'
gm_url2016 <-'https://raw.githubusercontent.com/mr-karan/BigDataAssignments/master/secgovanalyze/GM/2016/gm-20151231.xml'
```