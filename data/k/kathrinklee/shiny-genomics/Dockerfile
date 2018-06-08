############################################################  
# Dockerfile to build container with shiny server to run  
# genomics analysis suite  
# Based on r-base  
############################################################  
  
FROM r-base:latest  
  
# File Author / Maintainer  
MAINTAINER Kathrin Klee <klee@uni-bonn.de>  
  
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
R -e
"install.packages(c('shiny','rmarkdown','shinyjs','shinyBS','RColorBrewer','stringr','formula.tools','yarrr','data.table','fdrtool','VennDiagram','colorspace','gplots','webshot'),
dependencies = TRUE, repos='https://cran.rstudio.com/')" && \  
R -e
"library(c('shiny','rmarkdown','shinyjs','shinyBS','RColorBrewer','stringr','formula.tools','yarrr','data.table','fdrtool','VennDiagram','colorspace','gplots','webshot'))"
&& \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
EXPOSE 3838  
  
#COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server"]  

