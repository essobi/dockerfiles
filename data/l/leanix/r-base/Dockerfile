FROM rocker/r-base  
  
## Install some external dependencies. 360 MB  
RUN apt-get update && apt-get -t unstable install -y krb5-multidev \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
libcairo2-dev/unstable \  
libssl-dev/unstable \  
libcurl4-gnutls-dev \  
libgsl0-dev \  
libpq-dev \  
libxcb1-dev/unstable \  
libxdmcp-dev/unstable \  
libxml2-dev/unstable \  
libxslt1-dev \  
libxt-dev \  
libmysqlclient-dev \  
krb5-multidev \  
vim \  
openjdk-7-jdk \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
## fixes an rJava bug  
RUN R CMD javareconf  
  
## Install the R packages. 210 MB  
RUN install2.r --error \  
ggplot2 \  
httr \  
reshape2 \  
tidyr \  
base64enc \  
Cairo \  
data.table \  
downloader \  
gridExtra \  
gtable \  
hexbin \  
Hmisc \  
jpeg \  
lattice \  
png \  
RPostgreSQL \  
RMySQL \  
rJava \  
XML \  
mailR \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  

