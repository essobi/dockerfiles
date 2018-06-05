FROM rocker/r-ver:3.3.1  
  
LABEL org.label-schema.license="GPL-2.0,MPL-2.0" \  
org.label-schema.vcs-url="https://github.com/kfsq/gitlab-ci-docker" \  
org.label-schema.vendor="Docker images for use with GitLab CI" \  
maintainer="Kristoffer Winther Balling <kfsq@novonordisk.com>"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
## Debian packages for SSL  
libssl-dev \  
libcurl4-openssl-dev \  
libxml2-dev \  
libpcre3-dev \  
liblzma-dev \  
libicu52 \  
libicu-dev \  
# Debian packages Java (for rJava)  
libbz2-dev \  
openjdk-7-jdk \  
# Debian packages pandoc (for rmarkdown/knitr)  
pandoc \  
# Configure Java for R (for rJava)  
&& R CMD javareconf \  
## Install R packages  
&& Rscript -e "install.packages(c( \  
'import', \  
'ggplot2', \  
'knitr', \  
'magrittr', \  
'stringi', \  
'xml2', \  
'data.table', \  
'stringi', \  
'lubridate', \  
'matrixStats', \  
'whisker', \  
'digest', \  
'RJDBC', \  
'htmlwidgets', \  
'testthat', \  
'plyr', \  
'dplyr', \  
'rmarkdown', \  
'assertive', \  
'ISOweek' \  
))" \  
## Clean up  
&& cd / \  
&& rm -rf /tmp/* \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  

