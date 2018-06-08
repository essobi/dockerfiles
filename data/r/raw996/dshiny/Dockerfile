FROM r-base:latest  
  
MAINTAINER Winston Chang "winston@rstudio.com"  
  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
libgdal-dev \  
libproj-dev \  
libgsl0-dev  
  
RUN apt-get -y install libxml2-dev libssl-dev  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
R -e "install.packages(c('shiny', 'rmarkdown', 'ggvis', 'data.table',
'shinydashboard', 'flexdashboard', 'devtools', 'RCurl', 'readxl', 'plotly',
'DT', 'zoo', 'ggplot2', 'acepack', 'corr', 'igraph', 'vegan', 'ggdendro',
'ClustOfVar', 'data.table', 'shinyBS', 'ineq', 'ggrepel', 'htmlTable',
'rredis', 'pander', 'directlabels', 'openxlsx', 'gmailr','zip','glm2'),
repos='https://cran.rstudio.com/')" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
RUN R -e "devtools::install_github('bwlewis/doRedis',
ref='e4c1a81aa6bd0e4bfba2a7b465f08f822fd8c0d3')"  
RUN R -e
"devtools::install_github('Appsilon/shiny.router',ref='7d9bc757ea31a1fe8faea6a5817c8adda97a0be0')"  
RUN R -e "devtools::install_github('raubreywhite/RAWmisc')"  
RUN R -e "devtools::install_github('raubreywhite/fhi')"  
  
# install ssh and git  
RUN apt-get update && apt-get install -y ssh git  
  
EXPOSE 3838  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
#COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
  
CMD ["/usr/bin/shiny-server.sh"]

