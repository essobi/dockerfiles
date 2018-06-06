# DOCKER-VERSION 1.0  
FROM dit4c/dit4c-container-base:debian  
MAINTAINER t.dettrick@uq.edu.au  
  
# Install R  
# - R  
# - libcurl-devel (necessary for RCurl package, a dependency of devtools)  
RUN echo "deb https://cran.csiro.au/bin/linux/debian jessie-cran3/" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480 && \  
apt-get update && \  
apt-get install -y r-base gdebi-core libcurl4-openssl-dev libssl-dev && \  
export PKG=rstudio-server-1.0.136-amd64.deb && \  
cd /tmp && \  
curl -LOs https://download2.rstudio.org/$PKG && \  
gdebi --non-interactive $PKG && \  
rm $PKG && \  
apt-get clean  
  
# Install R packages used in intermediate bootcamp  
RUN Rscript -e \  
" options(repos=structure(c(CRAN='https://cran.csiro.au'))); \  
install.packages('ggplot2', dependencies = TRUE); \  
install.packages(c( \  
'knitr', \  
'testthat', \  
'assertthat', \  
'stringr', \  
'pander', \  
'plyr', \  
'dplyr', \  
'ggthemes', \  
'reshape2', \  
'gridExtra', \  
'RCurl', \  
'devtools', \  
'httr', \  
'git2r', \  
'data.table'))"  
# Add supporting files (directory at a time to improve build speed)  
COPY etc /etc  
COPY var /var  
  
# Check nginx config is OK  
RUN nginx -t  

