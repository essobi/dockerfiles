FROM r-base:latest  
  
MAINTAINER Borja Lorente "blorente@ucm.es"  
RUN apt-get update && apt-get install -y \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
libssl-dev \  
libxml2-dev  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
RUN R -e "install.packages(c('tidyverse', 'shiny', 'rmarkdown', 'knitr', 'tm',
'memoise', 'magrittr', 'visNetwork', 'igraph', 'stringr', 'janitor',
'RSQLite', 'dbplyr'))"  
  
COPY shiny-server.conf home/etc/shiny-server/shiny-server.conf  
COPY /myapp home/srv/shiny-server/  
  
EXPOSE 80  
COPY shiny-server.sh home/usr/bin/shiny-server.sh  
  
CMD ["sudo home/usr/bin/shiny-server.sh"]  

