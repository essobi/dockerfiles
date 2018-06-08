# Adapted from https://github.com/rocker-org/shiny  
FROM dougmet/r-base:3.3.2  
MAINTAINER Doug Ashton "dashton@mango-solutions.com"  
ENV SHINY_SERVER_VERSION 1.5.2.837  
RUN apt-get update && apt-get install -y \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev  
  
# Download and install shiny server  
RUN wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-${SHINY_SERVER_VERSION}-amd64.deb" -O
ss-${SHINY_SERVER_VERSION}.deb && \  
gdebi -n ss-${SHINY_SERVER_VERSION}.deb && \  
rm ss-${SHINY_SERVER_VERSION}.deb && \  
R -e "install.packages('shiny')" && \  
R -e "install.packages('rmarkdown')" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
EXPOSE 3838  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

