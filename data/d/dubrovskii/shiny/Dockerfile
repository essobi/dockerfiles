FROM r-base:latest  
  
MAINTAINER A.Dubrouski "a1dubrovskii@gmail.com"  
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
R -e "install.packages(c('shiny', 'rmarkdown', 'ggplot2', 'dplyr', 'plotly'),
repos='https://cran.rstudio.com/')" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
# RUN R -e 'if(!require(devtools)) { install.packages("devtools") }; \  
# library(devtools); \  
# install_github("cytoscape/r-cytoscape.js");'  
# RUN R -e "library(devtools); install_cran('plotly')"  
# Install plotly and change ownership otherwise plotly will complain: cannot
open file 'Rplots.pdf'  
# RUN chown -R shiny:shiny /srv/shiny-server  
# Expose Shiny server  
EXPOSE 3838  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

