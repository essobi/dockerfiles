  
FROM rocker/rstudio  
MAINTAINER Heidi Seibold  
  
## Software needed (subversion, stuff for R XML package, Latex)  
RUN apt-get update \  
&& apt-get install -y subversion \  
r-cran-xml \  
texlive texlive-latex-extra texinfo  
  
## From hadleyverse dockerfile (just copied it to get rJava running)  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends -t unstable \  
default-jdk \  
default-jre \  
gdal-bin \  
icedtea-netx \  
libatlas-base-dev \  
libcairo2-dev \  
libgsl0-dev \  
libgdal-dev \  
libgeos-dev \  
libgeos-c1v5 \  
librdf0-dev \  
libssl-dev \  
libmysqlclient-dev \  
libpq-dev \  
libsqlite3-dev \  
libv8-dev \  
libxcb1-dev \  
libxdmcp-dev \  
libxml2-dev \  
libxslt1-dev \  
libxt-dev \  
netcdf-bin \  
qpdf \  
r-cran-rgl \  
ssh \  
vim \  
&& R CMD javareconf \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
## R packages  
RUN install2.r --error \  
rJava \  
ggplot2 \  
knitr \  
plyr  

