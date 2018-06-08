FROM r-base:latest  
  
MAINTAINER Vlad Zaitsev "vladzaitsev@gmail.com"  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
libmysqlclient-dev libssl-dev  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
RUN R -e "install.packages(c('shiny',
'rmarkdown','RMySQL','gridExtra','plotly','flexdashboard','data.table','visNetwork','ggplot2','networkD3'),
repos='https://cran.rstudio.com/')" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
RUN apt-get clean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3838  
COPY ./shiny-server.sh /usr/bin/shiny-server.sh  
RUN chmod 777 /usr/bin/shiny-server.sh  
CMD ["/usr/bin/shiny-server.sh"]

