FROM r-base:latest  
  
MAINTAINER Kevin Park ”kevin@carlabs.com"  
# install additional packages needed  
RUN apt-get update && apt-get install -y && apt-get install -y -t unstable \  
curl \  
gdebi-core \  
git \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libpq-dev\  
libssl-dev\  
libxt-dev \  
libxml2-dev\  
unp \  
unixodbc \  
unixodbc-dev \  
odbc-postgresql \  
supervisor\  
python-pip \  
r-base  
  
# Install Shiny  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \  
R -e "install.packages(c('shinydashboard', 'leaflet','dplyr','stringr',
'RPostgreSQL',
'DT','tidyr','dygraphs','xts','devtools','ggplot2','lubridate','tidyr','rjson','googlesheets','htmlwidgets'),
repos='https://cran.r-project.org/')"  
  

