FROM rocker/verse  
MAINTAINER "Michael Ruepp" michael.ruepp@crate.io  
  
## JDK and rJava  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ed \  
default-jdk \  
default-jre \  
icedtea-netx \  
libbz2-dev \  
libcairo2-dev \  
libgdal-dev \  
libicu-dev \  
liblzma-dev \  
libproj-dev \  
libgeos-dev \  
libgsl0-dev \  
librdf0-dev \  
librsvg2-dev \  
libv8-dev \  
libxcb1-dev \  
libxdmcp-dev \  
libxslt1-dev \  
libxt-dev \  
mdbtools \  
netcdf-bin \  
&& . /etc/environment \  
## Install Alpla Dependencies: ggplot2 provided by verse image  
&& install2.r --error --repos $MRAN --deps TRUE \  
rJava tidyr reshape2 dplyr DAAG bit64 zoo sqldf RJDBC \  
## Reconfigure Java R  
&& R CMD javareconf \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
## tidyverse, devtools and related R packages already inherited from
rocker/verse  
## httr authentication uses this port  
EXPOSE 1410  
ENV HTTR_LOCALHOST 0.0.0.0  
#Export projects Volume  
VOLUME /home/rstudio/projects  
  
RUN chown -R :rstudio /usr/local/lib/R/site-library && chown -R
rstudio:rstudio /home/rstudio && service rstudio-server restart  

