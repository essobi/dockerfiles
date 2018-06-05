FROM rocker/verse:latest  
MAINTAINER "Matt Barry" mrb@greatgray.org  
  
## Add more R and R-Forge packages onto verse  
## staged for incremental images  
RUN apt-get update -qq \  
&& apt-get clean  
  
RUN . /etc/environment \  
&& install2.r --error \  
\--repos $MRAN \  
\--deps TRUE \  
scales directlabels Quandl downloader Rcpp TTR XML boot  
  
## grab 2017 quantmod with Yahoo URL fix  
RUN . /etc/environment \  
&& installGithub.r \  
joshuaulrich/xts \  
joshuaulrich/quantmod \  
braverock/FinancialInstrument \  
braverock/PerformanceAnalytics \  
braverock/blotter \  
braverock/quantstrat  
  
  
  

