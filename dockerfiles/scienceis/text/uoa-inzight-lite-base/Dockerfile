# ----------------------------------------
#
# The primary intention of this image is to inherit
# uoa-inzight-base image and install Lite specific 
# packages
#
# ----------------------------------------
FROM scienceis/uoa-inzight-base:latest

MAINTAINER "Science IS Team" ws@sit.auckland.ac.nz

ENV BUILD_DATE "2015-12-03"
# Install (via R) all of the necessary packages (R will automatially install dependencies):
RUN R -e "install.packages(\
             c('RJSONIO', 'iNZightMR', 'iNZightTS', 'iNZightRegression', 'iNZightPlots', 'GGally', 'gpairs'), \
             repos = c('http://docker.stat.auckland.ac.nz/R', 'http://cran.stat.auckland.ac.nz') \
           )" \
  && rm -rf /tmp/* /var/tmp/*

