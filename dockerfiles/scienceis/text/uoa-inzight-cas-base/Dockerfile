# ------------------------------
#
# Base build for Census At School (CAS)
# 
# ------------------------------

FROM scienceis/uoa-inzight-base:latest

MAINTAINER "Science IS Team" ws@sit.auckland.ac.nz

# install R packages specific to iNZight CAS
RUN apt-get update \
  && apt-get install -q -y libmysqlclient-dev libcurl4-openssl-dev \
  && R -e "install.packages(c('RMySQL', 'plyr', 'lattice', 'RCurl', 'RJSONIO', 'whisker', 'yaml'), repos='http://cran.rstudio.com/', lib='/usr/lib/R/site-library')" \
  && wget -O rCharts.tar.gz https://github.com/ramnathv/rCharts/archive/master.tar.gz \
  && R -e "install.packages('rCharts.tar.gz', repos = NULL)" \
  && rm -rf rCharts.tar.gz \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

