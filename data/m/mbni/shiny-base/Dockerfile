FROM mbni/r-base  
  
MAINTAINER "Keqiang Li" lkq@umich.edu  
  
# system libraries of general use  
RUN apt-get update && apt-get install -y \  
sudo \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev \  
libssl-dev \  
libssh2-1-dev \  
libssl1.0.0 \  
libxml2-dev \  
libmariadb-client-lgpl-dev  
  
# basic shiny functionality  
RUN R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cloud.r-project.org/')"  
  
COPY Rprofile.site /usr/lib/R/etc/  
  
EXPOSE 3838  

