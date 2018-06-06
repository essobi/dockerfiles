#################################################################  
# Dockerfile  
# Software: embassy-phylip  
# Software Version: 3.69.650-2  
# Description: EMBOSS conversions of the programs in the phylip package  
# Website: http://emboss.sourceforge.net/what/  
# Tags: Proteomics|Genomics|General  
# Provides: embassy-phylip 3.69.650-2  
#################################################################  
# Base docker image  
FROM jego/emboss  
MAINTAINER test@armadillo.uqam.ca  
  
# Install embassy-phylip package  
RUN apt-get --quiet update \  
&& apt-get install -qqy \  
embassy-phylip=3.69.650-2 \ Looks like doesn't pass the docker hub building  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

