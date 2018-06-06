FROM cannin/r-base:ubuntu-14.04.4_r-3.3.2_java-8  
MAINTAINER cannin  
  
##### R: SHINY  
# Install Shiny  
RUN apt-get install -y \  
sudo \  
wget \  
curl \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev  
  
# Download and install Shiny server  
# Cannot use ADD because using variables; Using wget instead  
ENV SHINY_SERVER_VERSION 1.5.2.837  
# Get version number of Shiny  
#RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt"  
RUN wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-${SHINY_SERVER_VERSION}-amd64.deb" -O
ss-latest.deb && \  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
# Install shiny related packages  
RUN R -e "install.packages(c('rmarkdown', 'shiny'))"  
  
RUN R -e 'if(!require(devtools)) { install.packages("devtools") }; \  
library(devtools); \  
install_github("cytoscape/r-cytoscape.js");'  
  
RUN R -e "library(devtools); install_cran('plotly')"  
  
COPY r-requirements.txt /  
COPY installPackages.R /  
COPY runInstallPackages.R /  
RUN R -e 'source("runInstallPackages.R")'  
  
# Copy sample apps  
RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
# Setup Shiny log  
RUN mkdir -p /var/log/shiny-server  
RUN chown shiny:shiny /var/log/shiny-server  
  
# Install plotly and change ownership otherwise plotly will complain: cannot
open file 'Rplots.pdf'  
RUN chown -R shiny:shiny /srv/shiny-server  
  
# Expose Shiny server  
EXPOSE 3838  
#CMD ["shiny-server"]  

