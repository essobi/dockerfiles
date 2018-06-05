#################################################################  
# Dockerfile  
# Software: embassy-domalign  
# Software Version: 0.1.650-1  
# Description: Extra EMBOSS commands for protein domain alignment.  
# Website: http://emboss.sourceforge.net/what/  
# Tags: Proteomics|Genomics|General  
# Provides: embassy-domalign 0.1.650-1  
#################################################################  
  
# Base docker image  
FROM jego/emboss  
MAINTAINER test@armadillo.uqam.ca  
  
# Install embassy-domalign package  
RUN apt-get --quiet update \  
&& apt-get install -qqy \  
embassy-domalign=0.1.650-1 \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

