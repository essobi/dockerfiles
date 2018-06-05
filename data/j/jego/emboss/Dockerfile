#################################################################  
# Dockerfile  
# Software: emboss  
# Software Version: 6.6.0-1  
# Description: Emboss the european molecular biology open software suite  
# Website: http://emboss.sourceforge.net/what/  
# Tags: Proteomics|Genomics|General  
# Provides: emboss 6.6.0-1  
#################################################################  
  
# Base docker image  
FROM ubuntu:14.04  
MAINTAINER test@armadillo.uqam.ca  
  
# Install EMBOSS amd embassy-domainatrix package  
RUN apt-get update && apt-get install -y \  
emboss=6.6.0-1 \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

