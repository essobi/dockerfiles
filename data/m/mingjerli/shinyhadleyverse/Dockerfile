FROM rocker/hadleyverse  
# FROM mingjerli/hadleyverseplus  
MAINTAINER Ming-Jer Lee "mingjerli@gmail.com"  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev  
  
# Download and install shiny server  
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
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
# Download and install extra R package  
RUN install2.r --error -d TRUE\  
shinyBS \  
shinythemes \  
treemap \  
networkD3 \  
xts \  
dygraphs \  
glmnet \  
reshape \  
plotly \  
DT \  
plyr \  
IMFData \  
caret \  
zoo \  
PerformanceAnalytics \  
gtrendsR \  
ggfortify \  
&& r -e "remotes::install_github('timelyportfolio/d3treeR')" \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
EXPOSE 3838  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
RUN chmod +x /usr/bin/shiny-server.sh  
  
#ENTRYPOINT ["/usr/bin/shiny-server.sh"]  
CMD ["/usr/bin/shiny-server.sh"]

