FROM rocker/hadleyverse  
MAINTAINER "Brock Tibert" btibert3@gmail.com  
  
## Manually install (useful packages from) the SUGGESTS list of the above
packages.  
## (because --deps TRUE can fail when packages are added/removed from CRAN)  
RUN install2.r --error \  
-r "https://cran.rstudio.com" \  
-r "http://www.bioconductor.org/packages/release/bioc" \  
&& r -e
'source("https://raw.githubusercontent.com/MangoTheCat/remotes/master/install-
github.R")$value("mangothecat/remotes")' \  
&& r -e 'remotes::install_github("nicolewhite/RNeo4j")' \  
&& r -e 'remotes::install_github("stattleship/stattleship-r@helpers")' \  
&& r -e 'remotes::install_github("jeroen/mongolite")' \  
&& r -e 'remotes::install_github("mkearney/rtweet")' \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  

