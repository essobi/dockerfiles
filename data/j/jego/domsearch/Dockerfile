#################################################################  
# Dockerfile  
# Software: embassy-domsearch  
# Software Version: 1:0.1.650-1  
# Description: Extra EMBOSS commands to search for protein domains  
# Website: http://emboss.sourceforge.net/what/  
# Tags: Proteomics|Genomics|General  
# Provides: embassy-domsearch 1:0.1.650-1  
#################################################################  
  
# Base docker image  
FROM jego/emboss  
MAINTAINER test@armadillo.uqam.ca  
  
# Install embassy-domsearch package  
RUN apt-get --quiet update \  
&& apt-get install -qqy \  
embassy-domsearch=1:0.1.650-1 \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

