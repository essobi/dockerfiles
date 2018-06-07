FROM rocker/r-base  
  
MAINTAINER Phillip Labuschagne <philliplab@gmail.com>  
  
RUN apt-get update && apt-get install -y libcurl4-openssl-dev  
  
RUN R -e "local({r <\- getOption('repos'); \  
r['CRAN'] <\- 'http://cran.rstudio.com'; \  
options(repos=r) \  
}); \  
source('http://bioconductor.org/biocLite.R'); \  
biocLite('Biostrings', ask=FALSE); \  
install.packages('devtools'); \  
library(devtools); \  
install_github('rstudio/shiny'); \  
install_github('philliplab/EpitopeMatcher'); \  
library(EpitopeMatcher)"  
  
EXPOSE 5436  

