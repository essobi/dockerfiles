FROM rocker/verse  
MAINTAINER "Carl Boettiger and Dirk Eddelbuettel" rocker-
maintainers@eddelbuettel.com  
  
## Install some external dependencies.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
icedtea-netx \  
libgdal-dev \  
libproj-dev \  
libgeos-dev \  
libgsl0-dev \  
librsvg2-dev \  
libxcb1-dev \  
libxdmcp-dev \  
libxslt1-dev \  
libxt-dev \  
mdbtools \  
netcdf-bin \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
## tidyverse, devtools and related R packages already inherited from
rocker/verse  
## httr authentication use external-facing localhost  
ENV HTTR_LOCALHOST 0.0.0.0  

